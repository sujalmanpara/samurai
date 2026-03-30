# UX Design Review — Creator Program Aggregator MVP
**Reviewer Role:** UX Designer  
**Date:** 2026-03-20  
**Files Reviewed:** FINAL-MVP-SPEC-v2.md + step6-platform-design-deep-dive.md

---

## Executive Summary

The spec is well-researched and the daily.dev-style interface is a smart pattern to borrow. The core UX decisions are mostly sound. However, there are 4 significant concerns that could hurt the product: (1) first-time users may not understand what a "creator program" is, (2) the split-layout modal breaks on mobile, (3) OG image inconsistency will make cards look chaotic, and (4) the filter system is 2-3 layers too complex for v1. These are all fixable — some with simple design changes, some with scope trim.

---

## 1. First Visit Experience — Will They Get It in 5 Seconds?

### ✅ What Works
- Short hero concept is right — no giant hero image
- Category pills for self-identification ("Is this for me?") is smart pattern
- "150+ Programs | 11 Categories | Free Forever" stats bar is good social proof
- Show cards above the fold — correct instinct

### ⚠️ What Could Confuse New Users

**Problem: "Creator Program" is industry jargon**  
Not every creator knows this term. A photographer who just started might not know that stock sites pay contributors, or that AI tools have "creator programs." The term assumes familiarity.

**Fix:** Add a one-sentence explainer *under* the headline:
> "Creator programs are paid partnerships, revenue sharing deals, and contributor programs offered by platforms. Most creators don't know they exist."

Or use the subtitle more explicitly:
> "150+ platforms pay creators. Stock sites, AI tools, video platforms, design apps — most have programs most creators don't know about."

**Problem: Search bar as the primary CTA on homepage**  
New visitors don't know what to search for if they don't know what programs exist. Searching requires knowing what you want — but the magic of this product is *discovery*.

**Fix:** Make the category pills the primary action, search secondary. Lead with:
> "What do you create? →" then the category pills.

The search bar can exist but shouldn't visually dominate. The discovery journey (Journey C in the spec) is the magic — design the homepage for that, not for search-first.

**Problem: "Stop leaving money on the table" is weak**  
This is a cliché opener. It doesn't communicate *how much* or *how easy* it is. First 3 words matter most.

**Alternative headlines:**
- "150+ platforms pay creators. Are you missing out?"
- "Find every creator program. Free. No signup."
- "The programs paying creators — all in one place."

### 📐 Recommended Hero Structure
```
[Headline: Bold, 1-2 lines, specific]
[Subheadline: What it is + why it matters, 1-2 sentences]
[Category pills — the primary CTA]
[Search bar — secondary, smaller]
[Stats bar: 150+ programs | 11 categories | Free forever | Last updated: March 2026]
```
Then immediately: program cards. No long how-it-works section before cards.

---

## 2. Browse Page UX — daily.dev Style

### ✅ What Works
- Instant filtering (no apply button) is correct
- Removable pills for active filters is correct
- URL updates for shareability is correct
- 3-col → 2-col → 1-col responsive grid is correct

### ⚠️ Hierarchy Confusion: Feed Tabs vs. Category Sidebar

**Problem:** Feed tabs (All/Trending/Top Rated/New/Hidden Gems) live in the sidebar, AND the category navigation also lives in the sidebar. These are two different types of sorting/filtering competing for the same space and hierarchy.

Feed tabs are a different dimension than categories — one controls *ranking/curation*, the other controls *subject matter*. Mixing them in the same sidebar creates cognitive confusion.

**Fix:** Move feed tabs to the main content area, above the grid — as a horizontal tab bar:
```
[Browse] [All ▼] [Trending] [Top Rated] [New] [Hidden Gems]
```
The sidebar then becomes purely: **Category navigation + Submit/Report links.**

This mirrors what daily.dev actually does — tags/topics in the sidebar, feed type in the top bar.

### ⚠️ Sidebar Is Too Tall
11 categories + 5 feed tabs + Submit link + Report link = ~20 sidebar items. On a 768px screen, the sidebar overflows.

**Fix:** 
- Collapse categories that have <5 programs under an expandable section
- Show top 7 categories by count, "Show all (4 more) ↓" collapses the rest
- Or use a thin icon sidebar (just icons + tooltips) that expands on hover

### ⚠️ "Hidden Gems" as a Feed Tab Is Overloaded
Hidden gems is a *tag/badge* on individual programs. Making it also a feed tab is correct, but if someone is already filtering by "AI category" and they also click "Hidden Gems" tab — are they seeing AI hidden gems? Or all hidden gems? The spec doesn't clarify this intersection.

**Fix:** Make it explicit: "Showing 12 AI · Hidden Gems programs" in the results count. The intersection should work as AND (category AND hidden gem status).

---

## 3. Modal Overlay — Split Layout

### ✅ What Works
- Overlay concept is right for preserving browse context
- URL change to `/programs/[id]` for SEO + sharing is correct
- Scroll position preservation on close is correct
- Left: details, Right: quick action panel — good desktop layout

### 🔴 Critical: Split Layout Breaks on Mobile

A 50/50 split modal on a 375px phone screen is unusable. Both columns would be ~175px wide — not enough for text or any meaningful content.

**Fix: Mobile-specific modal layout**

On mobile (< 768px), the modal should NOT be a floating overlay. Instead:
- Navigate to a full page: `/programs/[id]`
- Single-column layout, full screen
- Sticky bottom bar with the "Apply" button always visible
- Back button at top returns to browse at same scroll position (use history.back())

This is actually what daily.dev does — their article page is full screen on mobile, not a modal.

```
Mobile modal structure:
┌─────────────────────────┐
│ ← Back to Browse        │
│─────────────────────────│
│ [Banner image]          │
│ Logo + Platform name    │
│ Type badge | Category   │
│─────────────────────────│
│ Description             │
│ Requirements list       │
│ Payout info             │
│ Quick tip               │
│ Availability + Difficulty│
│ Last verified: 2026-03  │
│ Similar programs →      │
│ Vote + Share            │
│─────────────────────────│
│ [Apply to Program →]    │ ← sticky bottom
└─────────────────────────┘
```

### ⚠️ Modal Edge Cases to Design For

**Very long requirement lists:**  
Some programs have 10+ requirements. In the left column, this will push the "Apply" button way down. Consider: show first 5 requirements, "Show all X requirements ↓" expandable.

**Programs with minimal info:**  
If a program has no quickTip, no creatorsSay quotes, and a 2-sentence description — the left column will look sparse and empty next to a full right panel.  
**Fix:** For sparse programs, collapse the right panel into inline sections rather than a fixed split. Only use the split when there's enough content to justify it.

**Modal background scroll:**  
When the modal content is longer than the viewport and the user scrolls inside the modal, some browsers accidentally scroll the background too. Use `overflow: hidden` on body when modal is open.

**Right panel "Similar Programs" section:**  
If there are 0 similar programs mapped, this section looks empty. Always have a fallback: "Browse more [Category] programs →"

---

## 4. Card Design — Visual Consistency

### ✅ What Works
- Fallback chain (manual → OG → brand gradient) is smart
- Standardized card dimensions prevent layout chaos (if enforced)
- Status badge with color + text is correct

### 🔴 OG Image Inconsistency Is the Biggest Visual Risk

OG images pulled from program websites vary wildly:
- Some are `1200x630` (ideal)
- Some are `1080x1080` (square)
- Some are `600x315` (small)
- Some are `1920x1080` (wide cinema)
- Some have text overlaid (looks bad at card size)
- Some are product screenshots (not brand images)
- Some are just the company logo on white

If you stretch or crop these to a fixed aspect ratio, many will look broken, distorted, or cropped to show nothing meaningful.

**Fix:** 
- Enforce a **fixed aspect ratio container** (16:9 recommended) with `object-fit: cover` and `object-position: center` in CSS
- For the top 30-40 programs, manually curate/create banner images (already planned — good)
- For the rest, test OG images at card size before launch — discard ones that look bad and fall to the gradient
- Consider generating simple branded gradient + logo overlays for all 150 programs as a clean fallback — more consistent than random OG images

**Gradient fallback formula:**
```
[Brand primary color] → [Brand secondary or darkened brand color]
Centered: [Logo] + [Program name]
```
This always looks clean and intentional. It might actually look *better* than random OG images.

### ⚠️ Card Information Density Is High

The card currently shows:
- Banner image
- Logo + Program name  
- Category badge + Type badge
- Payout model hint
- Availability + Difficulty
- Status badge
- Vote % + count
- Hidden Gem tag
- Apply button

That's 9-10 elements. On a grid card at ~280px wide, this is very dense.

**Suggested trim for cards:**
- Remove **Availability** from card (show in modal — most users will just apply if interested)
- Remove **Content type** if it's already in the Category
- The card should answer 4 questions (per the spec's own framework): Platform? Type? Joinability? Worth it? Stick to those 4.

**Streamlined card:**
```
┌──────────────────────────┐
│ [Banner/OG image 16:9]   │
├──────────────────────────┤
│ [Logo] Platform Name     │
│ 🤖 AI · Revenue Share    │
│ 💰 $50-$500/month        │
│ 🟢 Active  · Beginner   │
│ 👍 82% (45)  [Apply →] │
│ ✨ Hidden Gem            │
└──────────────────────────┘
```

### ⚠️ Programs With Missing Data Will Look Bad
What renders if:
- `payoutRange` is null? → Show "Varies" not an empty row
- `difficulty` is unknown? → Show "Unrated" not nothing
- `votes` = 0? → Show "New — be first to vote!" not "0% (0 votes)"
- `logo` file missing? → Show brand initial letter in a colored circle

Every nullable field needs a designed empty state.

---

## 5. Filter UX — Too Many Filters for V1

### ✅ What Works
- Instant filtering is correct
- Removable pills for active filters is correct
- Result count ("Showing 23 of 150+") is correct
- Mobile bottom sheet is the right pattern

### ⚠️ 8 Filter Types Is Too Many for MVP

Current filters:
1. Category (11 options)
2. Type (8 types: Revenue Share, Fund, Contributor, Grant, Affiliate, Ambassador, Marketplace, Beta)
3. Difficulty (3)
4. Availability (Worldwide/regional)
5. Status (Active/Paused/Closed)
6. Content type (7: Video/Photo/Design/Writing/Music/Code/3D)
7. Sort (4 options)
8. Feed tabs (5)

That's 8 filter dimensions. Plus a search bar. This is more than most mature directories offer.

**The problem:** The "Content type" filter and "Category" filter are nearly redundant. "AI Tools" category + "Video" content type overlap significantly. Users will be confused about which to use.

**V1 Recommendation — drop to 5 filters:**
1. **Category** (11) — the primary filter, keep
2. **Type** (8) — important for understanding program nature, keep  
3. **Status** (Active/Paused/Closed) — default to "Active only" checked, keep
4. **Difficulty** (3) — keep, it's simple and useful
5. **Availability** (simplified to: Worldwide / Region-specific) — simplify

Drop for v1:
- **Content type** — overlaps heavily with category
- Feed tabs can be simplified to **Sort** only (Popular/New/Top Rated) — remove "Trending" and "Hidden Gems" as separate tabs (Hidden Gems becomes a filter toggle instead)

**Better Hidden Gems UX:**  
Instead of a feed tab, make it a toggle:
```
[☆ Show Hidden Gems only]
```
A checkbox/toggle is more intuitive than a feed tab for what is essentially a boolean filter.

### ⚠️ Mobile Bottom Sheet Filter Design Needs Attention

8 filter categories in a bottom sheet = a lot of scrolling. The sheet needs:
- Grouped sections with collapse/expand
- "Active filters" section at top showing what's selected
- Sticky "Show X results" button at bottom always visible
- One-tap "Clear all" button

**Bottom sheet wireframe:**
```
┌────────────────────────┐
│ Filters         Clear all │
│────────────────────────│
│ ▼ Category (1 selected) │
│   • AI   • Design  ...  │
│ ▼ Program Type          │
│   • Revenue Share  ...  │
│ ▼ Status               │
│   ● Active  ○ All      │
│ ▼ Difficulty           │
│   Beginner  Inter  Adv  │
│────────────────────────│
│     [Show 23 results →] │
└────────────────────────┘
```

---

## 6. Apply Flow — Friction or Value?

### ✅ Assessment: The Popup Adds Value

The requirements popup before redirect is actually *good UX* despite being an extra click. Here's why:

**Without the popup:** User clicks Apply → lands on platform page → reads requirements → discovers they don't qualify (e.g., needs 10K followers) → back button → repeat. Time wasted.

**With the popup:** User sees requirements upfront → if they don't qualify, they close and look for something else → time saved.

The popup is essentially a **pre-qualification screen**, not just a confirmation dialog. This is a real value-add for users who are new to creator programs.

### ⚠️ Popup Design Concerns

**Problem: "Continue to Platform →" is generic**  
The button should include the platform name to set expectation:
> "Open Canva Creator Program →"

**Problem: The popup could feel like a dark pattern**  
If the popup looks like an ad or a lead capture form, users will close it immediately. It needs to look like helpful information, not a barrier.

**Design principle:** 
- Clean white background, no gradients
- Information presented as a simple summary card
- The CTA button should be at the bottom and prominent
- Minimal UI chrome — no popup header with an "X" that's easy to miss

**Recommended popup structure:**
```
┌──────────────────────────────┐
│ [Logo] Canva Creator Program │
│                              │
│ ✅ Requirements              │
│  • Active Canva account      │
│  • Template portfolio        │
│                              │
│ 💰 Revenue share per template│
│ 🌍 Available worldwide       │
│ 🟢 Beginner-friendly         │
│                              │
│ 💡 Tip: Upload 10+ templates │
│    before applying           │
│                              │
│ ℹ️ Verify details on         │
│    official site before applying│
│                              │
│ [Open Canva Creator Program→]│
│ [← Back to Browse]          │
└──────────────────────────────┘
```

**Consider:** An animation when the popup appears — a subtle slide-up rather than a hard appear. Makes it feel intentional, not jarring.

---

## 7. Accessibility Concerns

### 🔴 Critical Issues

**Vote buttons have no accessible label**  
`👍` and `👎` emoji buttons need `aria-label`:
```html
<button aria-label="Upvote Canva Creator Program">👍</button>
```
Without this, screen readers announce "button" with no context.

**Modal focus trap missing from spec**  
When the modal opens, keyboard focus must be trapped inside. Tab should cycle through modal elements only. Escape should close. This needs to be explicitly built — Next.js parallel routes don't handle this automatically.

**Color is the only indicator for freshness**  
The spec says "color-coded: green/yellow/red" for last verified dates. Color alone fails for colorblind users. 

**Fix:** Add text indicators:
- 🟢 "Updated recently (March 2026)"
- 🟡 "Verify recommended (Sep 2025)"  
- 🔴 "Needs review (Feb 2025)"

Or use symbols: ✅ / ⚠️ / ⚡

**Emoji category icons in sidebar/pills**  
Emoji without alt text/aria-labels are read aloud weirdly by screen readers. "Robot face category AI" vs just "AI Tools category."

**Fix:** `<span aria-hidden="true">🤖</span> AI Tools`  
The emoji is decorative; the text carries the meaning.

### ⚠️ Should-Fix Issues

- Minimum tap target for vote buttons: spec says 44px — make sure to enforce this in implementation
- Search results should announce count changes to screen reader: `aria-live="polite"` on result count
- Cards should be navigable by keyboard (tabindex + enter to open modal)
- Modal close button needs visible focus state, not just color change
- "Report outdated info" and "Submit" links in sidebar need sufficient contrast against sidebar background

---

## 8. Mobile Experience — Sidebar Adaptation

### The Core Problem
The left sidebar contains: Feed tabs + Category navigation + Submit/Report links. None of this translates to mobile as-is.

### Recommended Mobile Navigation Architecture

**Option A: Bottom Tab Bar + Separate Filter Sheet (Recommended)**

```
┌─────────────────────────────┐
│ 🔍 Search programs...       │ ← sticky top
│─────────────────────────────│
│ [All] [AI] [Design] [Video] │ ← horizontal scroll, most popular categories
│─────────────────────────────│
│                             │
│ [Card]  [Card]              │ ← 2-column grid
│                             │
│ [Card]  [Card]              │
│─────────────────────────────│
│ 🏠 Home  🔍 Browse  ➕ Submit│ ← bottom nav bar
└─────────────────────────────┘
```

- Sticky header: search bar
- Below header: horizontal category pill scroller (top 8 categories + "All")
- Feed sort (Trending/New/Popular) as a small sort dropdown "↕ Popular" next to filter button
- Filter button opens bottom sheet (as planned)
- Bottom nav: Home | Browse | Submit (3 items, no more)

**Option B: Hamburger Menu (Not Recommended)**  
Hamburger menus on mobile directories kill discoverability. Don't hide categories behind a hamburger.

**Specifically for category navigation:**  
The 11 categories need to be visible/scrollable without tapping anything. A horizontal pill scroller works well:
```
← [All] [AI] [Design] [Stock] [Video] [Writing] [Music] →
```
Pills horizontally scrollable, selected pill highlighted.

**Feed tabs on mobile:**  
Simplify to a sort dropdown: "↕ Sort: Popular ▼" which opens: Popular | Newest | Top Rated | Hidden Gems

This keeps the information accessible without a full tab bar competing for space.

---

## 9. If I Could Redesign One Thing

### → Redesign the Card Grid Banner Image Strategy

This is my top pick because it's a visual-first product and the card grid *is* the product experience. If the cards look inconsistent, cluttered, or broken — the whole platform feels untrustworthy, regardless of how good the data is.

**The problem in more depth:**  
150+ OG images from different websites will create a visual cacophony. Some will be dark, some light, some have text, some are minimal, some have faces, some are abstract patterns. When arranged in a grid, this creates visual noise that makes scanning exhausting.

**Redesign: Unified card visuals with a generated banner system**

Instead of relying on OG images, generate a consistent banner template for every program:

```
┌────────────────────────────────┐
│                                │
│   [Brand gradient background]  │
│                                │
│       [Platform Logo]          │
│   [Program Name, 1-2 lines]    │
│                                │
└────────────────────────────────┘
```

Each card gets a banner that uses:
- The brand's primary color as a gradient base
- The platform logo centered
- Subtle texture or pattern overlay for visual interest

**Result:**  
- Every card looks equally polished
- Brand colors make cards instantly recognizable (Canva = rainbow, Spotify = green, etc.)
- No broken/weird OG images
- Cards scan beautifully in a grid

**Implementation:** Generate SVG banners at build time using brand color + logo data from the JSON schema (which already has `brandColor` field). Zero manual work, scales to 150+ automatically.

The manually curated banners for top 30-40 programs (already planned) can be used as feature cards/hero spots on the homepage and as the first row of browse results.

---

## Summary: Priority Issues

| Priority | Issue | Impact | Fix Difficulty |
|----------|-------|--------|----------------|
| 🔴 Critical | Split modal doesn't work on mobile | Breaks experience for mobile users | Medium — use full page on mobile |
| 🔴 Critical | OG image inconsistency | Cards look chaotic | Medium — generate branded banners |
| 🔴 Critical | Vote buttons have no accessible labels | Screen reader users locked out | Easy — add aria-labels |
| 🟡 High | "Creator program" terminology unclear on first visit | New users bounce without understanding | Easy — add 1-sentence explainer |
| 🟡 High | Feed tabs in sidebar = confused hierarchy | Navigation feels illogical | Medium — move tabs to main area |
| 🟡 High | 8 filter types too complex for v1 | Filter paralysis | Medium — drop content type, simplify |
| 🟡 High | Sidebar has no mobile equivalent | Navigation broken on mobile | Medium — horizontal pill scroller |
| 🟠 Medium | Card information density too high | Cognitive overload, harder to scan | Easy — remove 2 fields from card |
| 🟠 Medium | Modal focus trap not specified | Keyboard users can't navigate modal | Easy — add to implementation checklist |
| 🟠 Medium | Freshness color = only indicator | Colorblind accessibility | Easy — add text/icon alongside color |
| 🟢 Low | Apply popup button text is generic | Slightly reduced clarity | Trivial — "Open [Platform] →" |
| 🟢 Low | Search bar as primary homepage CTA | Discovery-first messaging undermined | Easy — demote search, promote pills |

---

## What the Spec Does Really Well

Worth noting because the fundamentals are solid:

- **No login required** — correct call. Any friction before value kills directory sites.
- **Apply popup as pre-qualifier** — genuinely useful, not just friction
- **Instant filtering** — critical and too often missed
- **Scroll position preservation on modal close** — many developers forget this
- **URL-driven state** — `/browse?category=ai` is correct for SEO and sharing
- **Gradient fallback for images** — planned for, not an afterthought
- **"Last verified" dates** — trust signal that most directories skip
- **Empty states designed** — no results, closed programs, zero votes all considered
- **44px minimum tap targets** — mobile accessibility built in from the start

The product concept is strong. The UX risks are fixable, and none of them require scope cuts to the core value proposition.

---

*UX Review complete. Highest priority actions: Fix the mobile modal, generate consistent card banners, add aria-labels to vote buttons, move feed tabs to main content area.*
