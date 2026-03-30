# SAMURAI Inter-Agent Communication Protocol v1.1

## Overview

SAMURAI agents communicate through three core channels plus extended protocols:

### Core Channels
1. **Direct Messages** — `sessions_send()` for targeted, urgent communication
2. **Message Bus** — Topic-based `bus/` directory for broadcast, history, and async coordination
3. **Shared Files** — `outputs/`, `blackboard.json`, and `memory.json` for deliverables and state

### Extended Protocols
4. **Review Loops** 🔄 — Structured feedback cycles between reviewer and coder
5. **Topic Channels** 📡 — Partitioned bus for organized communication
6. **Agent Hierarchy** 🌳 — Lead agents can spawn and manage sub-agents
7. **Request/Response** ❓ — Structured ask-and-answer with deadlines
8. **Shared Blackboard** 📋 — Append-only collaborative state
9. **Priority Levels** 🚨 — 4-tier message urgency system
10. **Dead Letter Queue** 🔁 — No message ever lost
11. **Context Sharing** 🧠 — Compressed briefings between agents
12. **Agent Reputation** 📊 — Performance tracking across runs
13. **Dynamic Role Switching** 🔀 — Reassign idle agents on the fly

---

## Channel Selection

| Scenario | Channel | Why |
|----------|---------|-----|
| "Hey coder, your API has a bug on line 42" | Direct Message | Targeted, urgent |
| "Architecture decision: we're using PostgreSQL" | Bus → `decisions.jsonl` | Everyone needs to know, recorded |
| "Here's the completed frontend code" | Shared Files | Large deliverable |
| "Voting on framework choice" | Bus → `decisions.jsonl` | Needs to be recorded |
| "I'm blocked, need architect's output" | Direct Message | Specific dependency |
| "Run-level fact: API base URL is /v2" | Blackboard | Persistent structured state |
| "Found 3 issues in coder's PR" | Review Loop (bus → topic) | Structured feedback cycle |
| "What auth library are you using?" | Request/Response | Need answer with deadline |
| "Here's a summary of what I've built so far" | Context Share (bus) | Save tokens for downstream |
| "CRITICAL: production DB creds are wrong" | Bus → `urgent.jsonl` (🔴) | Stop everything |
| "FYI: added a loading spinner" | Bus → `general.jsonl` (🟢) | Low priority, informational |
| "Coder-2 is idle, reassign to testing" | Direct Message (role_switch) | Dynamic reallocation |

---

## 1. Direct Messages (sessions_send)

```
sessions_send(label="samurai-<run-id>-<target-role>", message="<content>")
```

**Use for:**
- Urgent requests ("I need your output NOW")
- Specific feedback ("Fix the bug on line 42")
- Dependency notifications ("My part is ready for you")
- Private coordination (doesn't need to be broadcast)
- Role switch commands (Queen → idle agent)

**Conventions:**
- Start with your role: `"[reviewer] Found 3 issues in your code..."`
- Be actionable: include what you need the other agent to do
- Keep it focused: one topic per message
- For sub-agents: message your lead, not Queen directly

---

## 2. Message Bus (Topic Channels) 📡

Instead of a single `bus.jsonl`, SAMURAI uses a **topic-based bus directory** at `runs/<run-id>/bus/`.

### Directory Structure
```
runs/<run-id>/bus/
├── general.jsonl      # Default — progress updates, misc
├── decisions.jsonl    # Architecture decisions, votes, outcomes
├── urgent.jsonl       # Critical issues, blockers, emergencies
├── dead-letters.jsonl # Failed deliveries (see §7)
├── frontend.jsonl     # (Custom) Queen creates per-run topics
├── backend.jsonl      # (Custom) Queen creates per-run topics
└── testing.jsonl      # (Custom) Queen creates per-run topics
```

### Default Topics (always exist)

| Topic | File | Watched By | Purpose |
|-------|------|------------|---------|
| General | `general.jsonl` | Assigned agents | Progress updates, status, misc |
| Decisions | `decisions.jsonl` | **All agents** | Architectural decisions, votes |
| Urgent | `urgent.jsonl` | **All agents** | Blockers, critical errors, emergencies |

### Custom Topics
Queen creates custom topic files during the plan step:
```bash
touch runs/<run-id>/bus/frontend.jsonl
touch runs/<run-id>/bus/backend.jsonl
```

Each agent is told in their system prompt which topics to watch:
```
Watch topics: general, decisions, urgent, frontend
```

**Rules:**
- `decisions.jsonl` and `urgent.jsonl` are **always watched by every agent**
- Custom topics are watched only by assigned agents
- When in doubt, post to `general.jsonl`

### Message Format (all topics)
```jsonl
{"ts":"2026-03-16T12:00:00.000Z","from":"architect","to":"all","type":"decision","priority":"normal","msg":"Tech stack: Next.js 15 + Tailwind + Supabase"}
```

Every message includes:
- `ts` — ISO 8601 UTC timestamp
- `from` — sender role
- `to` — target role or `"all"`
- `type` — message type (see table below)
- `priority` — urgency level (see §6)
- `msg` — content string

### Message Types

| Type | From → To | Purpose |
|------|-----------|---------|
| `update` | any → all | Progress update |
| `ready` | producer → consumer | Output ready for next agent |
| `question` | any → any | Asking for input (informal) |
| `answer` | any → any | Responding to question (informal) |
| `feedback` | reviewer → worker | Review comments (see §4) |
| `revision` | worker → reviewer | Fixed code after feedback (see §4) |
| `approved` | reviewer → worker | Review passed (see §4) |
| `decision` | queen/architect → all | Key decision made |
| `vote` | any → queen | Casting a vote |
| `blocker` | any → queen | Something is blocked |
| `error` | any → queen | Agent encountered an error |
| `done` | any → all | Task completed |
| `heal` | queen → all | Replacement agent spawned |
| `request` | any → any | Formal question with deadline (see §5) |
| `response` | any → any | Formal answer to request (see §5) |
| `context_share` | any → all | Compressed understanding briefing (see §8) |
| `role_switch` | queen → agent | Reassign agent to new role (see §10) |

### Reading the Bus
Agents should read their watched topic files:
- At the start of their work (catch up on context)
- When waiting for a dependency
- Before making a decision (check `decisions.jsonl` first)
- Periodically during long tasks
- **Always** check `urgent.jsonl` before any other topic

### Writing to the Bus
```bash
# Bash — append to a topic
echo '{"ts":"'$(date -u +%Y-%m-%dT%H:%M:%S.000Z)'","from":"coder-1","to":"all","type":"done","priority":"normal","msg":"API routes complete"}' >> runs/<run-id>/bus/general.jsonl
```

---

## 3. Shared Files

### Output Directories
Each agent writes to `runs/<run-id>/outputs/<role>/`:
```
outputs/
├── architect/
│   ├── design.md
│   └── api-schema.json
├── coder-1/
│   ├── src/
│   └── package.json
├── coder-2/
│   ├── frontend/
│   └── styles/
├── reviewer/
│   ├── feedback-coder-1.md
│   └── feedback-coder-2.md
└── tester/
    ├── tests/
    └── coverage-report.md
```

### Shared Memory (memory.json)
Run-level shared state at `runs/<run-id>/memory.json`:
```json
{
  "facts": {
    "tech_stack": "Next.js 15 + Tailwind + Supabase",
    "api_base": "/api/v2"
  },
  "decisions": [
    {
      "topic": "Framework",
      "decision": "Next.js over Remix",
      "decidedBy": "architect",
      "timestamp": "2026-03-16T12:00:00Z",
      "reasoning": "Better SSR support for SEO landing page"
    }
  ],
  "votes": [
    {
      "topic": "Database choice",
      "options": ["Supabase", "PlanetScale", "Neon"],
      "votes": { "Supabase": 3, "PlanetScale": 1 },
      "winner": "Supabase",
      "timestamp": "2026-03-16T12:01:00Z"
    }
  ],
  "open_requests": []
}
```

Any agent can READ memory.json. Only Queen and designated agents should WRITE to it (to avoid conflicts).

---

## 4. Review Loops 🔄

Structured feedback cycles between reviewer and coder. Replaces ad-hoc "fix this" messages with a trackable protocol.

### Flow
```
Reviewer → feedback → Coder → revision → Reviewer → approved (or more feedback)
                                                    ↻ repeat (max 3 rounds)
```

### Protocol

**Round 1 — Reviewer finds issues:**
```jsonl
{"ts":"2026-03-16T12:10:00.000Z","from":"reviewer","to":"coder-1","type":"feedback","priority":"high","msg":"Round 1/3: 3 issues found. See outputs/reviewer/feedback-coder-1-r1.md"}
```

**Coder fixes and resubmits:**
```jsonl
{"ts":"2026-03-16T12:20:00.000Z","from":"coder-1","to":"reviewer","type":"revision","priority":"normal","msg":"Round 1 fixes applied. Updated outputs/coder-1/src/"}
```

**Reviewer approves (or sends more feedback):**
```jsonl
{"ts":"2026-03-16T12:25:00.000Z","from":"reviewer","to":"coder-1","type":"approved","priority":"normal","msg":"All issues resolved. Code approved ✅"}
```

### Rules
- **Max rounds:** Configurable by Queen, default **3**
- If max rounds reached without approval: Queen decides (merge anyway, reassign, or intervene)
- Reviewer writes detailed feedback to `outputs/reviewer/feedback-<target>-r<N>.md`
- Coder references the feedback file, fixes issues, posts `revision`
- Each feedback message includes the round number: `"Round 2/3: ..."`

---

## 5. Request/Response ❓

Structured ask-and-answer protocol with deadlines. For when you need a real answer, not just a bus broadcast.

### Request Message
```jsonl
{"ts":"2026-03-16T12:30:00.000Z","from":"coder-1","to":"architect","type":"request","priority":"high","id":"req-001","msg":"What auth library should I use? JWT or session-based?","deadline":"2026-03-16T12:40:00.000Z"}
```

Fields:
- `id` — Unique request ID (`req-XXX`)
- `deadline` — ISO 8601 timestamp for expected response
- Posted to the relevant topic channel (or `general.jsonl`)

### Response Message
```jsonl
{"ts":"2026-03-16T12:33:00.000Z","from":"architect","to":"coder-1","type":"response","priority":"normal","replyTo":"req-001","msg":"Use next-auth with JWT strategy. See design.md §4 for details."}
```

Fields:
- `replyTo` — References the original request ID

### Timeout Behavior
If no response arrives by the deadline:
1. Agent makes their best judgment and proceeds
2. Posts to `general.jsonl`: `"No response to req-001. Proceeding with JWT."`
3. If truly blocked: escalate to Queen via `urgent.jsonl` with type `blocker`

### Tracking
Open requests are tracked in `memory.json` under `open_requests`:
```json
{
  "open_requests": [
    {"id": "req-001", "from": "coder-1", "to": "architect", "question": "Auth library?", "deadline": "2026-03-16T12:40:00Z", "status": "pending"}
  ]
}
```

---

## 6. Priority Levels 🚨

Every bus message includes a `priority` field. Four levels:

| Level | Emoji | Value | Meaning | Action Required |
|-------|-------|-------|---------|-----------------|
| Critical | 🔴 | `"critical"` | Stop everything, read now | Immediate. Drop current work. |
| High | 🟠 | `"high"` | Blocking dependency | Read ASAP. Someone is waiting on you. |
| Normal | 🟡 | `"normal"` | Standard updates | Read during regular bus checks. Default level. |
| Low | 🟢 | `"low"` | FYI, cosmetic | Read when convenient. No rush. |

### Examples
```jsonl
{"ts":"...","from":"tester","to":"all","type":"error","priority":"critical","msg":"Production DB credentials are exposed in committed code!"}
{"ts":"...","from":"coder-1","to":"reviewer","type":"ready","priority":"high","msg":"API routes ready for review. Blocking frontend work."}
{"ts":"...","from":"coder-2","to":"all","type":"update","priority":"normal","msg":"Navbar component done, starting footer."}
{"ts":"...","from":"reviewer","to":"coder-2","type":"feedback","priority":"low","msg":"Consider renaming 'btn' to 'button' for readability."}
```

### Queen Behavior
- When Queen is busy coordinating: monitors only `urgent.jsonl` and `critical` messages
- During idle checks: scans all topics at all priority levels

---

## 7. Dead Letter Queue 🔁

No message ever lost. When `sessions_send()` fails (target agent crashed, dead, or unresponsive), the message is logged to the dead letter queue.

### File
```
runs/<run-id>/bus/dead-letters.jsonl
```

### Format
```jsonl
{"ts":"2026-03-16T13:00:00.000Z","from":"reviewer","to":"coder-2","type":"feedback","priority":"high","msg":"3 issues found...","error":"sessions_send failed: agent not found","originalTs":"2026-03-16T12:55:00.000Z"}
```

### Protocol
1. Agent tries `sessions_send()` → fails
2. Agent logs the failed message to `bus/dead-letters.jsonl` with the `error` field
3. Agent posts to `urgent.jsonl`: `"[reviewer] Failed to reach coder-2. Message logged to dead-letters."`
4. Queen checks dead letters during coordination sweeps
5. On auto-heal (replacement agent spawned): Queen forwards all undelivered dead letters to the new agent
6. Forwarded messages get marked: `"forwarded": true, "originalFrom": "reviewer"`

### Dead Letter Entry
```jsonl
{"ts":"2026-03-16T13:00:00.000Z","from":"reviewer","to":"coder-2","type":"feedback","priority":"high","msg":"3 issues in API error handling. See outputs/reviewer/feedback-coder-2-r1.md","error":"sessions_send failed: label samurai-001-coder-2 not found","forwarded":false}
```

After Queen forwards to replacement:
```jsonl
{"ts":"2026-03-16T13:05:00.000Z","from":"queen","to":"coder-2-replacement","type":"feedback","priority":"high","msg":"[Forwarded from reviewer] 3 issues in API error handling. See outputs/reviewer/feedback-coder-2-r1.md","forwarded":true,"originalFrom":"reviewer","originalTs":"2026-03-16T13:00:00.000Z"}
```

---

## 8. Context Sharing 🧠

Agents can post compressed summaries of their understanding so downstream agents don't have to dig through raw files. Like a briefing — saves time and tokens.

### Message Format
```jsonl
{"ts":"2026-03-16T12:15:00.000Z","from":"architect","to":"all","type":"context_share","priority":"normal","msg":"Architecture briefing","summary":"We're building a Next.js 15 app with Supabase backend. 3 main API routes: /auth, /posts, /users. Frontend uses Tailwind + shadcn/ui. Auth is JWT via next-auth. DB schema has 4 tables: users, posts, comments, tags.","confidence":0.95,"sources":["outputs/architect/design.md","outputs/architect/api-schema.json"]}
```

Fields:
- `summary` — Compressed text summary of what the agent knows/built
- `confidence` — Float 0-1, how confident the agent is in this summary
- `sources` — Array of file paths supporting the summary

### When to Post Context Shares
- After completing a major phase of work
- When your output will be consumed by multiple agents
- When the raw files are large and a summary would save tokens

### When to Read Context Shares
- Before starting work that depends on another agent's output
- Read the context share first; dig into source files only if needed
- Check `confidence` — if low (<0.7), verify against source files

---

## 9. Shared Blackboard 📋

Structured shared state that any agent can contribute to. Unlike `memory.json` (Queen-controlled), the blackboard is collaborative.

### File
```
runs/<run-id>/blackboard.json
```

### Structure
```json
{
  "api_endpoints": [
    {"path": "/api/auth/login", "method": "POST", "addedBy": "architect", "ts": "2026-03-16T12:00:00Z"},
    {"path": "/api/posts", "method": "GET", "addedBy": "coder-1", "ts": "2026-03-16T12:30:00Z"}
  ],
  "environment_vars": [
    {"key": "DATABASE_URL", "value": "set in .env", "addedBy": "architect", "ts": "2026-03-16T12:00:00Z"},
    {"key": "NEXT_PUBLIC_API_BASE", "value": "/api/v2", "addedBy": "coder-1", "ts": "2026-03-16T12:35:00Z"}
  ],
  "open_questions": [
    {"question": "Should we support dark mode?", "askedBy": "coder-2", "ts": "2026-03-16T12:40:00Z", "resolved": false}
  ],
  "design_decisions": [
    {"decision": "Use server components for data fetching", "madeBy": "architect", "ts": "2026-03-16T12:05:00Z", "reason": "Better performance, less client JS"}
  ],
  "dependencies": [
    {"package": "next-auth", "version": "^5.0", "addedBy": "coder-1", "ts": "2026-03-16T12:20:00Z"},
    {"package": "@supabase/supabase-js", "version": "^2.0", "addedBy": "coder-1", "ts": "2026-03-16T12:20:00Z"}
  ]
}
```

### Rules
- **Read before writing** — always read current state to avoid overwrites
- **Append-only sections** — `api_endpoints`, `environment_vars`, `dependencies` are append-only. Don't remove entries.
- **Attribution required** — every entry includes `addedBy` (role) and `ts`
- **Resolve, don't delete** — mark `open_questions` as `"resolved": true`, don't remove them
- Any agent can read and write to the blackboard
- For conflicting entries: raise on `decisions.jsonl`, let Queen or architect resolve

---

## 10. Agent Hierarchy 🌳

Lead agents can spawn sub-agents for parallel subtasks. Creates a tree structure instead of flat Queen → workers.

### How It Works
1. Queen grants **spawning authority** to a lead agent during the plan step
2. Lead agent uses `sessions_spawn()` to create sub-agents
3. Sub-agents report to their lead, **not directly to Queen**
4. Lead aggregates sub-agent outputs and reports a unified result to Queen

### Label Format
```
samurai-<run-id>-<lead>-<sub>
```

Examples:
- `samurai-001-backend-api` — "api" sub-agent under "backend" lead
- `samurai-001-backend-db` — "db" sub-agent under "backend" lead
- `samurai-001-frontend-components` — "components" sub-agent under "frontend" lead

### Hierarchy Example
```
Queen
├── architect (no sub-agents)
├── backend (lead — spawning authority)
│   ├── samurai-001-backend-api
│   ├── samurai-001-backend-db
│   └── samurai-001-backend-auth
├── frontend (lead — spawning authority)
│   ├── samurai-001-frontend-components
│   └── samurai-001-frontend-pages
├── reviewer (no sub-agents)
└── tester (no sub-agents)
```

### Communication Rules for Hierarchy
- Sub-agents post to their lead's topic channel (e.g., `bus/backend.jsonl`)
- Sub-agents watch: their lead's topic + `decisions.jsonl` + `urgent.jsonl`
- Lead aggregates sub-agent work into `outputs/<lead>/` before telling Queen it's done
- If a sub-agent is blocked: escalate to lead. Lead escalates to Queen only if needed.
- Queen never directly messages sub-agents (goes through lead)

---

## 11. Agent Reputation 📊

Performance tracking across runs. Queen uses reputation data to make smarter model/role assignments.

### File
```
memory/reputation.json
```
(Persists across runs — lives in the skill's memory directory, not inside a run folder.)

### Structure
```json
{
  "entries": [
    {
      "model": "claude-sonnet-4-20250514",
      "role": "coder",
      "runs": 12,
      "successes": 11,
      "failures": 1,
      "avgTimeSeconds": 180,
      "qualityScores": [0.9, 0.85, 0.95, 0.88],
      "avgQuality": 0.895,
      "lastUsed": "2026-03-16T12:00:00Z",
      "notes": "Excellent at backend. Struggles with complex CSS."
    },
    {
      "model": "gemini-2.5-pro",
      "role": "architect",
      "runs": 5,
      "successes": 5,
      "failures": 0,
      "avgTimeSeconds": 120,
      "qualityScores": [0.92, 0.94, 0.90],
      "avgQuality": 0.92,
      "lastUsed": "2026-03-15T18:00:00Z",
      "notes": "Strong system design. Good at breaking down tasks."
    }
  ]
}
```

### How It's Used
- **Before a run:** Queen reads `reputation.json` and assigns models to roles based on past performance
- **After a run:** During the `learn` step, Queen updates entries with results from this run
- **Quality scores:** Based on reviewer feedback, test pass rates, and completion success
- **Failure tracking:** Models that repeatedly fail in a role get deprioritized

---

## 12. Dynamic Role Switching 🔀

Queen can reassign idle agents to new roles instead of spawning new ones. Saves resources.

### Message Format (Direct Message)
```
sessions_send(label="samurai-001-coder-2", message='{"type":"role_switch","newRole":"tester","newTask":"Write integration tests for the API routes in outputs/coder-1/src/api/","newOutputDir":"outputs/tester-2/"}')
```

### Bus Announcement
```jsonl
{"ts":"2026-03-16T13:30:00.000Z","from":"queen","to":"all","type":"role_switch","priority":"normal","msg":"coder-2 reassigned to tester-2. Now handling integration tests."}
```

### Agent Behavior on Role Switch
1. Receive `role_switch` message from Queen
2. Create new output directory: `outputs/<newOutputDir>/`
3. Re-read relevant bus topics and blackboard for new role context
4. Begin working on new task
5. Post to bus: `"[tester-2] (formerly coder-2) Starting integration tests."`

### When to Use
- An agent finished early and is idle
- A role needs more hands (e.g., testing phase needs help)
- An agent's original role is no longer needed
- Queen wants to rebalance workload without spawning cost

---

## Conflict Resolution

### File Conflicts
- Each agent writes to their OWN output directory only
- Never write to another agent's directory
- Blackboard is collaborative but append-only
- Shared state (memory.json) goes through Queen

### Communication Conflicts
- If two agents give contradictory instructions: check `decisions.jsonl` for the latest decision
- If no decision exists: raise it on the bus as a `request` type with a deadline
- If urgent: post to `urgent.jsonl` with `critical` priority

### Timing
- Messages are not guaranteed to be instant
- Always check the bus before assuming another agent hasn't responded
- Use file outputs as the source of truth (bus is for coordination)
- Use request/response with deadlines for time-sensitive needs

---

## Anti-Patterns

❌ Don't message every 10 seconds with "still working..."
❌ Don't write to another agent's output directory
❌ Don't ignore the bus (context drift)
❌ Don't make decisions without checking `decisions.jsonl` first
❌ Don't send huge code blocks via `sessions_send` (use shared files + pointers)
❌ Don't post everything to `urgent.jsonl` — reserve it for real emergencies
❌ Don't skip reading context shares and re-parse raw files (token waste)
❌ Don't let review loops run forever — respect the max rounds limit
❌ Don't message Queen directly if you're a sub-agent (go through your lead)
❌ Don't silently drop failed `sessions_send` — always log to dead letters
❌ Don't overwrite blackboard entries — append only, resolve don't delete

✅ Do write deliverables to files, send pointers via messages
✅ Do read the bus (especially `decisions.jsonl` and `urgent.jsonl`) before starting work
✅ Do announce completion promptly
✅ Do ask for help when stuck (via `request` type with deadline)
✅ Do post context shares after completing major work phases
✅ Do log to dead letters when `sessions_send` fails
✅ Do check blackboard before duplicating shared state
✅ Do include priority on every bus message
✅ Do use review loops for code quality — don't just LGTM everything
✅ Do update reputation data honestly after each run
