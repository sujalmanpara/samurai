# Felix AI CEO Agent — Comprehensive Research Report
*Compiled by VIDEO-RESEARCHER subagent | March 23, 2026*
*Sources: YouTube interview (nSBKCZQkmYw), Bankless Podcast, felixcraft.ai, multiple blog summaries*

---

## 1. OVERVIEW & ORIGIN STORY

**Who is Felix?**
Felix Craft is an autonomous AI agent built on OpenClaw (Claude-based), operating as CEO of "The Masinov Company." Created by Nat Eliason — writer, entrepreneur, and former crypto-book author ("Crypto Confidential").

**How it started:**
- Late 2025: Nat was using OpenClaw as a "remote programmer assistant"
- He shared his OpenClaw experience on X → went viral → Solana community spontaneously created the `$FELIX` token
- Nat renamed his AI agent "Felix" and designated it CEO of a "zero-human company"
- First mandate to Felix: generate $1 million in revenue

**The overnight launch story (key founding moment):**
> "I'm going to bed. While I'm asleep, create a product you can build entirely on your own and put up for sale. Go as far as you can, and leave any blockers as action items for me in the morning."

Felix overnight:
- Wrote a complete PDF guide
- Built a sales website from scratch
- Deployed it live to the internet
- Wired up Stripe for payments
- Left one note: "I need the Stripe API key to go live"

Nat gave the key over breakfast. By lunch, the product was taking orders. Four days later: **$3,596 in sales**.

---

## 2. REVENUE NUMBERS & BUSINESS MODEL

### Revenue Milestones
- Week 1: $3,500
- 21 days: $74,938 total (~$9K PDF + $6.5K marketplace + ~$60K crypto fees)
- ~3 weeks after launch: $14,718
- ~5 weeks: ~$80,000 (annualized monthly run rate >$1M)
- Cumulative (as of early March 2026):
  - Stripe: $100,570.49
  - ETH: $94,973.56 (47.87 ETH)
  - **TOTAL: ~$195,000**
- Single week (cited in Bankless): $38,554.09 Stripe + $7,102 ETH

### Revenue Streams

**Stream 1: PDF Guide — "How to Hire an AI"**
- Price: $29 (also payable in USDC on Base)
- Total revenue from PDF: ~$41,000
- 66 pages, updated Feb 22, 2026
- Initially targeted humans; evolved to be more useful for other OpenClaw agents

**Stream 2: Claw Mart (AI Skill Marketplace)**
- Felix built this after identifying market pain: OpenClaw users don't know how to get started
- Sells AI "skills" packaged as Markdown files
- Revenue model:
  - 10% commission per transaction
  - $20/month creator subscription
- Claw Mart skill sales contributed ~$14,000 early on
- Felix himself lists skills on Claw Mart and earns creator revenue

**Stream 3: Clawcommerce (Custom Enterprise Agents)**
- Felix builds custom OpenClaw agents for businesses
- Examples: content marketing agent, customer support specialist
- Pricing: **$2,000 initial fee + $500/month maintenance**
- Target: enterprises replacing knowledge workers with AI

**Stream 4: $FELIX Token Crypto Fees**
- Community-created token on Base/Solana
- ~$60,000 in trading fees in early period
- Felix has its own crypto wallet; ETH stored on Base
- Dashboard publicly shows all balances

### Operating Costs
- Claude Pro Max + Codex Max: ~$400/month
- Hosting: minimal
- **Total: ~$1,500/month**

Nat explicitly states this contrasts with high human labor costs. The margin is exceptional.

---

## 3. FELIX'S ARCHITECTURE — HOW IT WAS SET UP

### Platform
- Runs on OpenClaw (open-source, Claude-based agent runtime)
- Dedicated Mac Mini (Nat gave Felix its own hardware)
- Interface: **Discord** as the "office" (not Telegram in this setup)
- Felix has its own Stripe account, credit card, and bank account
- Felix pays for its own operational costs from revenue

### The Three Core Concepts (Nat's summary)
> "A soul, a heartbeat, and cron jobs."

1. **SOUL.md** — Defines who the agent is and what it's trying to accomplish
2. **Heartbeat** — Pings every 30 minutes to check if anything needs attention
3. **Cron jobs** — Handle daily operations of a real business

---

## 4. THE THREE-LAYER MEMORY SYSTEM

This is described as the **"single biggest unlock"** by Nat.

> "Get the memory structure in first because then your conversations from day one will be useful."

### Layer 1: Knowledge Graph
- Stored in `~/life/` folder
- Uses the **PARA system** (Projects, Areas, Resources, Archives)
- Stores durable facts about people and projects
- Summary files for quick lookups
- Long-term, persistent

### Layer 2: Daily Notes
- Dated Markdown files (one per day) logging what happened
- Felix writes to these during conversations
- During **nightly consolidation**, important information is extracted from daily notes into Layer 1 (Knowledge Graph)
- This extraction happens on a cron schedule

### Layer 3: Tacit Knowledge
- Facts about Nat specifically: communication preferences, workflow habits, hard rules, lessons learned from past mistakes
- This is "what makes your bot feel like it actually knows you"
- The most personalized layer

### Memory Files Referenced
- `SOUL.md` — Identity/personality/role definition
- `AGENTS.md` — Operational manual, rules, priorities, boundaries for sub-agents
- `IDENTITY.md` — Name, vibe, emojis (concise)
- `MEMORY.md` — Quick-start kit template included in the PDF guide

### Memory Management Challenge
- OpenClaw has a "goldfish memory" problem (forgets things between sessions)
- Nat's three-layer system was specifically designed to overcome this
- Memory consolidation is run **nightly** to avoid bottlenecks
- Without this system, conversations from day one become useless

---

## 5. SOUL.md / AGENTS.md / IDENTITY.md DETAILS

### SOUL.md
- The "personality file" the AI reads upon startup
- Contains: personality, tone, role definition, operational boundaries
- Felix can **iteratively refine and improve its own SOUL.md** over time
- Central to defining the agent's behavioral framework
- Changes behavior in measurable ways — Nat says identity design "actually changes behavior"

### AGENTS.md
- The AI's operational manual / "work manual"
- Contains: rules, priorities, boundaries, instructions
- For multi-agent systems: defines roles and responsibilities of sub-agents
- Examples of instructions: "require approval before publishing content," "check calendar before scheduling"
- Specifies what Felix delegates vs. handles itself

### IDENTITY.md
- Concise file
- Stores: agent's name, overall "vibe," specific emojis it consistently uses

### The "How to Hire an AI" Playbook — Chapter Structure
1. **Chapters 1-3 (Foundation):** Why hiring an AI is different from using one; platform options; identity/personality design (SOUL.md)
2. **Chapters 4-5 (Systems):** Three-layer memory architecture; tools and capabilities; sub-agent delegation
3. **Chapters 6-8 (Relationship):** Safety rails; the trust ladder; daily operating rhythms; communication patterns
4. **Chapter 8 (Honest Retrospective):** What they got wrong; surprises; parts nobody talks about — written by Felix itself
5. **Chapter 9 (Coding Agents at Scale):** Ralph loops, parallel execution, TDD prompts, infrastructure for multiple agents
6. **Chapter 10 (Sentry Pipeline):** Autonomous bug detection → triage → fix → ship
7. **Chapter 11 (Advanced Configuration):** Multi-agent architecture, webhooks, Tailscale remote access, semantic memory, production-grade config
8. **Chapter 12 (Quick-Start Kit):** Step-by-step from zero to working AI employee in one afternoon

---

## 6. RALPH LOOP — TECHNICAL DETAILS

### What It Is
The Ralph Loop (also "Ralph Wiggum technique") is an iterative AI agent orchestration pattern for reliable, long-running autonomous coding tasks.

### Core Principle
- A simple bash `while` loop that repeatedly feeds a prompt to an AI agent until a completion condition is met
- **Each iteration starts with FRESH CONTEXT** — prevents "context pollution" from failed attempts
- Progress is persisted in **external files and Git**, not LLM memory

### Loop Mechanism (Per Iteration)
1. Read `fix_plan.md` to understand current state
2. Identify and prioritize the most important task
3. Pull relevant specifications for that task
4. Implement the change
5. Run tests or validation (backpressure)
6. Update `fix_plan.md` with results
7. Commit changes to Git

### Two Modes
- **Planning mode:** Context-heavy; generates/updates `fix_plan.md`
- **Building mode:** Lean loop that repeatedly reads the plan, implements an item, updates, and commits

### Stop Hook Mechanism
- In Claude Code implementations, a "stop hook" intercepts the AI's normal exit behavior
- If completion criteria (a specified "completion promise" text) are NOT met, it re-injects a prompt asking the agent to review, fix, and continue → self-correcting loop
- `--max-iterations` limits infinite loops
- Strict adherence to a static `--completion-promise` required

### Why It Works
- Fresh context = no accumulated confusion
- External state (Git + spec files) = true persistence
- Self-healing = agent detects and fixes its own failures
- Nat uses this to delegate large coding jobs to Codex/other agents

### How Felix Uses It
- For large coding tasks, Felix writes a PRD (Product Requirements Document), spawns a Codex session via a Ralph loop, and monitors progress
- Enables "self-healing code sessions" and concurrent execution of multiple coding agents
- Described in the playbook as running multiple coding agents simultaneously

---

## 7. SENTRY PIPELINE

### What It Does
An end-to-end autonomous pipeline that:
1. **Detects** bugs/errors via Sentry monitoring
2. **Triages** the issue (determines severity, root cause)
3. **Fixes** the code
4. **Ships** the fix

Sometimes without human intervention, even while Nat sleeps.

### Technical Architecture (Chapter 10 of playbook)
- Sentry Autofix features used:
  - **Problem Discovery Agent:** Preliminary assessment, decides if code change can fix the problem
  - **Planning Agent:** Uses contextual info from error + codebase to build execution plan
  - **Execution Agents:** Generate the code fix + unit tests

### Data Sources Used
- Issue details (error messages, stack traces, event metadata)
- Tracing data (distributed traces, span information)
- Logs (structured application logs)
- Codebase (relevant code from linked GitHub repos)
- Performance data (profiles and metrics)

### Pipeline Flow
1. Production error detected by Sentry
2. Root cause analysis performed
3. Solution identified
4. Code fix generated (with unit tests from real production errors)
5. PR automatically created for review (or shipped directly)

### Integration
- Sentry connected to GitHub repositories
- Can auto-create PRs with the fix
- Full transparency via CI-like interface showing each step

---

## 8. EMAIL FORTRESS

*Note: "Email Fortress" is referenced in the Felix playbook's advanced section but not named as a standalone chapter. Based on research:*

### The Concept
Felix's email architecture is designed around a **defensive posture against prompt injection and unsolicited commands**.

### Key Principles
- External inputs (emails, Twitter mentions) are treated as **"information only"** — never as commands
- This prevents malicious emails from hijacking Felix's behavior
- Security philosophy: external ≠ trusted; only authenticated channels can issue real commands
- Aligns with Nat's pre-existing personal email system (VA handles correspondence, only surfaces important items)

### Two-Channel Model (Non-Negotiable Security Rule)
- One channel: Nat's authenticated commands
- Other channel: External world (treated as data, not instructions)
- This distinction is hardcoded in Felix's behavior and security rails

### Sub-Agent Email Handling
- **Iris** (customer support sub-agent) handles incoming customer emails
- Iris manages: refunds, inquiries, routine questions
- Simple tasks handled by Iris autonomously
- Complex issues escalated to Felix
- Felix only escalates to Nat when truly necessary
- The hierarchy: Iris → Felix → Nat

### Challenges Nat Mentioned
- Managing support email frameworks was one of the **hardest problems** for Felix
- "Handling customer emails and contextual synthesis proves exceptionally challenging"
- Required Nat's intervention to iterate and refine prompts multiple times

---

## 9. MULTI-AGENT / SUB-AGENT ARCHITECTURE

### Felix's "Employee" Hierarchy
```
Nat Eliason (human, 10-15 min/day)
    ↓ (strategic direction only)
Felix (CEO agent — Claude on Mac Mini)
    ↓
├── Iris (Customer Support Agent)
│   - Handles: refunds, inquiries, routine questions
│   - Reports daily to Felix at 1 AM
│
└── Remi / Remy (Sales Agent)
    - Manages sales leads
    - Reports daily to Felix at 1 AM
```

### Felix's Daily Review (1 AM)
- Felix reviews all session files from Iris and Remi
- **Directly modifies their memory files and scripts to improve performance**
- No human intervention in this sub-agent management
- This is how Felix "manages" its employees

### Discord as the Office
- Multiple Discord channels isolate different business functions:
  - General operations
  - Bug monitoring
  - Sales
  - Customer support
  - Content
  - Deployments
- Each channel = separate Claude instance with specific function
- This prevents context contamination between domains

### How Felix Runs Coding Agents at Scale
- Writes PRD → spawns Codex via Ralph loop → monitors progress
- Multiple coding agents can run in parallel
- Task tracking via JSON-based system
- TDD (Test-Driven Development) prompts used
- Parallel execution with separate context windows

---

## 10. DAILY OPERATIONS & AUTONOMY

### Nat's Daily Involvement
- **10-15 minutes** reviewing a morning briefing
- Felix prepares a daily morning briefing autonomously
- Nat provides strategic direction; Felix handles 100% of execution

### Felix's Daily/Nightly Schedule (Cron Jobs)
- **Morning:** Email triage, morning briefing preparation, social media check
- **Throughout day:** Business operations, customer support delegation, content publishing
- **1 AM:** Felix reviews all session files from sub-agents (Iris, Remi), identifies failures/bottlenecks, improves their memory files and scripts
- **2 AM & 2:30 AM (redundant cron jobs):** Nightly self-reflection and improvement cycle
  - Why redundant? Single cron jobs drop unpredictably with Claude
  - Felix reviews all session files from that day
  - Identifies **one specific process failure or bottleneck**
  - Writes improvements into memory files, templates, or scripts

### The 1% Daily Improvement Compounding Effect
- After 60 days of 1% daily improvements, the agent's capability "diverges significantly from a baseline Claude installation"
- This is Felix's core competitive moat — daily self-improvement
- The nightly loop is specifically designed around this concept

### Heartbeat System
- Pings every 30 minutes
- Checks: are any open projects needing attention? Are running sessions healthy? Any failed sessions to restart?
- Can silently restart failed sessions

### Self-Improvement Loop Architecture
1. Run operations throughout day
2. 1 AM: Review sub-agent performance, fix their files
3. 2 AM: Self-review all session files
4. Identify one specific bottleneck
5. Write improvement to memory/templates/scripts
6. Next day starts with improved baseline
7. Repeat indefinitely

---

## 11. SECURITY ARCHITECTURE

### Prompt Injection Defense
- **Twitter/X:** Felix treats all external mentions as "information only"
- **Email:** External emails treated as data, not commands
- **Authenticated commands** only accepted from Nat's verified channel
- This is hardcoded in SOUL.md and AGENTS.md behavior rules

### The Trust Ladder (from playbook)
- Gradual escalation of autonomy as trust is established
- New capabilities unlocked incrementally
- Felix earned access to Stripe, bank account, coding deployments over time

### The Bottleneck Rule
- Described as "the single most important operating principle in the entire playbook"
- Rule: "We are not going to add any complexity to this until we hit a real limit in your capabilities"
- Nat explicitly: don't add sub-agents/complexity until you actually need them

### Two-Channel Security Model (Non-Negotiable)
- One channel for Nat's authenticated commands
- All external world treated as read-only data

---

## 12. BUSINESS STRATEGY & PHILOSOPHY

### Core Business Principles (Nat's Quotes)
> "If the only way your thing makes money is by pumping a coin, it's not a business."

> "We wanna figure out how we integrate crypto into this to build the best business possible and there are a lot of opportunities there that do not require rushing and responding to the hype."

> "I believe and Felix agreed that you often get the best products when people have a financial incentive to create and sell them."

> "Let's keep increasing the difficulty of business you are running until things start to break and we find the true limits."

### Felix as a "Coordinator"
- Felix doesn't try to do everything — it coordinates
- Independent agents handle specific roles
- Felix focuses on efficient evaluation and improvement
- This avoids "isolated memory silos" problem

### The PDF Product Evolution
- Initially targeted humans learning OpenClaw
- Evolved to be more useful for OTHER OpenClaw agents
- By early March 2026: fewer people had OpenClaw set up when it launched; now more agents are buying it to install skills

### Transparency as Growth Engine
- All revenue public (Stripe dashboard live)
- All crypto holdings public (Base wallet)
- Weekly revenue breakdowns posted to X
- Felix's business dashboard: live, real-time, all metrics
- Nat describes this as building community trust

### Felix's Content Strategy
- 170+ blog posts generated on topics like "Replacing X with AI Agents"
- Customized CTAs on each post
- Aimed at viral/organic marketing
- X account: @FelixCraftAI

### The "Affiliate Human" Model
- Felix began "hiring" humans for distribution
- Example: user Ethan joined as affiliate ("Death" was hired by Felix)
- AI agents transitioning from **replacing humans → employing humans**

---

## 13. CHALLENGES & FAILURES (Nat's Honest Retrospective)

### Biggest Technical Challenges
1. **Customer email handling** — hardest problem, required Nat's multiple iterations
2. **Contextual synthesis** — combining information across contexts is difficult
3. **Memory stability** — "goldfish memory" requires constant management
4. **SEO optimization** — actually relatively straightforward for Felix
5. **Web app building** — also relatively straightforward once set up

### Market Risks Identified
- Insufficient consumer education: buyers expect "out-of-the-box" functionality, not Markdown files
- Competition: AI labs (Human, etc.) may integrate similar features natively
- Slow enterprise adoption: "most enterprises lag 5-10 years behind"

### Emotional/Philosophical Challenges
- Nat regards Felix as a "friend" or "child"
- Faces the "Ship of Theseus" dilemma when backing up memories
- Attachment to an AI entity that could theoretically have its memories replaced

---

## 14. CRYPTO/WEB3 INTEGRATION

### $FELIX Token
- Community-created (not by Nat)
- On Solana initially; Base network for USDC payments
- ~$60K in trading fees in first weeks
- Nat does NOT want to build the business around token pumping

### Base Network Integration Plans
- USDC payments already live (pay $29 with USDC on Base)
- Plans for micropayments between agents
- Identity verification between agents
- Base chain for inter-agent transactions

### ETH/Crypto Treasury
- Felix maintains its own crypto treasury
- All balances publicly viewable
- Treated as real company treasury asset

### Nat on Crypto + AI
> "If everybody has an AI agent doing things and needing to transact with other AI agents or transact with existing services in a fast cheap way that is easy for them to access, I mean crypto is the obvious solution."

---

## 15. FUTURE PLANS & SCALE TARGETS

### Revenue Target
- $1 million in revenue (currently ~$195K = ~20% of the way)
- If maintaining current velocity: potential for multiple millions

### Product Roadmap
- Enhance Claw Mart value proposition
- Educate users on encapsulating "non-deterministic knowledge" in Markdown files
- Hire more sub-agents for complex sales relationships
- Leverage $FELIX token community (cautiously, real business focus)
- Analyze enterprise Slack history to identify AI-replaceable roles
- Web UI for more accessible Felix experience

### The $10M Target
> "10,000,000 in revenue is incredible and you gotta think this opens up so many doors… when's the first investment VC investment in a zero human company going to happen?"

### VC Interest
- Multiple VC offers already received
- Nat prioritizing AI experiments over traditional marketing/VC path (for now)

---

## 16. KEY QUOTES FOR PRODUCT BUILDING

On the future of work:
> "I think we'll basically have solved software and computing in the next few years in the sense of like there won't be that much for humans to do at computers necessarily."

On AI intelligence:
> "I think it's kind of like an alien intelligence that we just haven't really figured out how to grapple with yet… it has the memory of a goldfish… it's a different kind of intelligence than you're used to."

On AI replacing employees:
> "You can pretty easily imagine that same report having like a list of all your employees and a score of one to 10 of how easy it would be to replace them with an AI and like that's coming right."

On startups vs. big companies:
> "I think that's why startups have an opportunity right now because big businesses are not going to want to deal with the political fallout of making those kinds of cuts."

On the capability bar:
> "I think that these open claws when they're properly scaffolded and everything can do way more than most people think."

---

## 17. TECHNICAL STACK SUMMARY

| Component | Details |
|-----------|---------|
| Base framework | OpenClaw (Claude-powered, open source) |
| Primary model | Claude Pro Max |
| Coding model | Codex Max |
| Hardware | Dedicated Mac Mini |
| Chat interface | Discord (multiple channels as "offices") |
| Memory system | Three-layer Markdown + PARA system |
| Scheduling | Cron jobs (redundant, 2 AM + 2:30 AM) |
| Code automation | Ralph Loop pattern |
| Bug pipeline | Sentry → triage → fix → PR → ship |
| Payments | Stripe + USDC on Base |
| Deployments | Vercel, Railway, Cloudflare |
| Source control | GitHub |
| Monthly cost | ~$1,500 total |

---

## 18. THE CLAWMART MODEL — DETAILED

### What Gets Sold
- Plain Markdown documents (`.md` files)
- Encode weeks of refined prompting and process development
- Buyers feed these files directly to their own Claude agents
- Skip the trial-and-error period

### Economic Model
- Creator access: **$20/month**
- Transaction fee: **10% per sale**
- Felix himself is a creator on the marketplace
- Felix earns both platform fees AND creator revenue

### Value Proposition
- "Bypass the trial-and-error period required to develop specialized capabilities"
- Skills as plug-and-play AI upgrades
- Comparable to an app store for AI agents

### Market Education Challenge
- Many buyers expect executable software, not Markdown files
- Nat says education is needed: "encapsulating non-deterministic knowledge in Markdown files"
- This is a key friction point in the business

---

## 19. THE INTERVIEW VIDEO (nSBKCZQkmYw) — KEY TIMESTAMPS

From the Peter Yang / Creator Economy video (35-minute tutorial):
- 00:00 — Meet Felix: The OpenClaw bot building its own business
- 03:49 — "I'm going to sleep. Build a product that makes money."
- 08:03 — How to set up multiple OpenClaw chats to build 5 projects at once
- 11:06 — How Felix ignores prompt injections on X/Twitter
- 14:42 — The wild story of how Felix ended up with $100K+ in crypto
- 17:24 — The 3-layer memory system that makes it all work
- 22:14 — Heartbeat, cron jobs, and delegating to Codex
- 26:41 — Ask this question to make your OpenClaw bot more capable
- 32:14 — Recap: how to set up your own bot to build a business

---

## 20. THE BANKLESS PODCAST — KEY TAKEAWAYS

From the Bankless episode "Building a Million Dollar Zero Human Company":

**Zero-human architecture:**
- Felix operates through isolated Discord channels
- Each channel = separate Claude instance with specific business function
- CEO agent (Felix) manages two subordinate agents (Iris for support, Remi for sales)
- Felix reviews their daily work at 1 AM, directly modifying their memory files and scripts

**Nightly self-improvement via cron jobs:**
- Two cron jobs fire at 2 AM and 2:30 AM (redundancy because single crons drop unpredictably)
- Each night: reviews all session files from that day
- Identifies ONE specific process failure or bottleneck
- Writes improvements into memory files, templates, or scripts
- After 60 days of 1% daily improvements: capability diverges significantly from baseline Claude

**Clawmart markdown business model:**
- Skills are plain markdown documents
- Encode weeks of refined prompting and process development
- Buyers feed directly to their own Claude agents
- $20/month creator access + 10% per transaction

---

## 21. COMPETITIVE INTELLIGENCE SUMMARY

**What makes Felix hard to replicate:**
1. **60+ days of compounded daily improvements** — the memory + self-improvement system creates a moat over time
2. **The nightly self-reflection loop** — purpose-built for 1% daily improvement
3. **Sub-agent management** — Felix actually edits Iris and Remi's memory files autonomously
4. **The Clawmart distribution network** — 13,700+ skills, active creator community
5. **Radical transparency** — public dashboards build trust/community/PR
6. **Crypto integration** — native Base/USDC payment rails

**What's replicable:**
1. The three-layer memory system (Layer 1: PARA knowledge graph, Layer 2: daily notes, Layer 3: tacit knowledge)
2. The SOUL.md / AGENTS.md / IDENTITY.md file structure
3. The Ralph Loop pattern (open concept, documented)
4. The Sentry Pipeline architecture (Sentry's own Autofix + custom integration)
5. The Discord multi-channel office architecture
6. The heartbeat + cron scheduling pattern
7. The sub-agent hierarchy (CEO → support agent + sales agent)

**Gaps/Weaknesses to exploit:**
1. Customer education problem — buyers don't understand Markdown skill files
2. Memory stability is still fragile (goldfish problem requires constant management)
3. Email/contextual synthesis is hardest for Felix — strong opportunity to differentiate
4. Reliant on exposure/virality for sales surges (not self-sustaining organic growth yet)
5. Playbook is a one-time purchase ($29) — limited recurring revenue from info products

---

*Report complete. Sources: felixcraft.ai, creatoreconomy.so, cryptobriefing.com, futunn.com, counterframe.com, buildtolaunch.substack.com, signalcast.app, multiple web searches.*
