# HackerNews + Community Research Findings

> **Note:** Web search (Brave API) was unavailable during this run — no API key configured.
> HackerNews and dev.to/medium searches could not be executed.
> All use cases below sourced from **docs.openclaw.ai/start/showcase** (official community showcase)
> and **docs.openclaw.ai** (official docs). These are real community-submitted projects.

---

## Use Cases Found

### PR Review → Telegram Feedback — Insanity: 9/10
**What:** OpenCode finishes a code change → opens a PR → OpenClaw automatically reviews the diff and replies in Telegram with "minor suggestions" + a clear merge verdict (including critical fixes to apply first). Full CI-to-pocket feedback loop, no dashboard needed.
**Source:** https://x.com/i/status/2010878524543131691 (by @bangnokia)
**Ampere angle:** Full dev cycle in your pocket — code, review, merge verdict, all via chat. This is what GitHub Copilot wishes it was.

---

### Kev's Dream Team — 14+ Orchestrated Agents — Insanity: 10/10
**What:** 14+ specialized agents running under one OpenClaw gateway. Opus 4.5 orchestrator delegates to Codex workers. Custom sandboxing via Clawdspace, webhook triggers, heartbeats, full delegation flows. Comes with a comprehensive technical write-up and blog post.
**Source:** https://github.com/adam91holt/orchestrated-ai-articles | https://adams-ai-journey.ghost.io/2026-the-year-of-the-orchestrator/
**Ampere angle:** A solo dev built a multi-agent enterprise AI system on a self-hosted stack. This is the "year of the orchestrator" in practice.

---

### Couch Potato Dev Mode — Insanity: 9/10
**What:** @davekiss rebuilt his entire personal website via Telegram while watching Netflix. Never opened a laptop. Migrated 18 blog posts from Notion → Astro, switched DNS to Cloudflare. Complete website migration from couch.
**Source:** https://davekiss.com
**Ampere angle:** "I deployed a website without touching a computer." The ultimate lazy dev flex. Great viral angle.

---

### iOS App via Telegram — Insanity: 9/10
**What:** @coard built a complete iOS app with maps and voice recording, deployed it to TestFlight — entirely via Telegram chat. No IDE opened directly.
**Source:** Community Discord showcase
**Ampere angle:** Ship an app to TestFlight from your phone. No Mac required. This breaks people's brains.

---

### Tesco Shop Autopilot — Insanity: 8/10
**What:** @marchattonhere built a fully automated weekly grocery workflow: weekly meal plan → generates regular items list → books delivery slot → confirms order. No APIs needed — pure browser automation.
**Source:** https://x.com/i/status/2009724862470689131
**Ampere angle:** Your AI does your weekly shop. Not a concept demo — real groceries, real delivery booking, runs weekly.

---

### Slack Auto-Support (with Autonomous Bug Fix) — Insanity: 9/10
**What:** @henrymascot's setup watches a company Slack support channel, responds helpfully to users, forwards notifications to Telegram — AND autonomously fixed a production bug in a deployed app *without being asked*. Self-directed production repair.
**Source:** Community Discord showcase
**Ampere angle:** It fixed a production bug nobody asked it to fix. The "autonomous employee" moment that makes CTOs nervous.

---

### WhatsApp Memory Vault — Insanity: 8/10
**What:** Ingests full WhatsApp chat exports, transcribes 1,000+ voice notes, cross-references with git logs, outputs linked markdown reports. Turns years of personal messaging history into a searchable knowledge base.
**Source:** Community Discord showcase
**Ampere angle:** Your entire messaging history, transcribed and indexed. Recall any conversation or decision from 3 years ago instantly.

---

### TradingView Technical Analysis (No API) — Insanity: 8/10
**What:** @bheem1798 built a workflow that logs into TradingView via browser automation, screenshots charts, and performs technical analysis on demand. Zero official API needed — just browser control.
**Source:** Community Discord showcase
**Ampere angle:** Automated trading analysis that works on any site, bypasses API paywalls, delivers insights to your phone.

---

### Oura Ring Health Assistant — Insanity: 8/10
**What:** @AS integrated Oura ring biometric data with calendar, appointments, and gym schedule into a personal AI health assistant. Holistic health + schedule awareness in one agent.
**Source:** Community Discord showcase
**Ampere angle:** Your AI knows you slept 4 hours and proactively reschedules your 7am gym session. Real personalized health intelligence.

---

### Inside-Out-2 Memory System — Insanity: 9/10
**What:** A separate memory manager that converts raw session files → memories → beliefs → evolving self-model. The agent literally builds a theory of itself over time, like the Pixar movie's memory islands.
**Source:** Community Discord showcase
**Ampere angle:** An AI that doesn't just remember what you did — it develops beliefs and a self-model. This is genuinely next-level agent architecture.

---

### Bambu 3D Printer Control — Insanity: 7/10
**What:** @tobiasbischoff built an OpenClaw skill to control and troubleshoot BambuLab 3D printers: status, print jobs, camera feed, AMS filament management, calibration — all via natural language chat.
**Source:** https://clawhub.com/tobiasbischoff/bambu-cli
**Ampere angle:** "Pause my print and check the camera" from your phone while in bed. Hardware control via chat.

---

### Winix Air Purifier Control — Insanity: 7/10
**What:** @antonplex had Claude Code discover and confirm the purifier API/controls, then handed it off to OpenClaw for ongoing air quality management. Claude Code as R&D, OpenClaw as ops.
**Source:** https://x.com/antonplex/status/2010518442471006253
**Ampere angle:** Two-phase automation: one agent discovers how a device works, another runs it forever. Template for any undocumented IoT device.

---

### Clawdia Phone Bridge (Real-Time Voice Calls) — Insanity: 8/10
**What:** @alejandroOPI built a Vapi voice assistant ↔ OpenClaw HTTP bridge. Near real-time phone call conversations with your agent. Call your AI like a person.
**Source:** https://github.com/alejandroOPI/clawdia-bridge
**Ampere angle:** Dial your AI assistant on the phone. "Hey Clawdia, what's on my calendar?" — spoken, answered, done.

---

### Wine Cellar Skill (Built in Minutes) — Insanity: 7/10
**What:** @prades_maxime asked OpenClaw to build a local wine cellar management skill. It requested a sample CSV export, chose a storage location, built and tested the skill — handling 962 bottles — fast.
**Source:** https://x.com/i/status/2010916352454791216
**Ampere angle:** Asked for a niche skill, got a production-ready tool in minutes. Shows the self-extensibility angle — the agent builds its own tools.

---

### Padel Court Auto-Booking — Insanity: 7/10
**What:** @joshp123 built a Playtomic availability checker + auto-booking CLI. Never misses an open court slot.
**Source:** https://github.com/joshp123/padel-cli
**Ampere angle:** "Book me a court whenever one opens Saturday morning" — set and forget reservation automation.

---

### Accounting Intake on Autopilot — Insanity: 8/10
**What:** Community member automated monthly accounting: collects PDF invoices from email, preps documents for tax consultant. Monthly accounting workflow runs completely unattended.
**Source:** Community Discord showcase
**Ampere angle:** The accountant gets prepped documents without the human doing anything. Small business ops on autopilot.

---

### GoHome + Roborock (Full Home Automation) — Insanity: 7/10
**What:** @joshp123 built Nix-native home automation with OpenClaw as the conversation interface, Grafana dashboards for visualization, and Roborock vacuum control via natural language.
**Source:** https://github.com/joshp123/gohome
**Ampere angle:** Full self-hosted smart home controlled by chat, with beautiful monitoring dashboards. No Alexa, no Google, no cloud dependency.

---

### SNAG Screenshot-to-Markdown — Insanity: 7/10
**What:** @am-will built a hotkey tool: select a screen region → Gemini vision analyzes it → instant Markdown text in clipboard. Turns any screen content into structured text.
**Source:** https://github.com/am-will/snag
**Ampere angle:** Screenshot any diagram, table, or UI → instantly get clean Markdown. Dev productivity multiplier.

---

### ParentPay School Meal Booking — Insanity: 7/10
**What:** @George5562 automated UK school meal booking via ParentPay website. Uses precise mouse coordinates for reliable table cell clicking — browser automation for a site with no API.
**Source:** Community Discord showcase
**Ampere angle:** Relatable parent pain point. No API? Doesn't matter — browser automation handles it. Great "AI does my admin" narrative.

---

### Visual Morning Briefing (Scene Images) — Insanity: 7/10
**What:** @buddyhadry's scheduled workflow generates a single "scene" image each morning containing weather, tasks, date, and a favorite quote/post — delivered via Telegram from an OpenClaw persona.
**Source:** https://x.com/buddyhadry/status/2010005331925954739
**Ampere angle:** Wake up to a custom AI-generated visual briefing. Not just text — an actual illustrated scene of your day.

---

### xuezh Chinese Learning Engine — Insanity: 6/10
**What:** @joshp123 built a Chinese language learning skill with pronunciation feedback, vocabulary drilling, and study flows — all accessible via OpenClaw voice/chat.
**Source:** https://github.com/joshp123/xuezh
**Ampere angle:** Personal language tutor in your pocket, integrated with your agent. Remembers your progress session to session.

---

### Home Assistant Add-on (HAOS Native) — Insanity: 7/10
**What:** @ngutman packaged OpenClaw as a Home Assistant OS add-on with SSH tunnel support and persistent state. Runs natively on HAOS alongside smart home automation.
**Source:** https://github.com/ngutman/openclaw-ha-addon
**Ampere angle:** One-click install on Home Assistant OS. For the massive HA community — huge distribution channel.

---

### Job Search Agent (30-Minute Build) — Insanity: 6/10
**What:** @attol8 built an agent that searches job listings, matches them against CV keywords, and returns relevant opportunities with links — built in 30 minutes using JSearch API.
**Source:** Community Discord showcase
**Ampere angle:** 30-minute build → personal recruiter running 24/7. Speed-of-build story is compelling for developers.

---

### Pretty Sky Camera Trigger — Insanity: 6/10
**What:** @signalgaining asked OpenClaw to snap a photo whenever the sky "looks pretty" via a roof camera. OpenClaw designed a skill and took the shot automatically.
**Source:** https://x.com/signalgaining/status/2010523120604746151
**Ampere angle:** Subjective judgment trigger: "take a photo when it looks good." AI aesthetic decision-making for IoT cameras.

---

## What the Community Says OpenClaw is Best For

Based on all use cases, recurring themes emerge:

1. **"AI that runs your life from your phone"** — The dominant theme. Grocery shopping, school meals, padel bookings, accounting, website migrations — all triggered by chat, no laptop needed.

2. **Browser automation as the universal API** — No official API? Doesn't matter. Multiple users automate sites (TradingView, Tesco, ParentPay) via headless browser control. This pattern recurs constantly.

3. **Self-building tools** — Users ask OpenClaw to build skills for itself (wine cellar, Jira, Todoist). The meta-capability of an agent that extends its own toolset is uniquely compelling.

4. **Multi-agent orchestration** — Power users are spinning up 10-14 specialized agents under one gateway. The orchestrator pattern is emerging as the "advanced user" ceiling.

5. **Hardware + IoT control** — Air purifiers, 3D printers, robot vacuums, smart home devices. The "natural language as the universal remote" concept resonates strongly.

6. **Personal memory and continuity** — WhatsApp vault, Oura health data, Inside-Out memory systems. People want an AI that knows their life history deeply.

7. **Dev workflow integration** — PR reviews to Telegram, iOS apps from Telegram, Jira/Linear integration. Developers using OpenClaw to stay in flow state across devices.

---

## Emerging Use Cases (things people WANT but don't have yet)

These represent marketing / product opportunities for Ampere:

1. **Personal CRM via chat** — "Remember I met John at the conference, he mentioned X" — nobody has built a proper AI-powered personal relationship manager skill yet.

2. **Family dashboard agent** — Combining school schedules, meal planning, grocery ordering, and children's activities into a single family-facing agent. ParentPay is a hint of this.

3. **Medical/health protocol automation** — Beyond Oura ring; integrating CGM data, medication reminders, symptom logging. High-value, underserved.

4. **Financial monitoring without APIs** — Like TradingView but for banking portals (Monzo, bank statements, investment dashboards). Browser-based financial intelligence.

5. **Social media autopilot** — Fully autonomous social presence: schedule, post, reply to DMs, track analytics — all orchestrated from OpenClaw. No one's built this end-to-end yet.

6. **Business SOP executor** — Upload your company SOPs, have the agent autonomously execute them (onboarding checklists, client reporting, invoice follow-ups). The Accounting Intake use case hints at this.

7. **Voice-first everything** — Clawdia phone bridge exists, but no one's built the "daily driver voice assistant" that replaces Siri/Google Assistant completely, with full memory and tool use.

8. **Kubernetes / DevOps ChatOps** — The Linear CLI and Jira skill hint at it, but a full DevOps orchestrator (deploy, rollback, monitor, alert) via chat doesn't exist in the showcase yet.

9. **Real estate / rental automation** — Scraping listings, scheduling viewings, drafting applications, tracking leads. High-friction process perfect for browser automation.

10. **AI-powered parenting assistant** — Combining school calendar, meal planning, homework help, activity booking. The ParentPay use case is a seed here.

---

## YouTube Demos Found

- **"OpenClaw: The self-hosted AI that Siri should have been (Full setup)"** by VelvetShark (28 min)
  - https://www.youtube.com/watch?v=SaWSPZoPX34
- **OpenClaw showcase video**
  - https://www.youtube.com/watch?v=mMSKQvlmFuQ
- **OpenClaw community showcase**
  - https://www.youtube.com/watch?v=5kkIJNUGFho

---

## Key Quote (from VelvetShark video title)
> "The self-hosted AI that Siri should have been"

This encapsulates the community's positioning perfectly. OpenClaw isn't competing with ChatGPT — it's the thing Apple/Google promised but never delivered: a personal AI that actually *does things*.

---

*Research by: hn-community-agent | SAMURAI run 0318-0916-ea5a | 2026-03-18*
*Sources: docs.openclaw.ai/start/showcase, docs.openclaw.ai (llms.txt index), docs.openclaw.ai/concepts/features*
*Note: web_search unavailable (no Brave API key) — HackerNews/dev.to/Medium searches not executed*
