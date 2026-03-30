# Official Docs + ClawHub Research

**Research date:** 2026-03-18  
**Sources:** docs.openclaw.ai, openclaw.ai, clawhub.ai, community showcase, installed workspace skills

---

## What Is OpenClaw (Positioning Summary)

OpenClaw is a **self-hosted AI gateway** that connects messaging apps (WhatsApp, Telegram, Discord, iMessage, Slack, Signal, IRC, Matrix, LINE, Nostr, Twitch, etc.) to AI coding agents (Pi, Claude Code, Codex, Cursor, etc.). It runs on your own machine or server.

**Core differentiators (from official channels):**
- Self-hosted = data stays local, no walled garden
- Multi-channel: one Gateway serves all messaging platforms simultaneously
- Agent-native: tool use, sessions, persistent memory, multi-agent routing
- Extensible via Skills (AgentSkills spec) and Plugins
- MIT licensed, open source, community-driven
- "Personal AI assistant" — but users call it "company assistant, family tool, team tool"

**Official tagline:** *"The AI that actually does things."*

---

## Use Case Taxonomy

### Category 1: Personal Productivity
- **Daily briefings:** Morning summary of calendar, weather, tasks, favorite articles — sent via chat
- **Email management:** Read, search, send, unsubscribe, triage inbox from phone
- **Calendar management:** Check events, create meetings, check availability, reminders (Google Calendar, CalDAV)
- **Task management:** Todoist integration — add, manage, complete tasks via chat
- **Reminders + scheduling:** Cron-based reminders, traffic-aware departure alerts (e.g., "remind me when to leave for pickleball based on traffic")
- **Persistent memory / second brain:** Ingests conversations, builds knowledge base, remembers context 24/7 across sessions
- **Health tracking:** Integrates Oura ring, WHOOP data; biomarker summaries, gym schedule coordination
- **Language learning:** Chinese (xuezh), vocabulary drills, pronunciation feedback via voice
- **Custom meditations:** Write + TTS + ambient audio = personalized meditation sessions
- **Personal journaling / knowledge graph:** WhatsApp exports → transcription → cross-linked markdown

### Category 2: Business Automation
- **Accounting intake:** Collect PDFs from email, prep for tax consultant — monthly autopilot
- **Job search agent:** Search listings, match against CV keywords, return opportunities (JSearch API)
- **Legal/insurance negotiation:** Draft and send formal email challenges to insurance rejections
- **Health reimbursements:** Submit health claims with documents
- **Virtual assistant replacement:** "No more need to pay a VA" (community sentiment)
- **Company operations:** "It's running my company" — multi-agent setups delegating tasks
- **Content pipelines:** Design, code review, taxes, PM, content — all via chat
- **Slack auto-support:** Watch Slack channel, respond helpfully, forward to Telegram, fix production bugs autonomously
- **Jira integration:** Connect to Jira, generate skills on the fly, manage issues
- **Linear CLI:** Manage issues, projects, workflows from terminal — integrates with agentic workflows
- **Social media scheduling (Postiz):** Schedule to 28+ channels (X, LinkedIn, Instagram, TikTok, Discord, Slack, Reddit, etc.)

### Category 3: Developer Tools
- **Autonomous coding loops:** "fix tests" via Telegram → runs loop, sends progress every 5 iterations
- **PR creation and review:** Code change → open PR → OpenClaw reviews diff → replies with verdict in Telegram
- **Claude Code / Codex session management:** Kick off coding sessions from phone while on a walk
- **Spec file generation:** Create detailed spec files remotely via phone
- **Error resolution via Sentry webhook:** Captures errors → resolves them → opens PRs
- **Screenshot-to-Markdown (SNAG):** Hotkey region → Gemini vision → clipboard Markdown
- **CodexMonitor:** List/inspect/watch local Codex sessions (CLI + VS Code)
- **iOS app deployment via chat:** Built complete iOS app, deployed to TestFlight — entirely via Telegram
- **Website building from phone:** Full site migrations, DNS, CMS moves without opening a laptop
- **API key provisioning:** Agent opens browser, navigates GCP Console, configures OAuth, provisions token
- **Code review (skill):** AI-powered bug/security/improvement analysis
- **Test generation:** Unit tests from code (Jest, pytest, Vitest)
- **Commit message writing:** Conventional commits from diffs
- **Changelog generation:** Categorized changelogs from git diff or bullet points
- **API doc generation:** OpenAPI, markdown, README from code/endpoints
- **Architecture diagram generation:** Mermaid, C4, deployment views, ADRs from plain English
- **MCP server scaffolding:** TypeScript/Python boilerplate with tools, resources, Claude Desktop integration
- **Git manager:** Advanced workflows, branches, PRs, conflicts, automation
- **Database schema design:** SQL schemas, ER diagrams, migration files

### Category 4: Home Automation & IoT
- **Home Assistant integration:** Control smart home devices (lights, thermostats, locks, cameras, scenes) via natural language; also as HA Add-on
- **Air quality management:** Winix air purifier control based on biomarker goals
- **Robot vacuum control:** Roborock via natural conversation
- **3D printer control:** BambuLab — status, jobs, camera, AMS, calibration
- **Camera automation:** Snap photos when conditions met (pretty sky, motion triggers)
- **Home automation orchestration (GoHome):** Nix-native with Grafana dashboards
- **NAS storage:** Turn machine into network-attached storage
- **WireGuard VPN:** Personal VPN server setup
- **Pi-hole / adblock DNS:** Network-wide ad blocking
- **Remote PC control:** Turn off PC remotely via Telegram

### Category 5: Social Media & Content
- **Social media post creation:** Twitter/X, LinkedIn, Instagram — platform-specific with hooks and hashtags
- **Blog/article generation:** SEO-optimized, brand-voice-matched, with internal linking
- **Content engine:** Research → SEO blog → social promotion pipeline
- **X (Twitter) algorithm optimization:** Viral strategies, reach maximization
- **Postiz integration:** Schedule/publish to 28+ platforms
- **Brand voice analysis:** Extract tone, vocabulary, style rules
- **Copywriting:** Headlines, CTAs, landing pages, email sequences
- **SEO meta generation:** Titles, descriptions, OG tags, JSON-LD structured data
- **YouTube video → reusable agent skills:** Turn "cool ideas" into workflows

### Category 6: Data, Research & Knowledge
- **Web research + summarization:** Fetch, analyze, synthesize from URLs
- **Brave Search / Perplexity integration:** Web-grounded answers
- **Firecrawl:** Deep web crawling for research
- **TradingView analysis:** Login via browser, screenshot charts, technical analysis
- **Stock lookup:** Real-time quotes, company info, market data
- **Crypto prices:** CoinGecko real-time data
- **Country info:** Population, languages, currencies, capital via REST Countries API
- **Space tracking:** ISS location, who's in space, NASA APOD
- **IP lookup:** Geolocation, ISP, network info
- **Domain WHOIS:** Registration info, expiry dates
- **Random facts / dictionary / recipe finder:** Quick lookup utilities
- **Karakeep semantic search:** Vector search over bookmarks (Qdrant + embeddings)
- **RAG over internal docs:** "Processed entire source of truth via WhatsApp in minutes, where RAG agents struggled for days"

### Category 7: Communication & Messaging
- **Multi-channel gateway:** WhatsApp, Telegram, Discord, iMessage, Signal, Slack, Matrix, IRC, LINE, Nostr, Twitch, Feishu, Mattermost, Microsoft Teams, Nextcloud Talk, Google Chat, Zalo, Tlon
- **Group chat management:** Selective response, mention-gating, broadcast groups
- **Email automation:** Send, receive, search via IMAP/SMTP
- **Voice calls:** Phone bridge (Vapi), ElevenLabs TTS voice calls (custom accents)
- **Telegram voice notes:** TTS → sent as Telegram voice notes (papla.media)
- **Beeper CLI:** Read/send/archive via Beeper Desktop (iMessage, WhatsApp unified)
- **Proactive heartbeats:** Agent checks in proactively during idle periods

### Category 8: Media & Entertainment
- **Spotify player control:** Playback, queues, recommendations
- **Plex media server:** Stream movies, TV shows, music
- **Video downloader:** YouTube, Instagram, TikTok, 1000+ sites
- **Image generation:** Built-in via model providers
- **Sora video generation:** Full workflow including watermark removal
- **Audio transcription:** Multi-lingual via OpenRouter (Gemini, etc.)
- **TTS + custom meditations:** Combine voice, ambient audio, generated text
- **Morning briefing scene image:** Daily generated image with weather + tasks + quotes

### Category 9: Infrastructure & Deployment
- **Self-hosting on Raspberry Pi, Mac, Linux, Windows (WSL2)**
- **Cloud deployment:** Fly.io, Hetzner, GCP, DigitalOcean, Oracle Cloud, Railway, Render, Northflank
- **Docker / Podman / Kubernetes support**
- **Nix packaging:** Reproducible deployments
- **Multiple gateways:** Run separate instances
- **Tailscale integration:** Secure remote access
- **SSH management:** Connections, keys, tunnels
- **Docker management:** Containers, images, compose stacks
- **Ansible automation:** Infrastructure as code
- **System monitoring:** CPU, RAM, disk, network, processes, temperatures
- **Cron scheduling:** Precise task automation
- **Webhook ingestion:** External event triggers (Sentry, etc.)
- **Backup manager:** Files, databases, configurations
- **Health check + security hardening**

### Category 10: AI / Agent Orchestration
- **Multi-agent routing:** Isolated sessions per agent, workspace, or sender
- **14+ agent setups:** Opus orchestrator delegating to Codex workers
- **Sub-agent spawning:** Parallel task execution
- **Hive mind / SAMURAI / Ruflo swarms:** Dynamic multi-agent orchestration
- **ACP agents:** Agent Communication Protocol
- **Memory persistence:** Cross-session, cross-channel context
- **Skill self-creation:** Agent builds new skills when needed
- **Model failover:** Automatic fallback across providers
- **Multi-provider support:** Anthropic, OpenAI, Ollama (local), MiniMax, Mistral, Gemini, GitHub Copilot, LiteLLM, OpenRouter, Venice AI, Together AI, NVIDIA, Hugging Face, Qwen, Moonshot, and more
- **Sandbox isolation:** Docker-based sandboxing for untrusted agents

### Category 11: Shopping & Lifestyle
- **Grocery autopilot (Tesco):** Weekly meal plan → book delivery slot → confirm order (browser automation)
- **School meal booking (ParentPay):** UK school meal automation
- **Flight search CLI:** Multi-provider terminal flight search
- **Padel court booking:** Playtomic availability checker + booking
- **Sports scheduling:** Traffic-aware reminders for activities
- **Wine cellar management:** CSV-based personal inventory skill

### Category 12: Learning & Education
- **Language learning:** Any language via conversation, drills, grammar, flashcards
- **University course access:** Build skill for course/assignment access
- **Technical interview prep:** Role-targeted Q&A
- **Coding principles:** SOLID, DRY, KISS, design patterns tutoring
- **Student vibe coding support:** Teaching tool for educators

---

## Skills Installed in This Workspace (Inventory)

**Developer Tools:** api-doc-generator, api-mock-generator, architecture-diagram-generator, changelog-generator, code-reviewer, coding-principles, commit-writer, database-schema-designer, frontend-design, git-manager, mcp-server-scaffolder, pr-review, regex-generator, shadcn-ui, sql-generator, test-generator  

**Content & Marketing:** blog-agent, brand-voice-analyzer, content-engine, copymaster (copywriting-mastery), email-sequence-writer, landing-page-copy, postiz, prompt-engineer, seo-meta-generator, social-media-post, storymaster, superdesign, x-algorithm  

**Productivity:** cron-builder, cron-scheduler, google-calendar, gog (Google Workspace), meeting-summarizer, notion-manager, resume-reviewer, timezone-converter, translator  

**Data & Research:** competitor-analysis, country-info, crypto-prices, dictionary, domain-whois, ip-lookup, random-facts, recipe-finder, space-tracker, startup-idea-validator, stock-lookup  

**Communication & Media:** email-manager, spotify-player, video-downloader  

**Home & Infrastructure:** adblock-dns, backup-manager, docker-manager, home-assistant, nas-storage, pihole, plex-media-server, ssh-manager, system-monitor, wireguard-vpn  

**AI Orchestration:** hive-mind, ruflo, samurai  

**Utilities:** camoufox-browser, clip-extractor, color-palette, dating, language-learning, legal-summarizer, privacy-policy-generator, qr-generator, technical-interview-prep, url-shortener  

**Total installed skills: ~80+**

---

## Skills on ClawHub (Community Published)

ClawHub launched recently; notable community-published skills found:
- **homeassistant** — Home Assistant control via natural language
- **caldav-calendar** — Self-hosted calendar (khal/vdirsyncer)
- **r2-upload** — Cloudflare R2/S3 upload + presigned URLs
- **bambu-cli** — BambuLab 3D printer control
- **wienerlinien** — Vienna public transport real-time
- **openrouter-transcribe** — Multi-lingual audio transcription
- **codexmonitor** — Codex session inspector (brew)
- **linear-cli** — Linear issue management CLI

*Note: ClawHub is still early — "No highlighted skills yet / No skills yet. Be the first." Marketplace is in growth phase.*

---

## Key Messaging from Official Channels

| Theme | Quote / Angle |
|-------|--------------|
| Self-hosted control | "Your context and skills live on YOUR computer, not a walled garden" |
| AGI feeling | "Using it for a week genuinely feels like early AGI" |
| Replaces Siri | "Everything Siri was supposed to be. And it goes so much further." |
| Replaces VAs | "No more need to pay a virtual assistant" |
| Company OS | "It's running my company" |
| Platform killer | "Will actually be the thing that nukes a ton of startups, not ChatGPT" |
| Personal OS | "All apps, interfaces, walled gardens — gone" |
| Self-hackable | "Self-hackable — it builds upon itself just by talking to it" |
| Proactive | "Proactive AF: cron jobs, reminders, background tasks. Memory is amazing, context persists 24/7" |
| Multi-role | "Personal AI assistant undersells it — it's a company assistant, family assistant, team tool" |

---

## Underserved Use Cases (Gaps / Opportunities)

Based on analysis of installed skills vs. community demand:

### High-Signal Gaps (people doing it manually, no packaged skill):
1. **Finance / budgeting automation** — No personal finance skill (bank statement analysis, expense tracking, budget alerts)
2. **Travel planning** — Flight search CLI exists but no full travel agent skill (hotels, itineraries, visa info)
3. **CRM / sales pipeline** — Jira/Linear covered, but no HubSpot/Pipedrive/Airtable CRM skill
4. **Medical / health records** — Oura/WHOOP integration exists, but no doctor appointment booking, medical record parsing
5. **News digest / RSS aggregation** — RSS parsing mentioned in tweets, but no polished skill
6. **Smart TV / media center control** — Plex exists, but no Kodi/Jellyfin/Apple TV remote control skill
7. **NFT / blockchain / Web3** — Crypto prices skill exists, but no wallet monitoring, DeFi dashboards
8. **Family coordination** — "Family assistant" mentioned in positioning, but no dedicated family calendar / chore management skill
9. **Car / EV integration** — No Tesla API, OBD2, or vehicle telemetry skill
10. **E-commerce management** — No Shopify/WooCommerce admin skill
11. **HR / recruitment automation** — Job search exists, but no applicant tracking, resume screening
12. **Academic research** — No arXiv/PubMed search, citation manager, paper summarizer
13. **Gaming integration** — No Steam, Discord game status, achievement tracking
14. **Photo management** — Camera capture exists, but no Google Photos, iCloud, or album organization skill
15. **Fitness tracking beyond wearables** — No workout logging, gym routine management, nutrition tracking

### Infrastructure Gaps:
- **Kubernetes / cloud cost monitoring** — Docker managed, but no K8s dashboards or cloud spend alerts
- **Database querying** — SQL generator exists but no live DB connection skill (Postgres, MySQL, MongoDB)
- **Analytics dashboards** — No Google Analytics, Plausible, or Mixpanel integration

---

## Summary Statistics

| Dimension | Count |
|-----------|-------|
| Supported chat channels | 20+ |
| Supported AI model providers | 25+ |
| Workspace skills installed (this system) | ~80 |
| Deployment platforms documented | 15+ |
| Use case categories identified | 12 |
| Community showcase projects | 30+ |
| ClawHub published skills (early marketplace) | ~8 confirmed |

---

*Research compiled by SAMURAI docs-agent for run 0318-0916-ea5a*
