# 🗡️ SAMURAI

### Sam's Autonomous Multi-agent Unified Runtime for AI

---

## What is SAMURAI?

SAMURAI is a dynamic multi-agent orchestration system for OpenClaw. Instead of predefined agents, a **Queen agent** analyzes each task, dynamically creates the exact team needed, and coordinates agents that **collaborate with each other** — not just report back to a central controller.

Think of it as spawning an entire AI team on demand. 2 agents for a simple task. 50+ for a massive project. The Queen decides.

---

## How It Works

```
You give a task
      ↓
🐝 Queen Agent analyzes it
      ↓
Queen decides: "This needs a researcher, 2 coders, and a reviewer"
      ↓
Spawns 4 agents dynamically (no predefined list)
      ↓
Agents collaborate with each other:
  Researcher → shares findings with Coders
  Coder-1 ←→ Coder-2 coordinate on frontend/backend
  Reviewer → gives feedback to Coders
      ↓
Queen collects everything → delivers final result
```

**Simple tasks?** Queen handles them directly. Zero agents spawned. No overhead.

**Complex tasks?** Full swarm. Parallel execution. Agents talking to each other. Auto-healing if one fails. Voting if they disagree.

---

## Features

### 🐝 Dynamic Agent Spawning
No predefined agent list. Queen creates whatever agents the task needs — researcher, architect, coder, designer, security auditor, data analyst, copywriter — anything. The team is custom-built for every single task.

### 🗡️ Inter-Agent Communication
Agents don't work in isolation. They talk to each other through three channels:

| Channel | How | Use Case |
|---------|-----|----------|
| **Direct Messages** | `sessions_send()` | "Hey coder, your API has a bug on line 42" |
| **Message Bus** | `bus.jsonl` (shared file) | "Team decision: we're using PostgreSQL" |
| **Shared Workspace** | `outputs/` directory | Code, docs, deliverables |

A coder can message a reviewer. A researcher can share findings with all agents at once. A tester can report bugs directly to the coder who wrote the code.

### 🧠 Self-Learning Memory
After every run, SAMURAI saves what worked and what didn't. The Queen reads past learnings before composing a new team:

- *"Last time I used 3 coders for this size project, but 2 was enough"*
- *"The reviewer found 12 bugs — spawn reviewer earlier next time"*
- *"React approach won over Vue in the competitive round"*

Gets smarter with every run. Stored in `memory/learnings.json`.

### 🏆 Competitive Spawning
For critical deliverables, Queen spawns **two agents** with different approaches for the same task:

```
Coder-A → builds with React
Coder-B → builds with Vue

Queen evaluates both → picks the winner → discards the other
```

Costs 2x tokens for that one task, but guarantees higher quality where it matters most.

### 🔄 Auto-Healing
If an agent fails, crashes, or times out:

1. Queen detects the failure
2. Reads what the agent accomplished before dying
3. Spawns a replacement agent with that context
4. Run continues seamlessly — user never knows anything broke

### 💰 Model Tiering
Not every agent needs the most expensive model. Queen assigns models by complexity:

| Complexity | Model | Cost | Example Tasks |
|-----------|-------|------|---------------|
| Low | Haiku | $$ | File writing, formatting, simple transforms |
| Medium | Sonnet | $$$ | Coding, research, reviews, content |
| High | Opus | $$$$ | Architecture, complex reasoning, security |

Saves **60-70% on token costs** while maintaining output quality.

### ✋ Human Checkpoints
At critical decision points, Queen pauses and asks:

> 🗡️ **SAMURAI Checkpoint — Run #047**
>
> The architect proposed 2 approaches:
> - **A)** Monolithic Next.js app (faster to build, harder to scale)
> - **B)** Separate frontend + API (more work now, scales better)
>
> Which direction?

You reply → Queen tells the team → work continues with your decision baked in.

### 🗳️ Agent Voting
When agents disagree:

1. Each agent states their position with reasoning
2. All positions shared on the message bus
3. Agents vote
4. Majority wins — Queen breaks ties
5. Decision recorded for future learning

### 🔗 Pipeline Chaining
Multi-phase projects where each phase feeds into the next:

```
Phase 1: Research       → output: research.md
    ↓ automatically feeds into
Phase 2: Design         → output: design.md  
    ↓ automatically feeds into
Phase 3: Build          → output: /dist/
    ↓ automatically feeds into
Phase 4: Test & Review  → output: test-results.md
```

Each phase gets its own team. Queen manages transitions automatically.

### 🧬 Skill Inheritance
Spawned agents can use **any installed OpenClaw skill**:

- `web_search` / `web_fetch` for research
- `content-engine` for blog posts
- `code-reviewer` for code quality
- `test-generator` for writing tests
- Any custom skill in the workspace

Queen decides which skills each agent needs based on their role.

### 🔀 Run Replay & Fork
Every run is saved. You can:

- **Replay** — Run the same task structure with a new objective
- **Fork** — Take a completed run's outputs and modify them

```bash
# Replay: same team structure, new objective
python3 orchestrate.py replay <run-id> "Same thing but for mobile"

# Fork: copy outputs as starting context, then modify  
python3 orchestrate.py fork <run-id> "Change frontend from React to Vue"
```

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                    USER                                │
│              "Build me a SaaS app"                     │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│              🐝 QUEEN AGENT                           │
│                                                       │
│  1. Analyze task complexity                           │
│  2. Check past learnings                              │
│  3. Decide team: 6 agents                             │
│  4. Assign model tiers                                │
│  5. Define execution phases                           │
│  6. Spawn all agents                                  │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│              AGENT SWARM                              │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │Researcher│←→│Architect │←→│ Coder-1  │           │
│  │ (Sonnet) │  │  (Opus)  │  │ (Sonnet) │           │
│  └──────────┘  └──────────┘  └────┬─────┘           │
│                                    ↕                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ Designer │←→│ Coder-2  │←→│ Reviewer │           │
│  │ (Sonnet) │  │ (Sonnet) │  │ (Sonnet) │           │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                       │
│  Communication: sessions_send() + bus.jsonl + files   │
│  Shared workspace: runs/<id>/outputs/                 │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│              QUEEN SYNTHESIS                          │
│                                                       │
│  Collect all outputs → Evaluate quality →             │
│  Pick competitive winners → Compile deliverable →     │
│  Save learnings → Deliver to user                     │
└──────────────────────────────────────────────────────┘
```

---

## Communication Flow Example

A real example of agents building a landing page:

```
12:00:00  [architect → all]     DECISION: "Using Next.js 15 + Tailwind + Supabase"
12:00:30  [researcher → all]    READY: "Competitor analysis at outputs/researcher/analysis.md"
12:01:00  [coder-1 → coder-2]   DIRECT: "I'll handle API routes, you take the UI components"
12:01:30  [coder-2 → coder-1]   DIRECT: "Got it. What's the auth strategy?"
12:02:00  [coder-1 → coder-2]   DIRECT: "Supabase Auth — architect decided. Check bus."
12:03:00  [designer → coder-2]  DIRECT: "Color palette + layout specs at outputs/designer/"
12:05:00  [coder-1 → all]       READY: "API routes complete at outputs/coder-1/api/"
12:05:30  [reviewer → coder-1]  FEEDBACK: "3 issues found. See outputs/reviewer/feedback.md"
12:06:00  [coder-1 → reviewer]  DIRECT: "Fixed. Check again."
12:07:00  [coder-2 → all]       DONE: "Frontend complete at outputs/coder-2/"
12:07:30  [reviewer → all]      DONE: "All code reviewed, 0 issues remaining"
12:08:00  [queen → user]        "Here's your landing page! 🗡️"
```

---

## Decomposition Patterns

The Queen has 10 built-in decomposition patterns to draw from:

| Pattern | When | Agents |
|---------|------|--------|
| **Build Software** | "Build me a..." | Researcher + Architect + Coders + Reviewer + Tester |
| **Research & Report** | "Research..." | Researchers (parallel) + Analyst + Writer |
| **Code Audit** | "Review this code" | Security + Quality + Performance (parallel) |
| **Content Creation** | "Write a blog post" | Researcher + SEO + Writers (competitive) + Editor |
| **Refactor / Migrate** | "Migrate from..." | Analyst + Migrators (parallel) + Tester |
| **Debug / Fix** | "Fix this bug" | Investigators (parallel) + Fixer + Tester |
| **Data Processing** | "Analyze this data" | Schema Analyst + Processors (parallel) + Aggregator |
| **Strategy / Planning** | "Plan a..." | Researchers (parallel) + Strategist + Planner |
| **Pipeline** | Large multi-phase projects | Chains multiple patterns in sequence |
| **Simple Task** | Quick one-step task | No swarm — Queen handles directly |

Queen adapts and combines these. They're starting points, not rigid templates.

---

## File Structure

```
skills/samurai/
├── SKILL.md                          ← Skill definition (OpenClaw reads this)
├── SAMURAI.md                        ← This documentation
├── references/
│   ├── queen-prompt.md               ← Queen's full orchestration logic
│   ├── worker-prompt.md              ← Base instructions for all spawned agents
│   ├── communication.md              ← Inter-agent communication protocol
│   └── patterns.md                   ← Task decomposition patterns
├── scripts/
│   └── orchestrate.py                ← Run management CLI
├── memory/
│   └── learnings.json                ← Self-learning data (grows over time)
└── runs/                             ← Created dynamically per run
    └── <run-id>/
        ├── run.json                  ← Run metadata & agent roster
        ├── bus.jsonl                 ← Message bus (agent communication log)
        ├── memory.json               ← Shared state (facts, decisions, votes)
        ├── pipeline.json             ← Pipeline definition (if multi-phase)
        └── outputs/                  ← Agent deliverables
            ├── architect/
            ├── coder-1/
            ├── coder-2/
            └── reviewer/
```

---

## CLI Commands

```bash
# Create a new run
python3 orchestrate.py create "Build a SaaS dashboard"

# Check run status
python3 orchestrate.py status <run-id>

# List all runs
python3 orchestrate.py list

# View message bus
python3 orchestrate.py bus <run-id>
python3 orchestrate.py bus <run-id> --tail 20

# Save learnings from a completed run
python3 orchestrate.py learn <run-id>

# Replay a run with new objective
python3 orchestrate.py replay <run-id> "Same but for mobile app"

# Fork a run (copy outputs as starting context)
python3 orchestrate.py fork <run-id> "Change React to Vue"

# Cleanup old runs
python3 orchestrate.py cleanup --older-than 7d
```

---

## What Makes SAMURAI Different

| Feature | Other Systems | SAMURAI |
|---------|--------------|---------|
| Agent creation | Predefined list (pick from menu) | **Dynamic** (Queen creates on-the-fly) |
| Communication | Agents report to coordinator only | **Agents talk to each other** |
| Team size | Fixed | **2 to 50+, Queen decides** |
| Learning | None | **Self-learning from every run** |
| Failure handling | Run fails | **Auto-healing** (spawn replacement) |
| Cost control | One model for everything | **Model tiering** (3 tiers by complexity) |
| Human involvement | All or nothing | **Checkpoints** at key decisions |
| Disagreements | First agent wins | **Voting** with majority rule |
| Reusability | Start from scratch | **Replay & Fork** past runs |

---

## Platform

SAMURAI is built for **OpenClaw** and uses native primitives:
- `sessions_spawn()` → create agents
- `sessions_send()` → agent-to-agent messaging
- `sessions_list()` → discover agents
- Standard file I/O → shared workspace

No external dependencies. No Python packages. No Docker. Just OpenClaw.

---

*Built by Sam. Powered by AI. Orchestrated by the Queen.* 🗡️
