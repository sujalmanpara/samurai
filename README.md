<p align="center">
  <img src="https://img.shields.io/badge/SAMURAI-v1.1-red?style=for-the-badge&labelColor=1a1a2e&color=e94560" alt="Version"/>
  <img src="https://img.shields.io/badge/OpenClaw-Native-blue?style=for-the-badge&labelColor=1a1a2e&color=0f3460" alt="Platform"/>
  <img src="https://img.shields.io/badge/Agents-Dynamic-green?style=for-the-badge&labelColor=1a1a2e&color=16c79a" alt="Agents"/>
  <img src="https://img.shields.io/badge/License-Private-gray?style=for-the-badge&labelColor=1a1a2e&color=6c757d" alt="License"/>
</p>

<h1 align="center">🗡️ SAMURAI</h1>

<p align="center">
  <strong>Sam's Autonomous Multi-agent Unified Runtime for AI</strong>
</p>

<p align="center">
  <em>Dynamic multi-agent orchestration where a Queen agent builds the perfect team on-the-fly,<br>and agents don't just work — they collaborate.</em>
</p>

---

## 🎯 What is SAMURAI?

SAMURAI is not another agent framework with a menu of predefined bots. It's an **intelligent orchestration system** that:

- **Analyzes** your task and decides the exact team needed
- **Spawns** 2 to 50+ agents dynamically — no predefined list
- **Coordinates** agents that talk to each other, not just back to a controller
- **Learns** from every run and gets smarter over time

```
You: "Build me a SaaS landing page"

SAMURAI Queen: "I need 6 agents for this."
├── 🔍 Researcher (Sonnet) → competitor analysis
├── 🏗️ Architect (Opus) → system design
├── 💻 Coder-1 (Sonnet) → backend API
├── 🎨 Coder-2 (Sonnet) → frontend UI
├── 📝 Copywriter (Haiku) → headlines & CTAs
└── 🔎 Reviewer (Sonnet) → code review + feedback loops

Agents collaborate → Review loops → Final delivery
Total time: ~5 minutes
```

---

## ⚡ Features

### Core Orchestration

| Feature | Description |
|---------|------------|
| 🐝 **Dynamic Spawning** | Queen creates any agent type on-the-fly — researcher, architect, coder, designer, anything |
| 💰 **Model Tiering** | Haiku for simple tasks, Sonnet for medium, Opus for complex. Saves 60-70% on tokens |
| 🏆 **Competitive Spawning** | Two agents, same task, different approaches — best result wins |
| 🔄 **Auto-Healing** | Agent crashes? Queen spawns a replacement with the dead agent's context |
| 🧠 **Self-Learning** | Every run saves learnings. Queen gets smarter over time |
| ✋ **Human Checkpoints** | Queen pauses at critical decisions and asks you |
| 🗳️ **Agent Voting** | Agents disagree? They vote. Majority wins. Queen breaks ties |
| 🔗 **Pipeline Chaining** | Multi-phase projects where each phase feeds into the next |
| 🧬 **Skill Inheritance** | Agents use any installed OpenClaw skill |
| 🔀 **Replay & Fork** | Reuse or modify past runs |

### Advanced Communication (v1.1)

| Feature | Description |
|---------|------------|
| 🔄 **Review Loops** | Reviewer ↔ Coder back-and-forth until code is approved |
| 📡 **Topic Channels** | Separate chat rooms per topic — frontend, backend, decisions |
| 🌳 **Agent Hierarchy** | Lead agents spawn and manage their own sub-agents |
| ❓ **Request/Response** | Structured ask-and-answer with deadlines |
| 📋 **Shared Blackboard** | Collaborative problem-solving workspace |
| 🚨 **Priority Levels** | Critical → High → Normal → Low message priority |
| 🔁 **Dead Letter Queue** | Messages to dead agents get saved and forwarded |
| 🧠 **Context Sharing** | Agents share compressed briefings for downstream work |
| 📊 **Agent Reputation** | Tracks which model+role combos work best over time |
| 🔀 **Dynamic Role Switch** | Idle agents get reassigned instead of spawning new |
| 👤 **Context Injection** | Workers know your preferences, style, and conventions |
| 📏 **Style Contract** | Shared coding/writing rules all agents follow |
| 🔍 **Integration Review** | Consistency check before assembly — no Frankenstein code |
| ⚠️ **Anti-Pattern Detection** | Queen knows when NOT to swarm |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                         YOU                               │
│                  "Build me X"                             │
└────────────────────────┬─────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│                   🐝 QUEEN AGENT                          │
│                                                           │
│   📊 Check reputation → 🧠 Read past learnings →          │
│   🔍 Analyze task → 👥 Compose team →                     │
│   💰 Assign model tiers → 🚀 Spawn agents                │
└────────────────────────┬─────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│                   AGENT SWARM                             │
│                                                           │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│   │Lead-Back │←──→│Lead-Front│←──→│ Reviewer  │          │
│   │  (Opus)  │    │  (Opus)  │    │ (Sonnet)  │          │
│   └────┬─────┘    └────┬─────┘    └───────────┘          │
│        ↓               ↓                                  │
│   ┌────┴────┐    ┌────┴────┐                              │
│   │Coder-API│    │Coder-UI │     Communication:           │
│   │(Sonnet) │    │(Sonnet) │     📡 Topic Channels        │
│   └─────────┘    └─────────┘     📋 Shared Blackboard     │
│                                  🔄 Review Loops           │
│                                  ❓ Request/Response       │
└────────────────────────┬─────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│                   QUEEN SYNTHESIS                         │
│                                                           │
│   Collect outputs → Evaluate quality → Pick winners →     │
│   Compile deliverable → Save learnings → Update rep →     │
│   Deliver to you 🎁                                      │
└──────────────────────────────────────────────────────────┘
```

---

## 🔗 Agent Communication

Agents don't work in isolation — they **collaborate** through 6 channels:

| Channel | How | Example |
|---------|-----|---------|
| **Direct Message** | `sessions_send()` | "Hey coder, bug on line 42" |
| **Topic Channels** | `bus/*.jsonl` files | "Everyone: we're using PostgreSQL" |
| **Shared Files** | `outputs/` directory | Code, docs, deliverables |
| **Blackboard** | `blackboard.json` | API endpoints, env vars, decisions |
| **Request/Response** | Structured Q&A | "Should we use REST or GraphQL?" → "REST" |
| **Context Shares** | Compressed briefings | "Here's a summary of my research..." |

```
12:00  🏗️ [architect → decisions]     "Tech stack: Next.js + Tailwind + Supabase"
12:01  🔍 [researcher → general]      "Competitor analysis ready at outputs/researcher/"
12:02  💻 [coder-1 → coder-2]         DM: "I'll handle API routes, you take UI"
12:03  💻 [coder-2 → architect]       REQ: "REST or GraphQL?" deadline: 30s
12:03  🏗️ [architect → coder-2]       RES: "REST. Simpler for this use case."
12:05  💻 [coder-1 → general]         "API routes complete"
12:06  🔎 [reviewer → coder-1]        FEEDBACK: "3 issues found"
12:07  💻 [coder-1 → reviewer]        REVISION: "Fixed all 3"
12:08  🔎 [reviewer → coder-1]        APPROVED ✅
12:09  🐝 [queen → you]               "Here's your project! 🗡️"
```

---

## 📁 File Structure

```
skills/samurai/
├── SKILL.md                          ← Skill definition (OpenClaw reads this)
├── README.md                         ← You're here
├── SAMURAI.md                        ← Full documentation
├── references/
│   ├── queen-prompt.md               ← Queen's orchestration brain
│   ├── worker-prompt.md              ← Instructions for every spawned agent
│   ├── communication.md              ← Full inter-agent protocol (v1.1)
│   └── patterns.md                   ← Task decomposition patterns
├── scripts/
│   └── orchestrate.py                ← Run management CLI
├── memory/
│   ├── learnings.json                ← Self-learning data
│   └── reputation.json               ← Agent model+role reputation
└── runs/                             ← Created per run
    └── <run-id>/
        ├── run.json                  ← Run metadata
        ├── bus/                      ← Topic channels
        │   ├── general.jsonl
        │   ├── decisions.jsonl
        │   ├── urgent.jsonl
        │   └── dead-letters.jsonl
        ├── blackboard.json           ← Shared problem-solving state
        ├── memory.json               ← Run-level shared memory
        ├── pipeline.json             ← Pipeline definition (if multi-phase)
        └── outputs/                  ← Agent deliverables
            ├── architect/
            ├── coder-1/
            └── reviewer/
```

---

## 🚀 Quick Start

### Install
```bash
# Copy to your OpenClaw workspace
cp -r samurai/ ~/.openclaw/workspace/skills/samurai/
```

### Use
Just give your OpenClaw agent a complex task. SAMURAI activates automatically for multi-step work, or invoke it explicitly:

> "Use SAMURAI to build a REST API with auth, rate limiting, and tests"

### CLI
```bash
# Create a run
python3 orchestrate.py create "Build a dashboard"

# Check status
python3 orchestrate.py status <run-id>

# View message bus
python3 orchestrate.py bus <run-id>
python3 orchestrate.py bus <run-id> --channel decisions

# List all runs
python3 orchestrate.py list

# Save learnings
python3 orchestrate.py learn <run-id>

# Replay with new objective
python3 orchestrate.py replay <run-id> "Same but for mobile"

# Fork from existing run
python3 orchestrate.py fork <run-id> "Switch from React to Vue"

# Cleanup old runs
python3 orchestrate.py cleanup --older-than 7d
```

---

## 🆚 How is SAMURAI Different?

| | Traditional Frameworks | SAMURAI |
|---|---|---|
| **Agent creation** | Pick from predefined menu | Queen creates on-the-fly |
| **Team size** | Fixed | 2 to 50+, Queen decides |
| **Communication** | Report to coordinator only | Agents talk to each other |
| **Channels** | Single bus | Topic channels + DMs + blackboard |
| **Hierarchy** | Flat | Leads spawn sub-agents |
| **Learning** | None | Self-learning + reputation tracking |
| **Failure** | Run crashes | Auto-healing with context transfer |
| **Cost** | One model for all | 3-tier model assignment |
| **Human input** | All or nothing | Checkpoints at key decisions |
| **Disagreements** | First agent wins | Voting with majority rule |
| **Code quality** | Ship and pray | Review loops until approved |
| **Reusability** | Start from scratch | Replay & Fork past runs |

---

## 🧩 Decomposition Patterns

SAMURAI includes 10 built-in patterns the Queen draws from:

| Pattern | When | Example |
|---------|------|---------|
| Build Software | "Build me a..." | Researcher + Architect + Coders + Reviewer |
| Research & Report | "Research..." | Parallel researchers + Analyst + Writer |
| Code Audit | "Review this code" | Security + Quality + Performance |
| Content Creation | "Write a blog post" | Researcher + Writers (competitive) + Editor |
| Refactor/Migrate | "Migrate from..." | Analyst + Parallel migrators + Tester |
| Debug/Fix | "Fix this bug" | Investigators + Fixer + Tester |
| Data Processing | "Analyze this data" | Schema analyst + Parallel processors |
| Strategy/Planning | "Plan a..." | Researchers + Strategist + Planner |
| Pipeline | Large multi-phase | Chains multiple patterns |
| Simple Task | Quick one-step | No swarm — Queen handles directly |

---

## 📊 Real World Usage

### SAMURAI's First Run: Ampere Shield
SAMURAI was used to build **Ampere Shield** — a prompt injection prevention system (1,528 lines of TypeScript):

```
Run #0316-1243-1fd8 — Ampere Shield
├── ✅ Decoder Agent (1m27s) → decoder.ts
├── ✅ Patterns Agent (2m28s) → patterns.ts (120 rules!)
├── ✅ Invisible Agent (1m0s) → invisible.ts
├── ✅ Scorer Agent (1m56s) → scorer + output-scan + config + logger + index
├── ✅ Integration Agent (2m4s) → proxy-handler.ts hooks

5 agents • 2 phases • ~8 minutes total
Then PR-reviewed by 4 more agents (quality, regression, alternatives, coordinator)
```

---

## 🔧 Requirements

- **OpenClaw** — installed and running
- **AI Model** — Claude API access (Haiku + Sonnet + Opus recommended)
- **Python 3** — for orchestrate.py CLI
- That's it. No external dependencies.

---

## 🛣️ Roadmap

- [x] v1.0 — Core orchestration (dynamic spawning, 10 features)
- [x] v1.1 — Advanced communication (10 new features)
- [x] v1.2 — Context Injection (workers know user preferences)
- [x] v1.3 — Quality Guard (style contracts, integration review, anti-pattern detection)
- [ ] v2.0 — Visual dashboard, vector memory, ML-assisted scoring

---

<p align="center">
  <strong>Built by Sam. Powered by AI. Orchestrated by the Queen.</strong> 🗡️
</p>
