---
name: samurai
description: >
  SAMURAI — Sam's Autonomous Multi-agent Unified Runtime for AI.
  Dynamic multi-agent orchestration with a Queen agent that analyzes tasks,
  spawns the exact agents needed, and coordinates them as a collaborative swarm.
  Agents communicate with each other, vote on disagreements, self-heal on failures,
  and learn from every run. Use when: complex multi-step tasks, building software,
  research projects, content creation, code reviews, anything that benefits from
  multiple specialized agents working together. Invoke with $samurai or keywords
  like swarm, orchestrate, multi-agent, spawn agents, agent team, samurai, queen.
---

# SAMURAI — Sam's Autonomous Multi-agent Unified Runtime for AI 🗡️

## Overview

SAMURAI is a dynamic multi-agent orchestration system. Instead of predefined agents, a **Queen agent** analyzes each task, decides the optimal team composition, spawns agents dynamically, and coordinates their collaboration. Agents communicate freely with each other, not just back to Queen.

## Core Architecture

```
User Task → Queen Agent → Dynamic Team → Collaborative Execution → Result
```

The Queen:
1. Analyzes task complexity and requirements
2. Decides how many agents and what roles (2 to 50+)
3. Spawns them with custom instructions via `sessions_spawn()`
4. Agents collaborate via `sessions_send()` + shared workspace
5. Queen synthesizes final deliverable

## Activation

When the user's request matches this skill (complex task, multi-step work, explicit "samurai" or "swarm" mention), read this file and follow the protocol below.

---

## Step 1: Create a Run

```bash
python3 SKILL_DIR/scripts/orchestrate.py create "<objective>"
```

This creates a run directory at `SKILL_DIR/runs/<run-id>/` with:
- `run.json` — Run metadata, status, agent roster
- `bus/` — Topic-based message channels (see Topic Channels below)
- `memory.json` — Run-level shared memory
- `blackboard.json` — Shared key-value state for all agents
- `reputation.json` — Agent reliability scores (Queen-managed)
- `outputs/` — Each agent writes their deliverables here

### Run Lifecycle Commands
```bash
# Track agents as you spawn them
python3 SKILL_DIR/scripts/orchestrate.py roster <run-id> '{"role":"coder-1","model":"sonnet","label":"samurai-xxx-coder-1","task":"..."}'

# Mark run complete when done
python3 SKILL_DIR/scripts/orchestrate.py complete <run-id>

# Record learnings for future runs
python3 SKILL_DIR/scripts/orchestrate.py learn <run-id>
```

**IMPORTANT:** Call `roster` after EVERY spawn so agent data gets tracked for learning/reputation.

## Step 2: Queen Analysis (YOU are the Queen)

Read `SKILL_DIR/references/queen-prompt.md` for full instructions. In summary:

### Analyze the Task
- What is the objective?
- What specialized roles are needed?
- How many agents? (right-size: don't over-spawn)
- What are the dependencies between tasks?
- Are there decision points requiring human input?
- Does the task need a hierarchy (leads + sub-agents)?

### Decide Model Tiers (Feature: Model Tiering 💰)
Assign the right model to each agent based on task complexity:

| Complexity | Model | Use For |
|-----------|-------|---------|
| Low | `anthropic/claude-haiku` | File writing, formatting, simple transforms |
| Medium | `anthropic/claude-sonnet-4-20250514` | Code writing, reviews, research |
| High | `anthropic/claude-opus-4-6` | Architecture, complex reasoning, critical decisions |

This saves 60-70% on tokens. Don't use Opus for a file rename.

### Decide Execution Strategy
- **Parallel**: Independent tasks that don't depend on each other
- **Sequential**: Tasks with dependencies (reviewer needs code first)
- **Competitive**: For critical tasks, spawn 2 agents with different approaches (Feature: Competitive Spawning 🏆)
- **Pipeline**: Chain multiple phases (Feature: Pipeline Chaining 🔗)
- **Hierarchical**: Lead agents manage sub-agents for large teams (Feature: Agent Hierarchy 🏗️)

## Step 3: Context Injection (Pre-Spawn)

Before spawning, prepare user context for workers:

1. **Read `USER.md`** from workspace root → create compact ~200 token brief (name, style, preferences)
2. **Read `SKILL_DIR/memory/preferences.json`** → extract section relevant to each agent's role:
   - Coder → `preferences.code`
   - Writer → `preferences.writing`
   - Designer → `preferences.design`
3. **Inject both** into each agent's spawn prompt BEFORE their task instructions

This ensures workers produce output aligned with the user's style — not generic AI output.
Cost: ~300-500 extra tokens per worker. Worth it.

## Step 4: Spawn Agents

For each agent, use `sessions_spawn()`:

```
sessions_spawn(
  task: "<USER_BRIEF>\n<RELEVANT_PREFERENCES>\n<WORKER_PROMPT>\n\n<AGENT_SPECIFIC_INSTRUCTIONS>",
  label: "samurai-<run-id>-<role>",
  mode: "run",
  model: "<appropriate-model-tier>"
)
```

**Injection templates** (paste into every agent's task prompt):
- `SKILL_DIR/references/worker-inject.md` — Compact worker rules (~600 tokens). **USE THIS, not the full worker-prompt.md.**
- `SKILL_DIR/references/reviewer-inject.md` — Reviewer rules with LLM-as-Judge rubric.

Read the appropriate inject template, replace `{RUN_ID}`, `{ROLE}`, `{WORKSPACE}` variables, and paste it at the TOP of each agent's task instructions.

**Full reference docs** (for Queen's understanding, NOT injected into agents):
- `SKILL_DIR/references/queen-prompt.md` — Full Queen decomposition logic
- `SKILL_DIR/references/worker-prompt.md` — Detailed worker protocol reference
- `SKILL_DIR/references/communication.md` — Inter-agent communication details
- `SKILL_DIR/references/patterns.md` — Common decomposition patterns

### Competitive Spawning 🏆
For critical deliverables, spawn 2 agents for the same task:
```
samurai-<run-id>-coder-A   (approach 1)
samurai-<run-id>-coder-B   (approach 2)
```
When both complete, Queen evaluates both outputs and picks the better one.

## Step 5: Monitor & Coordinate (Feature: Auto-Healing 🔄)

### Auto-Healing 🔄
Monitor for agent failures. If an agent dies or times out:
1. Read what the agent accomplished (check shared workspace)
2. Spawn a replacement with that context included
3. Continue the run seamlessly

### Human Checkpoints ✋
At critical decision points, PAUSE and ask the user:
```
"🗡️ SAMURAI Checkpoint — Run #<id>
The architect proposed 2 approaches:
A) <option A>
B) <option B>
Which should the team build?"
```
Wait for user response → relay decision to relevant agents via `sessions_send()`.

### Agent Voting 🗳️
When agents disagree:
1. Collect each agent's position (via bus channels or sessions_send)
2. Present positions to all voting agents
3. Majority wins; Queen breaks ties
4. Record the decision in `memory.json` and `bus/decisions.jsonl`

### Dead Letter Handling 📭
If an agent can't reach a teammate:
1. Message goes to `bus/urgent.jsonl`
2. Queen detects undeliverable messages
3. Queen reroutes, respawns, or reassigns as needed
4. No message silently dropped

### Reputation Tracking ⭐
Queen maintains `reputation.json` — scores for each agent based on:
- Task completion (success/failure)
- Code quality (review feedback)
- Communication quality
- Speed of delivery

Used internally by Queen for future spawning decisions. Transparent to workers.

## Step 6: Integration Review (Feature: Integration Review 🔍)

If the run used 2+ agents producing the same output type (code, content):

1. **Read ALL outputs together** — check naming consistency, import/export compatibility, shared patterns
2. **Compare against style contract** — does everything follow the agreed conventions?
3. **Fix inconsistencies** yourself (small teams) or spawn an Integration Reviewer agent (Opus, large teams)
4. Write cleaned output to `outputs/integrated/`

**Never skip this when multiple agents wrote code.** This prevents Frankenstein assemblies.

## Step 7: Collect & Synthesize

When agents complete:
1. Read all outputs from `runs/<run-id>/outputs/`
2. Read the bus channels for final communications
3. Read `blackboard.json` for shared state
4. If competitive spawning was used, compare and select the winner
5. Synthesize everything into a single coherent deliverable
6. Present to the user

## Step 8: Learn (Feature: Self-Learning Memory 🧠)

After every run, update the learning memory:

```bash
python3 SKILL_DIR/scripts/orchestrate.py learn <run-id>
```

This records in `SKILL_DIR/memory/learnings.json`:
- Task type and complexity
- Team composition used (how many, what roles)
- What worked well / what didn't
- Time taken, model costs
- Which competitive approach won (if applicable)
- Voting outcomes and reasoning
- Agent reputation updates

Next time a similar task comes in, Queen reads past learnings to make better decisions.

## Step 9: Run Replay & Fork (Feature: Replay & Fork 🔀)

### Replay
```bash
python3 SKILL_DIR/scripts/orchestrate.py replay <run-id> "<updated-objective>"
```
Loads the previous run's team composition and adapts it for the new objective.

### Fork
```bash
python3 SKILL_DIR/scripts/orchestrate.py fork <run-id> "<modification>"
```
Copies a previous run's outputs as starting context, then spawns agents to modify.

---

## Topic Channels 📢

Messages are organized into **topic channels** under `bus/` instead of one `bus.jsonl`:

| Channel | Purpose | Mandatory |
|---------|---------|-----------|
| `bus/general.jsonl` | Progress updates, done messages | All agents |
| `bus/decisions.jsonl` | Architectural decisions, tech choices | ✅ All agents |
| `bus/urgent.jsonl` | Blockers, security issues, critical alerts | ✅ All agents |
| `bus/reviews.jsonl` | Code review feedback and approvals | Coders + Reviewers |
| `bus/<role>.jsonl` | Messages targeted at a specific role | That role |

Agents post to the **appropriate channel** — decisions go in `decisions`, blockers in `urgent`, etc. Every agent must read `decisions` and `urgent`.

---

## Agent Hierarchy 🏗️

For large teams (8+ agents), Queen can assign **lead agents** who manage sub-teams:

```
Queen
├── frontend-lead
│   ├── coder-ui-1
│   └── coder-ui-2
├── backend-lead
│   ├── coder-api
│   └── coder-db
└── reviewer
```

- **Leads** spawn and manage sub-agents, aggregate outputs, report to Queen
- **Sub-agents** report to their lead, not directly to Queen
- Reduces Queen's coordination overhead for large swarms

---

## Review Loops 🔄

Reviewers and coders iterate until code is approved:

1. Coder writes code → posts `ready` to `bus/reviews.jsonl`
2. Reviewer reviews → posts `feedback` with specific issues
3. Coder fixes → resubmits
4. Repeat until reviewer posts `approved`
5. **Max 3 rounds** — escalate to Queen if unresolved

---

## Shared Blackboard 📋

`blackboard.json` is a shared key-value store for the run:

```json
{
  "coder-1": { "endpoints": ["/api/users"], "port": 3000 },
  "coder-2": { "endpoints": ["/api/products"], "port": 3001 }
}
```

- Agents publish facts other agents need (endpoints, ports, env vars, schemas)
- **Always read before writing** — don't clobber entries
- Each agent writes under their own role key

---

## Request/Response Protocol 📨

For structured questions needing specific answers:

```jsonl
{"ts":"<ISO>","from":"coder-1","to":"architect","type":"request","priority":"high","msg":"What auth strategy?","request_id":"req-coder1-001","deadline":"<ISO>"}
{"ts":"<ISO>","from":"architect","to":"coder-1","type":"response","priority":"normal","msg":"Use JWT with refresh tokens","request_id":"req-coder1-001"}
```

Include `request_id` for matching and `deadline` for urgency. No response by deadline → escalate.

---

## Context Sharing 📤

When an agent finishes major work, they post a `context_share` summary:

```jsonl
{"ts":"<ISO>","from":"coder-1","to":"all","type":"context_share","msg":"Built 5 API endpoints. Auth middleware at middleware/auth.ts. Schema in outputs/coder-1/schema.sql"}
```

Saves downstream agents from reading entire output directories.

---

## Dynamic Role Switching 🔀

Queen can reassign agents mid-run if priorities shift:

```jsonl
{"ts":"<ISO>","from":"queen","to":"coder-2","type":"role_switch","msg":"Switch to tester. Write integration tests for the API."}
```

Agent accepts new role, creates new output directory, continues working.

---

## Priority System ⚡

All bus messages include a priority level:

| Priority | Use |
|----------|-----|
| `critical` | Genuine blockers, security issues only |
| `high` | Important, needs attention soon |
| `normal` | Default for standard communication |
| `low` | FYI, minor suggestions |

---

## Pipeline Chaining 🔗

For multi-phase projects, define a pipeline:

```
Phase 1: Research → output: research.md
    ↓ feeds into
Phase 2: Design → output: design.md
    ↓ feeds into
Phase 3: Build → output: /dist/
    ↓ feeds into
Phase 4: Test → output: test-results.md
```

Queen manages phase transitions automatically. Each phase's output becomes the next phase's input context.

To define a pipeline, Queen writes `runs/<run-id>/pipeline.json`:
```json
{
  "phases": [
    { "id": "research", "objective": "...", "dependsOn": [] },
    { "id": "design", "objective": "...", "dependsOn": ["research"] },
    { "id": "build", "objective": "...", "dependsOn": ["design"] },
    { "id": "test", "objective": "...", "dependsOn": ["build"] }
  ]
}
```

---

## Skill Inheritance 🧬

Spawned agents can use ANY installed OpenClaw skill. When spawning, include skill instructions:

```
"You have access to the following skills:
- web_search / web_fetch — for research
- content-engine — for content creation
- code-reviewer — for code quality
- test-generator — for writing tests
Use them as needed for your task."
```

The Queen decides which skills each agent needs based on their role.

---

## Communication Protocol Summary

### Direct Messaging
Agents use `sessions_send(label, message)` for urgent/targeted communication.

### Topic Channels
All agents read/write to `runs/<run-id>/bus/`:
- `bus/general.jsonl` — General updates and completions
- `bus/decisions.jsonl` — Decisions (mandatory read)
- `bus/urgent.jsonl` — Blockers and critical issues (mandatory read)
- `bus/reviews.jsonl` — Review feedback and approvals
- `bus/<role>.jsonl` — Role-specific messages

### Shared State
- `blackboard.json` — Key-value store for shared facts (endpoints, ports, env vars)
- `memory.json` — Decisions and established facts
- `reputation.json` — Agent reliability scores (Queen-managed)

### Message Bus Format
```jsonl
{"ts":"2026-03-16T12:00:00Z","from":"architect","to":"all","type":"decision","priority":"normal","msg":"Using Next.js + Tailwind"}
{"ts":"2026-03-16T12:01:00Z","from":"coder-1","to":"reviewer","type":"ready","priority":"normal","msg":"API routes complete, see outputs/coder-1/"}
{"ts":"2026-03-16T12:02:00Z","from":"reviewer","to":"coder-1","type":"feedback","priority":"high","msg":"Found 3 issues, see outputs/reviewer/feedback.md"}
{"ts":"2026-03-16T12:05:00Z","from":"coder-1","to":"all","type":"context_share","priority":"normal","msg":"API done: 5 endpoints, JWT auth, schema at outputs/coder-1/schema.sql"}
```

---

## File Structure

```
skills/samurai/
├── SKILL.md                          ← This file
├── references/
│   ├── worker-inject.md              ← COMPACT worker template (~600 tokens) — INJECT THIS
│   ├── reviewer-inject.md            ← COMPACT reviewer template with rubric — INJECT THIS
│   ├── queen-prompt.md               ← Full Queen decomposition logic (reference)
│   ├── worker-prompt.md              ← Detailed worker protocol (reference)
│   ├── communication.md              ← Inter-agent communication details (reference)
│   └── patterns.md                   ← Common decomposition patterns (reference)
├── scripts/
│   └── orchestrate.py                ← Run management CLI (create/status/roster/complete/learn/fork/replay/bus/cleanup)
├── memory/
│   ├── learnings.json                ← Self-learning data (grows over time)
│   ├── preferences.json              ← User coding/writing/design preferences
│   └── reputation.json               ← Model+role performance tracking
└── runs/                             ← Run directories (created dynamically)
    └── <run-id>/
        ├── run.json                   ← Metadata + agent roster + timestamps
        ├── bus/                       ← Topic-based message channels
        │   ├── general.jsonl
        │   ├── decisions.jsonl
        │   ├── urgent.jsonl
        │   ├── reviews.jsonl
        │   └── <role>.jsonl
        ├── memory.json
        ├── blackboard.json            ← Shared key-value state
        ├── style-contract.md          ← Coding/writing conventions (Queen fills)
        ├── pipeline.json (optional)
        └── outputs/
```

---

## Quick Reference

| Feature | How It Works |
|---------|-------------|
| 🐝 Dynamic Spawning | Queen creates agents on-the-fly, no predefined list |
| 🗡️ Inter-Agent Comms | `sessions_send()` + topic channels + blackboard |
| 🧠 Self-Learning | Every run saves learnings; Queen gets smarter over time |
| 🏆 Competitive Spawning | 2 agents, same task, best result wins |
| 🔄 Auto-Healing | Failed agent → Queen spawns replacement with context |
| 💰 Model Tiering | Haiku for simple, Sonnet for medium, Opus for complex |
| ✋ Human Checkpoints | Queen pauses at key decisions, asks user |
| 🗳️ Agent Voting | Disagreements resolved by majority vote |
| 🔗 Pipeline Chaining | Multi-phase workflows, output feeds into next phase |
| 🧬 Skill Inheritance | Agents use any installed OpenClaw skill |
| 🔀 Replay & Fork | Reuse or modify past runs |
| 📢 Topic Channels | Organized `bus/` directory instead of single bus.jsonl |
| 🏗️ Agent Hierarchy | Lead agents manage sub-teams for large swarms |
| 🔄 Review Loops | Reviewer↔Coder iterate up to 3 rounds until approved |
| 📋 Shared Blackboard | `blackboard.json` key-value store for shared state |
| 📨 Request/Response | Structured requests with IDs and deadlines |
| ⚡ Priority Levels | critical/high/normal/low on all bus messages |
| 📭 Dead Letters | Queen reroutes undeliverable messages |
| 📤 Context Sharing | Agents post summaries after major work |
| ⭐ Reputation | Queen tracks agent reliability for future runs |
| 🔀 Dynamic Role Switch | Queen can reassign agents mid-run |
| 👤 Context Injection | Workers know user's preferences and style |
| 📏 Style Contract | Shared coding/writing conventions for multi-agent consistency |
| 🔍 Integration Review | Mandatory consistency check before delivery |
| ⚠️ Anti-Pattern Detection | Queen knows when NOT to swarm |
| 🧠 Reflexion | Agents self-critique output before delivery — catches 15-30% more issues |
| 📊 LLM-as-Judge | Structured scoring rubrics (1-10) replace vague approve/reject reviews |
| 🔬 Multi-Specialist Review | Review squad (bug hunter, security auditor, quality, tests, contracts) for critical code |
