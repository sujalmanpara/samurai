#!/usr/bin/env python3
"""
SAMURAI Orchestrator — Run Management CLI

Usage:
  python3 orchestrate.py create "objective description"
  python3 orchestrate.py status <run-id>
  python3 orchestrate.py list
  python3 orchestrate.py complete <run-id>
  python3 orchestrate.py roster <run-id> '{"role":"coder-1","model":"sonnet","label":"samurai-xxx-coder-1","task":"..."}'
  python3 orchestrate.py learn <run-id>
  python3 orchestrate.py replay <run-id> "new objective"
  python3 orchestrate.py fork <run-id> "modification"
  python3 orchestrate.py cleanup [--older-than 7d]
  python3 orchestrate.py bus <run-id> [--tail 20]
"""

import sys
import os
import json
import uuid
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Resolve paths relative to skill directory
SKILL_DIR = Path(__file__).resolve().parent.parent
RUNS_DIR = SKILL_DIR / "runs"
MEMORY_DIR = SKILL_DIR / "memory"
LEARNINGS_FILE = MEMORY_DIR / "learnings.json"


PREFERENCES_FILE = MEMORY_DIR / "preferences.json"
REPUTATION_FILE = MEMORY_DIR / "reputation.json"


def ensure_dirs():
    """Create required directories."""
    RUNS_DIR.mkdir(exist_ok=True)
    MEMORY_DIR.mkdir(exist_ok=True)
    if not LEARNINGS_FILE.exists():
        LEARNINGS_FILE.write_text("[]")
    if not PREFERENCES_FILE.exists():
        PREFERENCES_FILE.write_text(json.dumps({
            "code": {},
            "writing": {},
            "design": {}
        }, indent=2))
    if not REPUTATION_FILE.exists():
        REPUTATION_FILE.write_text("{}")


def generate_run_id():
    """Generate a short, readable run ID."""
    ts = datetime.now(timezone.utc).strftime("%m%d-%H%M")
    short_uuid = uuid.uuid4().hex[:4]
    return f"{ts}-{short_uuid}"


def cmd_create(objective):
    """Create a new run directory with initial metadata."""
    ensure_dirs()
    run_id = generate_run_id()
    run_dir = RUNS_DIR / run_id

    run_dir.mkdir()
    (run_dir / "outputs").mkdir()
    (run_dir / "bus").mkdir()

    # Initialize run metadata
    run_meta = {
        "runId": run_id,
        "objective": objective,
        "status": "created",
        "createdAt": datetime.now(timezone.utc).isoformat() + "Z",
        "agents": [],
        "phases": [],
        "competitive": [],
        "checkpoints": [],
        "healingEvents": [],
        "reviewLoops": [],
        "roleSwitches": [],
        "completedAt": None,
    }
    (run_dir / "run.json").write_text(json.dumps(run_meta, indent=2))

    # Initialize topic channels
    for channel in ["general.jsonl", "decisions.jsonl", "urgent.jsonl", "dead-letters.jsonl"]:
        (run_dir / "bus" / channel).write_text("")

    # Initialize shared memory
    shared_memory = {
        "facts": {},
        "decisions": [],
        "votes": [],
        "openRequests": [],
    }
    (run_dir / "memory.json").write_text(json.dumps(shared_memory, indent=2))

    # Initialize blackboard
    blackboard = {
        "api_endpoints": [],
        "environment_vars": [],
        "open_questions": [],
        "design_decisions": [],
        "dependencies": [],
    }
    (run_dir / "blackboard.json").write_text(json.dumps(blackboard, indent=2))

    # Create empty style contract (Queen fills this before spawning coders)
    (run_dir / "style-contract.md").write_text("# Style Contract\n\n_Queen: Fill this before spawning 2+ coders/writers._\n")

    print(json.dumps({
        "status": "created",
        "runId": run_id,
        "path": str(run_dir),
        "objective": objective,
    }, indent=2))
    return run_id


def cmd_status(run_id):
    """Show status of a run."""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    run_meta = json.loads((run_dir / "run.json").read_text())

    # Count bus messages across all topic channels
    bus_dir = run_dir / "bus"
    bus_count = 0
    channel_stats = {}
    if bus_dir.exists() and bus_dir.is_dir():
        for channel_file in bus_dir.iterdir():
            if channel_file.suffix == '.jsonl' and channel_file.stat().st_size > 0:
                lines = channel_file.read_text().strip().split("\n")
                lines = [l for l in lines if l.strip()]
                channel_stats[channel_file.stem] = len(lines)
                bus_count += len(lines)
    # Legacy single bus.jsonl support
    elif (run_dir / "bus.jsonl").exists():
        bus_file = run_dir / "bus.jsonl"
        if bus_file.stat().st_size > 0:
            lines = bus_file.read_text().strip().split("\n")
            bus_count = len([l for l in lines if l.strip()])

    # Count output files
    outputs_dir = run_dir / "outputs"
    output_dirs = [d.name for d in outputs_dir.iterdir() if d.is_dir()] if outputs_dir.exists() else []

    # Read all bus messages for agent status
    all_bus_lines = []
    if bus_dir.exists() and bus_dir.is_dir():
        for channel_file in bus_dir.iterdir():
            if channel_file.suffix == '.jsonl' and channel_file.stat().st_size > 0:
                for line in channel_file.read_text().strip().split("\n"):
                    if line.strip():
                        try:
                            all_bus_lines.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass

    done_msgs = [m for m in all_bus_lines if m.get("type") == "done"]
    error_msgs = [m for m in all_bus_lines if m.get("type") == "error"]
    dead_letters = []
    dl_file = bus_dir / "dead-letters.jsonl" if bus_dir.exists() else None
    if dl_file and dl_file.exists() and dl_file.stat().st_size > 0:
        for line in dl_file.read_text().strip().split("\n"):
            if line.strip():
                try:
                    dead_letters.append(json.loads(line))
                except json.JSONDecodeError:
                    pass

    # Blackboard status
    bb_file = run_dir / "blackboard.json"
    blackboard_entries = 0
    if bb_file.exists():
        try:
            bb = json.loads(bb_file.read_text())
            blackboard_entries = sum(len(v) for v in bb.values() if isinstance(v, list))
        except json.JSONDecodeError:
            pass

    status = {
        **run_meta,
        "busMessages": bus_count,
        "channelStats": channel_stats,
        "outputDirectories": output_dirs,
        "completedAgents": [m["from"] for m in done_msgs],
        "failedAgents": [m["from"] for m in error_msgs],
        "deadLetters": len(dead_letters),
        "blackboardEntries": blackboard_entries,
    }

    print(json.dumps(status, indent=2))


def cmd_list():
    """List all runs."""
    ensure_dirs()
    runs = []
    for run_dir in sorted(RUNS_DIR.iterdir(), reverse=True):
        if not run_dir.is_dir():
            continue
        meta_file = run_dir / "run.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            runs.append({
                "runId": meta["runId"],
                "objective": meta["objective"][:80],
                "status": meta["status"],
                "createdAt": meta["createdAt"],
                "agents": len(meta.get("agents", [])),
            })

    print(json.dumps({"runs": runs, "total": len(runs)}, indent=2))


def cmd_learn(run_id):
    """Extract learnings from a completed run and save to memory."""
    ensure_dirs()
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    run_meta = json.loads((run_dir / "run.json").read_text())
    memory = json.loads((run_dir / "memory.json").read_text())

    # Read bus for stats (v1.1: topic channels)
    bus_lines = []
    bus_dir = run_dir / "bus"
    if bus_dir.exists() and bus_dir.is_dir():
        for channel_file in bus_dir.iterdir():
            if channel_file.suffix == '.jsonl' and channel_file.stat().st_size > 0:
                for line in channel_file.read_text().strip().split("\n"):
                    if line.strip():
                        try:
                            bus_lines.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass
    # Legacy single bus.jsonl support
    elif (run_dir / "bus.jsonl").exists():
        bus_file = run_dir / "bus.jsonl"
        if bus_file.stat().st_size > 0:
            for line in bus_file.read_text().strip().split("\n"):
                if line.strip():
                    try:
                        bus_lines.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass

    done_agents = [m["from"] for m in bus_lines if m.get("type") == "done"]
    error_agents = [m["from"] for m in bus_lines if m.get("type") == "error"]
    review_loops = [m for m in bus_lines if m.get("type") in ("feedback", "revision", "approved")]
    role_switches = [m for m in bus_lines if m.get("type") == "role_switch"]
    context_shares = [m for m in bus_lines if m.get("type") == "context_share"]
    dead_letters = []
    dl_file = bus_dir / "dead-letters.jsonl" if bus_dir.exists() else None
    if dl_file and dl_file.exists() and dl_file.stat().st_size > 0:
        for line in dl_file.read_text().strip().split("\n"):
            if line.strip():
                try:
                    dead_letters.append(json.loads(line))
                except json.JSONDecodeError:
                    pass

    learning = {
        "runId": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
        "objective": run_meta["objective"],
        "status": run_meta["status"],
        "teamComposition": run_meta.get("agents", []),
        "completedAgents": done_agents,
        "failedAgents": error_agents,
        "competitiveResults": run_meta.get("competitive", []),
        "votes": memory.get("votes", []),
        "healingEvents": run_meta.get("healingEvents", []),
        "reviewLoops": len(review_loops),
        "roleSwitches": len(role_switches),
        "contextShares": len(context_shares),
        "deadLetters": len(dead_letters),
        "decisions": memory.get("decisions", []),
        "busMessages": len(bus_lines),
        "createdAt": run_meta["createdAt"],
        "completedAt": run_meta.get("completedAt"),
    }

    # Update reputation data
    reputation_file = MEMORY_DIR / "reputation.json"
    if not reputation_file.exists():
        reputation_file.write_text("{}")
    try:
        reputation = json.loads(reputation_file.read_text())
        for agent in run_meta.get("agents", []):
            role = agent.get("role", "unknown")
            model = agent.get("model", "unknown")
            key = f"{model}:{role}"
            if key not in reputation:
                reputation[key] = {"runs": 0, "successes": 0, "failures": 0}
            reputation[key]["runs"] += 1
            if role in done_agents:
                reputation[key]["successes"] += 1
            elif role in error_agents:
                reputation[key]["failures"] += 1
        reputation_file.write_text(json.dumps(reputation, indent=2))
    except Exception:
        pass

    # Append to learnings file
    learnings = json.loads(LEARNINGS_FILE.read_text())
    learnings.append(learning)
    LEARNINGS_FILE.write_text(json.dumps(learnings, indent=2))

    print(json.dumps({"status": "learned", "runId": run_id, "totalLearnings": len(learnings)}, indent=2))


def cmd_replay(run_id, new_objective):
    """Create a new run based on a previous run's structure."""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    old_meta = json.loads((run_dir / "run.json").read_text())

    # Create new run
    new_run_id = cmd_create(new_objective)
    new_run_dir = RUNS_DIR / new_run_id

    # Copy team composition as reference
    new_meta = json.loads((new_run_dir / "run.json").read_text())
    new_meta["replayOf"] = run_id
    new_meta["previousTeam"] = old_meta.get("agents", [])
    new_meta["previousObjective"] = old_meta["objective"]
    (new_run_dir / "run.json").write_text(json.dumps(new_meta, indent=2))

    print(json.dumps({
        "status": "replayed",
        "newRunId": new_run_id,
        "basedOn": run_id,
        "previousTeam": old_meta.get("agents", []),
    }, indent=2))


def cmd_fork(run_id, modification):
    """Fork a run — copy outputs as starting context."""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    old_meta = json.loads((run_dir / "run.json").read_text())

    # Create new run
    new_run_id = generate_run_id()
    new_run_dir = RUNS_DIR / new_run_id
    new_run_dir.mkdir()

    # Copy outputs as starting context
    old_outputs = run_dir / "outputs"
    new_context = new_run_dir / "forked-context"
    if old_outputs.exists():
        shutil.copytree(old_outputs, new_context)

    (new_run_dir / "outputs").mkdir()

    # Copy memory (facts/decisions carry over)
    old_memory = run_dir / "memory.json"
    if old_memory.exists():
        shutil.copy2(old_memory, new_run_dir / "memory.json")
    else:
        (new_run_dir / "memory.json").write_text('{"facts":{},"decisions":[],"votes":[],"openRequests":[]}')

    # Initialize bus directory with topic channels
    (new_run_dir / "bus").mkdir()
    for channel in ["general.jsonl", "decisions.jsonl", "urgent.jsonl", "dead-letters.jsonl"]:
        (new_run_dir / "bus" / channel).write_text("")

    # Initialize blackboard
    (new_run_dir / "blackboard.json").write_text(json.dumps({
        "api_endpoints": [], "environment_vars": [], "open_questions": [],
        "design_decisions": [], "dependencies": [],
    }, indent=2))

    # Create empty style contract
    (new_run_dir / "style-contract.md").write_text("# Style Contract\n\n_Queen: Fill this before spawning 2+ coders/writers._\n")

    # Create metadata
    new_meta = {
        "runId": new_run_id,
        "objective": modification,
        "status": "created",
        "createdAt": datetime.now(timezone.utc).isoformat() + "Z",
        "forkedFrom": run_id,
        "previousObjective": old_meta["objective"],
        "agents": [],
        "phases": [],
        "competitive": [],
        "checkpoints": [],
        "healingEvents": [],
        "completedAt": None,
    }
    (new_run_dir / "run.json").write_text(json.dumps(new_meta, indent=2))

    print(json.dumps({
        "status": "forked",
        "newRunId": new_run_id,
        "forkedFrom": run_id,
        "contextCopied": new_context.exists(),
        "modification": modification,
    }, indent=2))


def cmd_bus(run_id, tail=None, channel=None):
    """Show message bus contents (all channels or specific channel)."""
    run_dir = RUNS_DIR / run_id
    bus_dir = run_dir / "bus"

    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    lines = []

    if bus_dir.exists() and bus_dir.is_dir():
        if channel:
            # Specific channel
            ch_file = bus_dir / f"{channel}.jsonl"
            if ch_file.exists() and ch_file.stat().st_size > 0:
                lines = [l for l in ch_file.read_text().strip().split("\n") if l.strip()]
        else:
            # All channels
            for ch_file in sorted(bus_dir.iterdir()):
                if ch_file.suffix == '.jsonl' and ch_file.stat().st_size > 0:
                    for l in ch_file.read_text().strip().split("\n"):
                        if l.strip():
                            lines.append(l)
    # Legacy single bus.jsonl
    elif (run_dir / "bus.jsonl").exists():
        bus_file = run_dir / "bus.jsonl"
        if bus_file.stat().st_size > 0:
            lines = [l for l in bus_file.read_text().strip().split("\n") if l.strip()]

    if tail:
        lines = lines[-int(tail):]

    messages = []
    for line in lines:
        try:
            messages.append(json.loads(line))
        except json.JSONDecodeError:
            pass

    # Sort by timestamp
    messages.sort(key=lambda m: m.get("ts", ""))

    result = {"runId": run_id, "messages": messages, "total": len(messages)}
    if channel:
        result["channel"] = channel
    elif bus_dir.exists():
        result["channels"] = [f.stem for f in bus_dir.iterdir() if f.suffix == '.jsonl']
    print(json.dumps(result, indent=2))


def cmd_complete(run_id):
    """Mark a run as completed and set completedAt timestamp."""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    run_meta = json.loads((run_dir / "run.json").read_text())
    run_meta["status"] = "completed"
    run_meta["completedAt"] = datetime.now(timezone.utc).isoformat() + "Z"
    (run_dir / "run.json").write_text(json.dumps(run_meta, indent=2))

    print(json.dumps({
        "status": "completed",
        "runId": run_id,
        "completedAt": run_meta["completedAt"],
    }, indent=2))


def cmd_roster(run_id, agent_json):
    """Add an agent to the run's roster. agent_json: {"role":"coder-1","model":"sonnet","label":"samurai-xxx-coder-1","task":"Build API"}"""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        print(json.dumps({"error": f"Run {run_id} not found"}))
        sys.exit(1)

    try:
        agent_info = json.loads(agent_json)
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON for agent info"}))
        sys.exit(1)

    agent_info["spawnedAt"] = datetime.now(timezone.utc).isoformat() + "Z"

    run_meta = json.loads((run_dir / "run.json").read_text())
    run_meta["agents"].append(agent_info)
    run_meta["status"] = "running"
    (run_dir / "run.json").write_text(json.dumps(run_meta, indent=2))

    print(json.dumps({
        "status": "agent_added",
        "runId": run_id,
        "agent": agent_info,
        "totalAgents": len(run_meta["agents"]),
    }, indent=2))


def cmd_cleanup(older_than_days=7):
    """Remove old run directories."""
    ensure_dirs()
    cutoff = datetime.now(timezone.utc) - timedelta(days=older_than_days)
    removed = []

    for run_dir in RUNS_DIR.iterdir():
        if not run_dir.is_dir():
            continue
        meta_file = run_dir / "run.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            created = datetime.fromisoformat(meta["createdAt"].replace("Z", ""))
            if created < cutoff:
                shutil.rmtree(run_dir)
                removed.append(meta["runId"])

    print(json.dumps({"status": "cleaned", "removed": removed, "count": len(removed)}, indent=2))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "create" and len(sys.argv) >= 3:
        cmd_create(sys.argv[2])
    elif cmd == "status" and len(sys.argv) >= 3:
        cmd_status(sys.argv[2])
    elif cmd == "list":
        cmd_list()
    elif cmd == "learn" and len(sys.argv) >= 3:
        cmd_learn(sys.argv[2])
    elif cmd == "complete" and len(sys.argv) >= 3:
        cmd_complete(sys.argv[2])
    elif cmd == "roster" and len(sys.argv) >= 4:
        cmd_roster(sys.argv[2], sys.argv[3])
    elif cmd == "replay" and len(sys.argv) >= 4:
        cmd_replay(sys.argv[2], sys.argv[3])
    elif cmd == "fork" and len(sys.argv) >= 4:
        cmd_fork(sys.argv[2], sys.argv[3])
    elif cmd == "bus" and len(sys.argv) >= 3:
        tail = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--tail" else None
        cmd_bus(sys.argv[2], tail)
    elif cmd == "cleanup":
        days = 7
        if "--older-than" in sys.argv:
            idx = sys.argv.index("--older-than")
            if idx + 1 < len(sys.argv):
                val = sys.argv[idx + 1].rstrip("d")
                days = int(val)
        cmd_cleanup(days)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
