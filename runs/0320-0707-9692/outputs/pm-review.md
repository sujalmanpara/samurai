# PM Review — Creator Program Aggregator MVP
**Reviewer Role:** Product Manager  
**Date:** 2026-03-20  
**Spec Reviewed:** FINAL-MVP-SPEC-v2.md  
**Pain Points Cross-Referenced:** step3-creator-pain-points.md

---

## Executive Summary

The spec is solid and shows good product thinking. The core idea is well-scoped and the data model is thorough. However, the MVP is **moderately oversized** — it has ~35 features where ~22 would suffice. The timeline is **optimistic by 20-30%**. The data collection plan is the biggest risk: 150+ programs is a massive underestimate of effort. Several pain points are only partially addressed. Here's the detailed breakdown.

---

## 1. Feature Scope

### MVP is too big — cut these without losing core value

**Cut or defer to V2:**

1. **Feed tabs (Trending / Top Rated / Hidden Gems)** — These require meaningful vote data to be useful. At launch with 0 users, "Trending" will be empty and "Top Rated" will be random. Showing empty/gamed tabs destroys trust. **Cut to V1.5 when you have real vote data.**

2. **"What Creators Say" quotes (50-100 of them)** — Nice touch but 3 hours of curation time for a feature that users barely read. Keep 5-10 hand-picked quotes on the homepage. Cut the per-program quotes inside modals for MVP. **That's 2.5 hours saved.**

3. **Contributor credits on community-added programs** — Zero users at launch. No one will submit programs for weeks. This adds complexity with no day-1 payoff. **Keep the submit form, cut the credit display.**

4. **Content type filter** (Video/Photo/Design/Writing/Music/Code/3D) — This overlaps heavily with Category filter. Do you really need both? A "Music & Audio" category + a "Music" content type filter is redundant. **Merge into tags, cut standalone filter.**

5. **Sort by "Highest Payout"** — Payout data is inconsistent ("Early access + paid opportunities" vs "$500 per Pin"). Sorting incomparable strings is useless or misleading. **Cut this sort option; keep Newest, Alphabetical, Popular.**

6. **JSON-LD structured data for all 150+ programs** — Technically good for SEO long-term, but at launch you'll have zero domain authority. This is 1-2 hours of work with 0 return in the first 3 months. **Do it for the homepage and 5 flagship programs only.**

7. **About page (full story page)** — A simple paragraph on the homepage footer is fine for MVP. Don't spend an hour building a full page nobody reads on day 1. **1 paragraph in footer, full page in V1.5.**

**What's missing that IS critical:**

1. **Empty state design** — What does a user see when search returns 0 results? Or a filter combination returns nothing? Needs explicit handling or users think the site is broken.

2. **Error state for broken external links** — When a creator clicks "Apply" and the link is dead, you have zero handling. This is your primary UX trust point. Need a fallback message: "This link may be outdated — please report it."

3. **Mobile filter UX** — Spec says "bottom sheet on mobile" but this is a non-trivial UI component. Budget 1-1.5 extra hours or use a simpler approach (collapsible accordion) for MVP.

4. **Loading states** — Fuse.js is client-side but 150+ programs with images will have loading lag. Need skeleton cards or a loading indicator, or first-load feels broken.

---

## 2. User Story Audit

Mapping each feature to a user need:

| Feature | User Story | Gap? |
|---|---|---|
| Search | "I know a program name, find it fast" | ✅ Clear |
| Category filters | "I'm a photographer, show me relevant programs" | ✅ Clear |
| Status filter | "I don't want to apply to closed programs" | ✅ Clear |
| Difficulty filter | "I'm a beginner, I only want beginner-friendly" | ✅ Clear |
| Availability filter | "I'm outside the US, skip US-only" | ✅ Clear |
| Feed tabs (Trending/Top Rated) | ??? | ⚠️ No clear user need at launch — this is a builder's assumption |
| "Hidden Gems" tag | "Discover programs I've never heard of" | ✅ Clear, keep it |
| Vote system | "Tell others if this program was good" | ✅ Weak but valid |
| Contributor credits | ??? | ❌ No user need identified at MVP scale |
| Content type filter | "I make videos, show video programs" | ⚠️ Redundant with category — merge |
| Sort by Highest Payout | "Show me the most lucrative programs" | ⚠️ Data doesn't support this accurately |
| JSON-LD structured data | (Not a user story — it's SEO) | ⚠️ No user need; defer |
| "What Creators Say" (50-100) | "Is this program legit?" | ✅ Valid need, but 3 quotes per program is sufficient |
| Apply popup | "Remind me of requirements before I apply" | ✅ Critical — keep |
| Last verified date | "Is this info current?" | ✅ Critical — keep |

**Overall:** 3-4 features have no clear user story or the user story doesn't justify MVP complexity. Cut them.

---

## 3. Build Order Assessment

The proposed build order is mostly right but has two risky sequencing issues:

**Issue 1: Data should come BEFORE UI polish**

Steps 11-13 (populate 150+ programs, collect banner images, curate quotes) are placed at the end. This is wrong. You should:
- **Start with 30-40 real programs** (the best ones per category)
- **Build UI against real data** (not sample JSONs)
- **Add remaining programs incrementally** after the UI is built and tested

Building against 10 samples and then stuffing in 150+ is a recipe for UI bugs you discover too late (card text overflow, broken image states, weird category distribution, etc.).

**Revised Build Order:**

| # | Task | Est. |
|---|------|------|
| 1 | Next.js + Tailwind setup | 1h |
| 2 | Data schema + **30 real programs** (3 per category) | 3h |
| 3 | Browse page — card grid + category sidebar | 4h |
| 4 | Program modal — split layout | 3h |
| 5 | Apply popup + tracked redirect | 2h |
| 6 | Search (Fuse.js) | 2h |
| 7 | Filters (category, status, difficulty, availability) | 2h |
| 8 | Homepage — hero + sections | 3h |
| 9 | Vote system | 1h |
| 10 | Submit + Report forms (Formspree) | 1h |
| 11 | Mobile responsive fixes | 2h |
| 12 | **Populate remaining ~120 programs** | 8-10h |
| 13 | Collect banner images (OG auto-fetch + top 30 manual) | 3h |
| 14 | SEO — meta tags + sitemap | 1.5h |
| 15 | QA + Deploy | 2h |
| **TOTAL** | | **~38-42h** |

**Issue 2: Mobile responsive should be step 3, not step 16**

Building desktop-first and retrofitting mobile at step 16 doubles the CSS work. Tailwind makes this easier but you'll still spend 2x longer. Design mobile-first from step 3.

---

## 4. Edge Cases Not Addressed

1. **Programs that change terms mid-display** — What if a user bookmarks `/programs/tiktok-creator-fund` and when they return, the program is "Closed"? The modal needs a clear closed/paused state CTA: "This program is closed — see similar programs →"

2. **Search with typos** — Fuse.js handles fuzzy matching but the threshold needs tuning. "ElevenLab" vs "ElevenLabs" — does it match? Test this specifically. Default Fuse.js threshold is often too strict.

3. **Programs with no payout data** — Schema allows `payoutRange` to be a string, but some programs genuinely don't publish payment info ("Varies", "Invite only"). The UI needs to handle "Payout: Undisclosed" gracefully, not show a blank field.

4. **Multiple programs for same company** — Adobe has Adobe Stock AND Adobe Express Creator. Canva has Canva Creator AND Canva Affiliate. How do you display these? Related programs panel? Or separate cards? Not defined.

5. **Sharing a filtered URL** — `/browse?category=ai&status=active&difficulty=beginner` — does this work on first load? URL state restoration needs explicit testing. Easy to break in Next.js App Router.

6. **Image CDN limits** — If you're storing 150+ banner images on Vercel, free tier has a 100GB bandwidth limit. With 150 images at ~200KB each = 30MB per full page load cycle. 3,333 full loads = bandwidth limit. Need to aggressively use lazy loading and consider Cloudflare R2 or similar for images.

7. **OG image auto-fetch is unreliable** — Many sites don't have OG images, or their OG image is behind a CDN that requires user-agent spoofing. The fallback chain (OG → gradient) will hit "gradient" more often than expected — budget 50+ programs needing manual banners, not 10-20.

8. **Vote manipulation** — localStorage can be cleared. Anyone can vote unlimited times by clearing localStorage. Minor issue for MVP, but if votes heavily influence "Trending/Top Rated" tabs, expect gaming. Document this limitation and ignore it for V1.

---

## 5. Metrics Assessment

**Current success metrics in spec:** Not explicitly defined (gap!).

The spec has a "Programs You Might Not Know" section and analytics tracking for redirects but no KPI targets are defined. This is a problem — without targets, you won't know if you're succeeding.

**Recommended V1 Metrics:**

| Metric | Target (30 days post-launch) | Why |
|---|---|---|
| Total apply clicks | 500+ | Core value delivered |
| Apply click rate (clicks/visits) | >15% | Are visitors actually using it? |
| Search usage rate | >40% of sessions | Is search working? |
| Programs submitted by community | 5+ | Community contribution working? |
| Avg session duration | >90 seconds | Are people browsing or bouncing? |
| Mobile traffic % | >50% | Mobile-first claim validated? |
| Top 5 most applied-to programs | Know these | Understand what users want |
| Bounce rate by entry source | <65% | SEO traffic quality |
| Reports submitted | Track but no target | Data quality signal |

**What NOT to measure in V1:**
- Vote counts (too gameable, too few users)
- Trending tab clicks (not meaningful with small dataset)
- Revenue (there is none in V1)

**Realistic traffic expectation:** 
- Launch day: 200-500 visitors (Product Hunt / Twitter post)
- Week 1: Drops to 50-100/day organic
- Month 1 total: ~2,000-3,000 visitors
- Month 3 SEO organic: Potentially 5,000-15,000/month if content is indexed well

Don't call it a failure if month 1 is 2,000 visitors. That's realistic for a zero-budget launch.

---

## 6. Data Quality — Is 150+ Programs Realistic?

**Short answer: The data collection is significantly underestimated.**

**The math:**
- 150 programs × ~20 minutes of research per program = **50 hours** of data collection alone
- This doesn't include writing unique descriptions, quick tips, finding logos, and verifying all info

**Breakdown of per-program work (realistic):**
- Find official program page: 2 min
- Read and verify requirements: 5 min
- Write/adapt description (own words, not copy-paste): 5 min
- Write quick tip: 3 min
- Find and download logo: 2 min
- Find/download banner image: 3 min (or verify OG image)
- Fill all schema fields: 5 min
- Cross-reference related programs: 3 min
- **Total: ~28 min per program**

150 × 28 min = **70 hours** for data collection. With Jarvis (AI) doing 70% of it, estimate **25-30 hours of human review + AI generation time** — but AI-generated data MUST be verified for accuracy (wrong payout info or closed programs will kill trust immediately).

**Recommendations:**

1. **Launch with 60-80 programs, not 150+.** Pick the best 5-8 per category. This halves data work. "60+ Programs across 11 categories" is still compelling. Users won't notice the missing 90 programs on day 1.

2. **Tier your data effort:**
   - **Tier A (30 programs):** Full treatment — manual banners, curated quotes, verified everything, cross-linked
   - **Tier B (30 programs):** Standard treatment — OG image, AI-written description, verified basics
   - **Tier C (remaining):** Minimal — just the essentials, image = gradient, no quotes

3. **The riskiest data issue:** Programs that appear active but are actually closed/invite-only. A creator clicks "Apply" and lands on a 404 or closed page. This is the #1 trust-killer. Need a manual verification pass on every single "Apply" URL before launch, no exceptions.

4. **The OG image auto-fetch problem:** Don't rely on it at launch. Build the fallback system but assume 40-50% of OG fetches will fail silently. Pre-download and store locally for top 50 programs.

---

## 7. Timeline Assessment

**Spec says: 35-40 hours. Realistic: 55-65 hours.**

**What's always underestimated in projects like this:**

| Task | Spec Estimate | Realistic Estimate | Why Underestimated |
|---|---|---|---|
| Program modal — UI | 3h | 4-5h | Split layout + mobile version + all states (closed, loading, error) |
| Data population | 8-10h | 20-25h | Research + verify + describe 150 programs |
| Banner images | 3h | 5-6h | OG fetch failures, manual curation, image optimization |
| Mobile responsive | 2h | 3-4h | Bottom sheet filter is non-trivial |
| SEO setup | 2h | 2.5h | Sitemap generation + meta tags per page |
| QA | 2h | 3-4h | Cross-browser, filter combos, search edge cases |
| **Total** | **35-40h** | **55-65h** | **+55% over-optimism** |

**If you cut the scope as recommended (launch with 70 programs, cut 4-5 features):**
- Realistic timeline: **40-48 hours** — achievable for a solo developer in 2-3 weeks of part-time work

---

## 8. Pain Points Cross-Check

| Pain Point | Severity | MVP Feature Addressing It | Coverage |
|---|---|---|---|
| #1 Discovery is broken | 🔴 Critical | Directory + Search + Category browse | ✅ FULLY COVERED |
| #2 Info scattered & stale | 🔴 Critical | Standardized schema + Last Verified date + Report button | ✅ WELL COVERED — maintenance is the gap |
| #3 Category blindness | 🟠 High | Cross-category browse + "Similar Programs" in modal | ✅ COVERED |
| #4 Low/unpredictable pay | 🟠 High | Payout info in schema, but no community earnings data | ⚠️ PARTIALLY — spec acknowledges this is V2. Acceptable. |
| #5 Overwhelming choice | 🟠 High | Difficulty + Content Type + Availability filters | ✅ COVERED — but "Programs for me" quiz is V2, which weakens this |
| #6 Application confusion | 🟡 Medium | Requirements in apply popup + eligibility in schema | ⚠️ PARTIALLY — requirements listed but no "do you qualify?" check |
| #7 Programs disappear | 🟡 Medium | Active/Paused/Closed status + Last Verified date | ✅ COVERED for static data — alerts are V2 |

**Gaps:**

- **Pain Point #5 — "Programs for me" quiz** is the most powerful UX for overwhelmed beginners, and it's in V2. Consider a minimal version: a "filter by content type + difficulty" preset (e.g., "I'm a beginner photographer" → auto-applies filters). Takes 2 hours extra but dramatically improves first-time user experience.

- **Pain Point #6 — Application confusion** is only half-solved. The apply popup shows requirements but doesn't tell users "you probably don't qualify yet" (e.g., if YouTube requires 1,000 subs and the user has 200). This requires user input (account creation) so it's rightly V2. But the UX should be honest: show "Typical applicant: 10K+ followers" not just the minimum bar.

---

## 9. Top 10 Actionable Recommendations

**Priority 1 — Do these before building:**

1. **Reduce launch data target to 70-80 programs.** Ship faster, with higher quality data. Add more post-launch. Write "80+ Programs" in the stats bar, not "150+."

2. **Manual verify every "Apply" URL before launch.** Build a simple script that pings each URL and flags 4xx/5xx responses. One broken apply link per category is acceptable; a 20% broken rate is a launch killer.

3. **Cut: Feed tabs (Trending/Top Rated), Content type filter, Sort by Payout, Contributor credits, Full About page, per-program quotes (50-100 of them).** This saves ~6-8 hours and removes features that would feel hollow at launch.

**Priority 2 — Change while building:**

4. **Design mobile-first from Day 1.** Use Tailwind's mobile breakpoints as the base, not the override. Will save 2-3 hours of retrofitting.

5. **Build with 30 real programs in Step 2, not 10 samples.** Catch data/UI mismatches early, not at Step 11.

6. **Add empty state and error state designs** for search (no results), filter combos (no matching programs), and broken apply links. Takes 2 hours but prevents "broken" feeling.

7. **Add a simple "preset filter" button** for Pain Point #5: "I'm a Beginner" / "I'm a Photographer" / "I'm a Developer" — pre-applies relevant filters. No quiz logic needed. Takes 1-2 hours and meaningfully improves UX for overwhelmed users.

**Priority 3 — Launch decisions:**

8. **Set explicit launch KPIs before you start.** Target: 500 apply clicks in month 1. If you hit it, the platform works. If not, investigate why.

9. **Don't auto-fetch OG images at runtime.** Pre-download them. Auto-fetch can be added in V2 for new submissions. Runtime fetching will cause slow first loads and CORS issues.

10. **Pick the domain name NOW** (it's listed as an open decision). Everything from SEO to sharing depends on it. Don't build 40 hours of content before securing the domain.

---

## Final Verdict

**This is a genuinely good idea with a well-researched spec.** The core value proposition is clear, the data schema is thoughtful, and the tech stack is sensible. The main risks are:

- **Overestimated timeline** (add 20-30 hours buffer)
- **Overestimated data scope** (cut to 70-80 programs for launch)
- **4-5 features that add complexity without adding user value** (cut them)
- **Underinvestment in error/empty states** (add them before launch)

Scope it down, verify your data, launch faster. The core value — one place to discover 150 creator programs — doesn't need 35 features to be compelling. It needs 20 really good ones.

**Confidence that V1 would succeed if built as spec'd:** 65%  
**Confidence that V1 would succeed with recommended cuts:** 80%

---

*Review complete. Cross-checked against 7 pain points. 10 actionable recommendations provided.*
