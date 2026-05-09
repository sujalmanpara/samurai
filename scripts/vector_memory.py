#!/usr/bin/env python3
"""
SAMURAI Vector Memory — Semantic search over past runs.

Stores run learnings as embeddings in SQLite so the Queen can ask:
  "Find runs similar to: build a REST API with auth"
  "What team composition worked best for code review tasks?"
  "Which agent was most reliable for frontend work?"

Usage:
  python3 vector_memory.py store <run-id> <skill-dir>
  python3 vector_memory.py search "<query>" <skill-dir> [--top=5]
  python3 vector_memory.py stats <skill-dir>
"""

import sys
import json
import os
import sqlite3
import math
import hashlib
import re
from collections import Counter
from pathlib import Path
from datetime import datetime

MAX_VOCAB_SIZE = 2000

# ── Embedding backend ──────────────────────────────────────────────────────

def _openai_embed(texts: list[str], api_key: str) -> list[list[float]]:
    """Get embeddings via OpenAI text-embedding-3-small (1536 dims, cheap)."""
    import httpx
    resp = httpx.post(
        "https://api.openai.com/v1/embeddings",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "text-embedding-3-small", "input": texts},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()["data"]
    return [item["embedding"] for item in data]


def _tfidf_embed(texts: list[str], vocab: dict | None = None) -> tuple[list[list[float]], dict]:
    """
    Fallback: lightweight TF-IDF bag-of-words embedding (no API needed).
    Returns (embeddings, vocab) — pass vocab on subsequent calls to keep dims consistent.
    """
    def tokenize(text):
        return re.findall(r"[a-z0-9]+", text.lower())

    # Build vocab from all texts if not provided, capped to prevent unbounded growth.
    if vocab is None:
        token_freq = Counter(tok for text in texts for tok in tokenize(text))
        top_tokens = [tok for tok, _ in token_freq.most_common(MAX_VOCAB_SIZE)]
        vocab = {tok: i for i, tok in enumerate(sorted(top_tokens))}
    elif len(vocab) > MAX_VOCAB_SIZE:
        # Preserve deterministic dimensions if an old vocab file already grew too large.
        vocab = {tok: i for i, tok in enumerate(sorted(vocab)[:MAX_VOCAB_SIZE])}

    dim = max(len(vocab), 1)
    embeddings = []
    for text in texts:
        tokens = tokenize(text)
        vec = [0.0] * dim
        for tok in tokens:
            if tok in vocab:
                vec[vocab[tok]] += 1.0
        # L2 normalize
        norm = math.sqrt(sum(x * x for x in vec)) or 1.0
        embeddings.append([x / norm for x in vec])

    return embeddings, vocab


def get_embeddings(texts: list[str], skill_dir: Path, expand_vocab: bool = True) -> list[list[float]]:
    """Get embeddings — OpenAI if key available, else TF-IDF fallback."""
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")

    if api_key and api_key.startswith("sk-"):
        try:
            return _openai_embed(texts, api_key)
        except Exception as e:
            print(f"[vector_memory] OpenAI embed failed ({e}), falling back to TF-IDF", file=sys.stderr)

    # TF-IDF fallback — load existing vocab if present
    vocab_path = skill_dir / "memory" / "tfidf_vocab.json"
    vocab = None
    if vocab_path.exists():
        vocab = json.loads(vocab_path.read_text())

    # Always expand vocab with new texts so queries use full vocabulary
    embeddings, new_vocab = _tfidf_embed(texts, vocab)

    if expand_vocab:
        # Save updated vocab (grows over time as more runs are added)
        vocab_path.parent.mkdir(parents=True, exist_ok=True)
        vocab_path.write_text(json.dumps(new_vocab))

    # If vocab expanded, re-embed with consistent dimensions
    if vocab and len(new_vocab) != len(vocab):
        embeddings, _ = _tfidf_embed(texts, new_vocab)

    return embeddings


# ── SQLite store ───────────────────────────────────────────────────────────

def get_db(skill_dir: Path) -> sqlite3.Connection:
    db_path = skill_dir / "memory" / "vector_store.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS run_embeddings (
            run_id      TEXT PRIMARY KEY,
            timestamp   TEXT,
            objective   TEXT,
            summary     TEXT,          -- rich text used for embedding
            team_json   TEXT,          -- JSON list of agent roles
            outcome     TEXT,          -- success/partial/failed
            duration_s  REAL,
            agent_count INTEGER,
            embedding   BLOB,          -- JSON-encoded float list
            embed_dim   INTEGER,
            embed_type  TEXT           -- "openai" or "tfidf"
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS agent_reputation (
            agent_role  TEXT PRIMARY KEY,
            runs_total  INTEGER DEFAULT 0,
            runs_ok     INTEGER DEFAULT 0,
            avg_quality REAL DEFAULT 0.0,
            last_seen   TEXT
        )
    """)
    conn.commit()
    return conn


def cosine_sim(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a)) or 1e-9
    norm_b = math.sqrt(sum(x * x for x in b)) or 1e-9
    return dot / (norm_a * norm_b)


# ── Store a run ────────────────────────────────────────────────────────────

def build_summary(run: dict) -> str:
    """Build rich text summary of a run for embedding."""
    parts = [
        f"Objective: {run.get('objective', '')}",
        f"Status: {run.get('status', '')}",
    ]

    team = run.get("teamComposition") or run.get("completedAgents") or []
    if team:
        parts.append(f"Agents: {', '.join(team)}")

    decisions = run.get("decisions", [])
    if decisions:
        parts.append("Decisions: " + "; ".join(
            d.get("msg", d) if isinstance(d, dict) else str(d)
            for d in decisions[:5]
        ))

    # Pull lessons from run-level memory.json if it exists
    lessons = run.get("_lessons", [])
    if lessons:
        parts.append("Lessons: " + "; ".join(lessons[:5]))

    votes = run.get("votes", [])
    if votes:
        parts.append(f"Votes: {len(votes)} decisions made by consensus")

    competitive = run.get("competitiveResults", [])
    if competitive:
        parts.append(f"Competitive spawning: {len(competitive)} competitions")

    return "\n".join(parts)


def store_run(run_id: str, skill_dir: Path):
    """Embed and store a run into the vector store."""
    # Load run.json
    run_path = skill_dir / "runs" / run_id / "run.json"
    if not run_path.exists():
        # Try learnings.json fallback
        learnings_path = skill_dir / "memory" / "learnings.json"
        if not learnings_path.exists():
            print(f"[vector_memory] Run {run_id} not found", file=sys.stderr)
            return False
        learnings = json.loads(learnings_path.read_text())
        runs = [r for r in learnings if r.get("runId") == run_id]
        if not runs:
            print(f"[vector_memory] Run {run_id} not in learnings.json", file=sys.stderr)
            return False
        run = runs[0]
    else:
        run = json.loads(run_path.read_text())

    # Try to enrich with run-level memory.json
    mem_path = skill_dir / "runs" / run_id / "memory.json"
    if mem_path.exists():
        mem = json.loads(mem_path.read_text())
        run["_lessons"] = mem.get("lessons", [])
        run["decisions"] = run.get("decisions", []) + mem.get("decisions", [])

    summary = build_summary(run)
    embeddings = get_embeddings([summary], skill_dir)
    emb = embeddings[0]
    embed_type = "openai" if (os.getenv("OPENAI_API_KEY") or "").startswith("sk-") else "tfidf"

    team = run.get("teamComposition") or run.get("completedAgents") or []
    outcome = run.get("status", "unknown")
    created_at = run.get("createdAt", run.get("timestamp", datetime.utcnow().isoformat()))
    completed_at = run.get("completedAt")
    duration_s = None
    if created_at and completed_at:
        try:
            t0 = datetime.fromisoformat(created_at.rstrip("Z"))
            t1 = datetime.fromisoformat(completed_at.rstrip("Z"))
            duration_s = (t1 - t0).total_seconds()
        except Exception:
            pass

    conn = get_db(skill_dir)
    conn.execute("""
        INSERT OR REPLACE INTO run_embeddings
        (run_id, timestamp, objective, summary, team_json, outcome,
         duration_s, agent_count, embedding, embed_dim, embed_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        run.get("runId", run_id),
        created_at,
        run.get("objective", ""),
        summary,
        json.dumps(team),
        outcome,
        duration_s,
        len(team),
        json.dumps(emb),
        len(emb),
        embed_type,
    ))

    # Update agent reputation
    for agent in team:
        role = agent.split("-")[0] if "-" in agent else agent
        conn.execute("""
            INSERT INTO agent_reputation (agent_role, runs_total, runs_ok, last_seen)
            VALUES (?, 1, ?, ?)
            ON CONFLICT(agent_role) DO UPDATE SET
                runs_total = runs_total + 1,
                runs_ok = runs_ok + (CASE WHEN ? = 'completed' OR ? = 'success' THEN 1 ELSE 0 END),
                last_seen = ?
        """, (role, 1 if outcome in ("completed", "success") else 0, created_at,
              outcome, outcome, created_at))

    conn.commit()
    conn.close()

    print(f"[vector_memory] Stored run {run.get('runId', run_id)} ({embed_type}, dim={len(emb)})")
    return True


# ── Search ─────────────────────────────────────────────────────────────────

def search(query: str, skill_dir: Path, top_k: int = 5) -> list[dict]:
    """Semantic search over stored runs. Returns top_k most similar."""
    conn = get_db(skill_dir)
    rows = conn.execute(
        "SELECT run_id, objective, summary, team_json, outcome, duration_s, agent_count, embedding FROM run_embeddings"
    ).fetchall()
    conn.close()

    if not rows:
        return []

    # Embed the query
    query_emb = get_embeddings([query], skill_dir)[0]

    results = []
    for run_id, objective, summary, team_json, outcome, duration_s, agent_count, emb_blob in rows:
        emb = json.loads(emb_blob)
        # Pad/truncate if dims differ (e.g. tfidf vocab grew)
        if len(emb) != len(query_emb):
            min_dim = min(len(emb), len(query_emb))
            emb = emb[:min_dim]
            q = query_emb[:min_dim]
        else:
            q = query_emb
        sim = cosine_sim(q, emb)
        results.append({
            "run_id": run_id,
            "objective": objective,
            "outcome": outcome,
            "team": json.loads(team_json or "[]"),
            "agent_count": agent_count,
            "duration_s": duration_s,
            "similarity": round(sim, 4),
        })

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]


# ── Stats ──────────────────────────────────────────────────────────────────

def stats(skill_dir: Path) -> dict:
    conn = get_db(skill_dir)
    total = conn.execute("SELECT COUNT(*) FROM run_embeddings").fetchone()[0]
    outcomes = conn.execute(
        "SELECT outcome, COUNT(*) FROM run_embeddings GROUP BY outcome"
    ).fetchall()
    top_agents = conn.execute(
        "SELECT agent_role, runs_total, runs_ok, avg_quality FROM agent_reputation ORDER BY runs_ok DESC LIMIT 10"
    ).fetchall()
    conn.close()

    return {
        "total_runs": total,
        "outcomes": {o: c for o, c in outcomes},
        "top_agents": [
            {"role": r, "total": t, "ok": o, "quality": q}
            for r, t, o, q in top_agents
        ],
    }


# ── Migrate existing learnings.json → vector store ─────────────────────────

def migrate(skill_dir: Path):
    """One-time migration: import all learnings.json entries into vector store."""
    learnings_path = skill_dir / "memory" / "learnings.json"
    if not learnings_path.exists():
        print("[vector_memory] No learnings.json to migrate")
        return

    learnings = json.loads(learnings_path.read_text())
    print(f"[vector_memory] Migrating {len(learnings)} runs...")

    for run in learnings:
        run_id = run.get("runId", "unknown")
        summary = build_summary(run)
        embeddings = get_embeddings([summary], skill_dir)
        emb = embeddings[0]
        embed_type = "openai" if (os.getenv("OPENAI_API_KEY") or "").startswith("sk-") else "tfidf"

        team = run.get("teamComposition") or run.get("completedAgents") or []

        conn = get_db(skill_dir)
        conn.execute("""
            INSERT OR REPLACE INTO run_embeddings
            (run_id, timestamp, objective, summary, team_json, outcome,
             duration_s, agent_count, embedding, embed_dim, embed_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            run_id,
            run.get("timestamp", run.get("createdAt", "")),
            run.get("objective", ""),
            summary,
            json.dumps(team),
            run.get("status", "unknown"),
            None,
            len(team),
            json.dumps(emb),
            len(emb),
            embed_type,
        ))
        conn.commit()
        conn.close()
        print(f"  ✅ {run_id}: {run.get('objective', '')[:60]}")

    print(f"[vector_memory] Migration complete — {len(learnings)} runs indexed")


# ── CLI ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    skill_dir = Path(sys.argv[-1]).expanduser().resolve()

    if cmd == "store":
        run_id = sys.argv[2]
        ok = store_run(run_id, skill_dir)
        sys.exit(0 if ok else 1)

    elif cmd == "search":
        query = sys.argv[2]
        top_k = 5
        for arg in sys.argv:
            if arg.startswith("--top="):
                top_k = int(arg.split("=")[1])
        results = search(query, skill_dir, top_k)
        print(json.dumps(results, indent=2))

    elif cmd == "stats":
        s = stats(skill_dir)
        print(json.dumps(s, indent=2))

    elif cmd == "migrate":
        migrate(skill_dir)

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
