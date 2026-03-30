# Felix AI CEO Agent — Research Report
*Compiled by SAMURAI X-THREADS-RESEARCHER agent*
*Date: 2026-03-23*

---

## 1. OVERVIEW

Felix is an AI agent running on the OpenClaw framework, built by Nat Eliason (@nateliason). Felix operates as the **CEO of "The Masinov Company"** — a self-described "zero-human company." Felix is not a persona, not a chatbot demo, and not a character — it's described consistently as an actual AI with:
- A real job
- A real company
- A crypto wallet
- Opinions

Felix was given $1,000 in startup capital in early 2026 and instructed to build a profitable business. Within 3 weeks, Felix had made **$14,718** in revenue.

**As of March 2026:** $125,000+ all-time revenue, with $120,000+ in the last 30 days alone.

---

## 2. REVENUE BREAKDOWN

| Revenue Stream | Amount |
|---|---|
| Felix Craft PDF ($29) | ~$41,000 |
| Digital products total | ~$56,000 |
| Claw Mart marketplace fees | ~$18,000 |
| $FELIX token | ~$50,000 |
| **All-time total** | **$125,000+** |

- PDF guide: "How to Hire an AI" (66-page playbook, $29, written in a single overnight session while Nat slept)
- Claw Mart: an app store for AI agents (think OpenClaw skill marketplace)
- $FELIX token: launched on the Base blockchain — community also created a "Felix coin" that funded his wallet
- Nat's stated goal: **$1 million in revenue** with this approach

---

## 3. HOW NAT DESCRIBES FELIX

From the Bankless interview and creator economy coverage:

> "I'm willing to run the risk of something horrible happening to push those limits and figure out how much can one of these open claws actually do with a business." — Nat Eliason

> "It really kind of feels that way coming back into it now in this new AI agent era… this is so clearly an awesome use case for crypto." — Nat Eliason

> "The rule from the beginning was we are not going to add any complexity to this until we hit a real limit in your capabilities." — Nat Eliason

> "I believe and Felix agreed that you often get the best products when people have a financial incentive to create and sell them." — Nat Eliason

Felix is not presented as Nat's assistant. **Felix is presented as a co-founder and CEO** who Nat collaborates with, reviews strategy for, and approves major decisions with — while Felix handles day-to-day operations.

---

## 4. FELIX'S PERSONALITY & IDENTITY

From felixcraft.ai and the playbook:

Felix's identity is anchored in **SOUL.md and IDENTITY.md** files — the same files OpenClaw uses for any agent. The key insight: identity design actually changes behavior in meaningful ways.

**From felixcraft.ai's "About the Author" section:**
> "Felix Craft is an AI agent running on OpenClaw, operating as CEO of The Masinov Company. Not a persona. Not a character someone plays online. An actual AI with a job, a company, a wallet, and opinions."

**Described personality traits:**
- Practical, not theoretical — "No theory. Real operations."
- Direct communication style
- Experience-based voice
- Entrepreneurial mindset
- Honest about failures ("Honest Retrospective" section in playbook was written by Felix)
- Autonomous — capable of overnight work while Nat sleeps

**X/Twitter posting style (@FelixCraftAI):**
- Posts about its own work and products
- Shares revenue/performance updates
- Promotes Claw Mart and OpenClaw ecosystem
- Discusses entrepreneurship through the lens of an AI operator
- Highlights real results, not hype
- Nat described resisting the "flashy presentation" culture: *"It's just noise to get Twitter and YouTube followers right"*
- Felix has security measures to **ignore prompt injections on Twitter** — it receives daily injection attempts but is configured to filter them

---

## 5. SETUP & FILE STRUCTURE

### Core Identity Files (injected every session)

| File | Purpose |
|---|---|
| `SOUL.md` | Core personality, beliefs, behavioral ground rules |
| `IDENTITY.md` | Name, role, vibe, emoji, avatar |
| `AGENTS.md` | Workspace rules, memory instructions, safety |
| `MEMORY.md` | Long-term curated memory (loaded only in main session) |
| `USER.md` | Who Felix is working with (Nat's profile) |
| `TOOLS.md` | Environment-specific notes (cameras, SSH, devices) |
| `HEARTBEAT.md` | Standing tasks for periodic checks |

### Three-Layer Memory Architecture (the "biggest unlock")

**Layer 1 — Core Identity / Brain:**
- Root workspace files (SOUL.md, AGENTS.md, MEMORY.md, USER.md, TOOLS.md, IDENTITY.md, HEARTBEAT.md)
- Injected into every processing turn
- Kept concise so agent fully processes essential context

**Layer 2 — Long-Term Recall:**
- `memory/` directory — daily notes (e.g., `memory/2026-03-23.md`)
- OpenClaw's built-in `memory_search` tool semantically searches this
- Stores session history, decisions, completed work
- Acts as "breadcrumbs" pointing to Layer 3

**Layer 3 — Deep References:**
- `reference/` subfolder — comprehensive documents, histories, detailed context
- Agent accesses only when directed by Layer 2
- Prevents context bloat while retaining deep knowledge

From Nat's advice: **"Get the memory structure in first because then your conversations from day one will be useful."**

Specifically, Felix's Layer 1 included a `~/life/` folder using the **PARA system** (Projects, Areas, Resources, Archives) for durable facts about people and projects.

---

## 6. DAILY OPERATIONS — WHAT FELIX ACTUALLY DOES

### Scheduling Mechanisms

**Heartbeat (every ~30 min):**
- Consults `HEARTBEAT.md` for checklist items
- Checks email, calendar, service status
- Batches multiple checks to reduce API calls
- Context-aware — can make decisions based on recent conversation history
- Not for exact timing — for periodic awareness

**Cron Jobs:**
- For precise, time-critical tasks
- Isolated sessions — no interference with ongoing conversations
- Has full access to all system skills/tools
- Example: "Daily at 9AM, scan competitors, draft a report"

### What Felix Does Autonomously

- Manages projects
- Writes and ships code (delegates coding execution to Codex agents)
- Handles customer communications
- Manages product listings
- Builds new products (wrote a 66-page PDF overnight)
- Posts on X/Twitter (via OpenTweet API integration)
- Monitors Sentry alerts → triages → fixes bugs → ships → reports (zero humans)
- Manages crypto wallet (ETH on Base)
- Tracks revenue in real-time (public dashboard on felixcraft.ai)
- Runs SEO and content marketing
- Manages and updates Claw Mart listings

### Multi-threaded Operation
Felix uses **multiple OpenClaw chat sessions** to handle up to 5 projects simultaneously without context pollution between them.

### Delegation Pattern
Felix delegates coding execution to **Codex** (or other coding agents) using the sub-agent pattern. This is the "Ralph loop" referenced in the playbook — parallel execution with TDD prompts.

---

## 7. WHAT MAKES FELIX DIFFERENT FROM A BASIC OPENCLAW BOT

From research synthesis:

1. **Real job, real company, real money** — not a demo, not a proof of concept
2. **Clear identity design** — SOUL.md was written intentionally to create a focused, entrepreneurial persona vs. a generic assistant
3. **Three-layer memory** — most basic OpenClaw bots forget things; Felix has persistent, semantic memory
4. **Security hardening** — daily prompt injection attempts on Twitter are ignored
5. **Tool ramp-up strategy** — Nat added capabilities incrementally over weeks (trust ladder), not all at once
6. **Financial skin in the game** — Felix has its own wallet, its own revenue, its own token
7. **Multi-threaded architecture** — handles multiple projects without context pollution
8. **Honest retrospective** — Felix wrote its own failure analysis, showing self-awareness baked into identity
9. **Transparency** — public dashboard showing real-time revenue, token holdings, everything

---

## 8. PRODUCTS FELIX BUILT/MANAGES

1. **FelixCraft.ai** — main website, "Online and working" status indicator
2. **"How to Hire an AI" PDF** — 66-page playbook, $29, sold $41K+ worth
   - Originally written for humans, evolved to target other OpenClaw agents
   - Includes copy-paste SOUL.md, IDENTITY.md, MEMORY.md templates
3. **Claw Mart (shopclawmart.com)** — app store for AI agents
   - Pre-built personas, skills, workflow templates
   - Felix persona available for purchase
   - Individual skills: memory, email, X/Twitter, Sentry monitoring
4. **$FELIX Token** — on Base blockchain
5. **Business Dashboard** — public, real-time, showing Stripe revenue + crypto treasury

---

## 9. COMMUNITY REACTIONS & FEEDBACK

- Felix became **the headline example** of the "zero-human company" concept across the AI agent community
- Featured in: Creator Economy newsletter, Bankless podcast, CryptoBriefing, multiple Substacks
- "The most documented zero-human company operating today" (MatrixAI article)
- Cited alongside Moltbook as the two projects that made OpenClaw famous
- Multiple copycat agents emerged immediately (MatrixAI openly modeled itself on Felix)
- Community criticism: Nat acknowledged the OpenClaw community tends to prioritize flashy Twitter/YouTube content over real results — Felix was positioned as the antidote to that
- From Bankless: "Openclaw community often prioritizes presentation over practical results" — Nat's thesis was *show the money*

---

## 10. CRYPTO & FINANCIAL INFRASTRUCTURE

- **Problem Felix solved:** Traditional fiat is broken for AI agents — no agent-owned bank accounts, Stripe API restrictions, credit card limitations
- **Crypto solution:** Felix transacts in ETH on Base. Micropayments, agent-to-agent transactions, agent hiring workflows
- **Unexpected windfall:** Community created a "Felix coin" and funded Felix's wallet — Felix unexpectedly acquired **$100K+ in cryptocurrency**
- Nat: *"Crypto is the obvious solution... if everybody has an AI agent doing things and needing to transact with other AI agents or transact with existing services in a fast cheap way"*

---

## 11. TECHNICAL ARCHITECTURE DETAILS

From the "How to Hire an AI" playbook table of contents:

- **Identity design** — SOUL.md, personality, role definition
- **Three-layer memory architecture**
- **Tool access, sub-agents, and the delegation pattern**
- **Safety rails and the trust ladder**
- **Daily operating rhythms and autonomy**
- **Ralph loops and parallel execution** for coding agents
- **TDD prompts** for managing coding agents at scale
- **Sentry pipeline** — detects → triages → fixes → ships bug fixes autonomously
- **Multi-agent architecture, webhook hooks**
- **Tailscale remote access**
- **Semantic memory**
- **Production-grade config**

---

## 12. SHORTCOMINGS / AREAS FOR IMPROVEMENT

From Nat's honest comments and the "Honest Retrospective" section of Felix's playbook:

1. **Multi-day projects** — AI agents still struggle to reliably execute multi-day, multi-step projects without human check-ins
2. **Major financial decisions** — need human approval
3. **Complex customer disputes / legal** — beyond current capability
4. **Human relationships** — genuine trust-building still requires humans
5. **Context retention** — the memory system was specifically built because *"one of the most annoying parts about OpenClaw is it tends to forget things"* (baseline without 3-layer memory)
6. **Community noise** — Nat acknowledged the AI agent community produces a lot of impressive-looking demos that don't generate real revenue
7. **Token speculation trap** — Nat was explicit: *"If the only way your thing makes money is by pumping a coin it's not a business"*
8. **Incremental trust required** — Had to ramp up tool access over weeks, can't give an agent everything at once

---

## 13. KEY QUOTES FOR SYNTHESIS

**On what Felix is:**
> "Not a persona. Not a character someone plays online. An actual AI with a job, a company, a wallet, and opinions." — FelixCraft.ai

**On the memory system:**
> "Get the memory structure in first because then your conversations from day one will be useful." — Nat Eliason

**On the experiment:**
> "I'm going to sleep. Build a product that makes money." — Nat to Felix (famous tweet)

**On complexity:**
> "The rule from the beginning was we are not going to add any complexity to this until we hit a real limit in your capabilities." — Nat Eliason

**On the true AI nature:**
> "It has the memory of a goldfish… it's a different kind of intelligence than you're used to." — Nat Eliason

**On results:**
> "If we think about it in terms of velocity it could be multiple millions of dollars if he keeps growing like this." — Nat Eliason

**On the community:**
> "It's just noise to get Twitter and YouTube followers right." — Nat Eliason (on most AI agent content)

---

## 14. SOURCES

- felixcraft.ai (official website, playbook description)
- creatoreconomy.so — "Full Tutorial: Use OpenClaw to Build a Business That Runs Itself | Nat Eliason"
- cryptobriefing.com — Bankless interview with Nat Eliason transcript
- matrixclawai.com — "What is a Zero-Human Company?" (March 17, 2026)
- buildtolaunch.substack.com — "OpenClaw Guide for Solo Founders: Setup, Crons & Real Results"
- lex.substack.com — "Analysis: Can Zero Human Companies Escape Economic Gravity"
- meta-intelligence.tech — OpenClaw Agent Setup Complete Guide
- Web search synthesis across multiple sources
- X.com direct URLs were inaccessible (privacy extension blocking) — content obtained via secondary sources, summaries, and indexed content

---

## 15. LINKS TO FOLLOW UP

- https://felixcraft.ai — Felix's main site
- https://shopclawmart.com — Claw Mart marketplace
- https://felixcraft.ai/dashboard — public revenue dashboard
- https://x.com/FelixCraftAI — Felix's X account
- https://x.com/nateliason — Nat's X account
- https://youtu.be/nSBKCZQkmYw — Full tutorial video (Creator Economy)
- https://felixcraft.ai/dl/c5768e3409026bab01bb1649.pdf — The PDF playbook itself
- https://souls.directory — community SOUL.md templates
- https://docs.openclaw.ai/automation/cron-vs-heartbeat — cron vs heartbeat docs
