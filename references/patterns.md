# SAMURAI — Common Decomposition Patterns

Reference patterns for the Queen agent when decomposing tasks. These are starting points — adapt and combine as needed.

---

## Pattern 1: Build Software

**Trigger:** "Build me a...", "Create an app...", "Make a website..."

```
Phase 1 (parallel):
  - Researcher: Study similar products, gather requirements
  - Architect: Design system architecture

Phase 2 (parallel, after Phase 1):
  - Coder-backend: Build API/backend
  - Coder-frontend: Build UI/frontend
  - (optional) Coder-infra: Setup deployment

Phase 3 (sequential, after Phase 2):
  - Reviewer: Code review all outputs
  - Tester: Write and run tests

Phase 4:
  - Queen: Synthesize, apply fixes, deliver
```

**Model tiers:** Architect=Opus, Coders=Sonnet, Reviewer=Sonnet, Tester=Haiku

---

## Pattern 2: Research & Report

**Trigger:** "Research...", "Find out about...", "Compare..."

```
Phase 1 (parallel):
  - Researcher-1: Search web for topic A
  - Researcher-2: Search web for topic B
  - Researcher-3: Search web for topic C

Phase 2:
  - Analyst: Combine all research, identify patterns
  - Writer: Draft the report

Phase 3:
  - Reviewer: Fact-check and polish
```

**Model tiers:** Researchers=Sonnet, Analyst=Opus, Writer=Sonnet, Reviewer=Haiku

---

## Pattern 3: Code Review / Audit

**Trigger:** "Review this code...", "Audit the security..."

```
Parallel:
  - Security-auditor: Check for vulnerabilities
  - Quality-reviewer: Check code quality, patterns
  - Performance-analyst: Check for bottlenecks
  - (optional) Test-writer: Write missing tests

Synthesis:
  - Queen: Combine all findings into unified report
```

**Model tiers:** Security=Opus, Quality=Sonnet, Performance=Sonnet, Tests=Haiku

---

## Pattern 4: Content Creation

**Trigger:** "Write a blog post...", "Create content for..."

```
Phase 1 (parallel):
  - Researcher: Topic research, competitor analysis
  - SEO-analyst: Keyword research, search intent

Phase 2 (competitive):
  - Writer-A: Draft with approach A (storytelling)
  - Writer-B: Draft with approach B (data-driven)

Phase 3:
  - Editor: Review winner, polish, add CTAs
  - SEO-optimizer: Add meta tags, internal links
```

**Model tiers:** Researcher=Sonnet, Writers=Sonnet, Editor=Opus, SEO=Haiku

---

## Pattern 5: Refactor / Migration

**Trigger:** "Migrate from...", "Refactor the..."

```
Phase 1:
  - Analyst: Map the existing codebase, identify all changes needed

Phase 2 (parallel):
  - Migrator-1: Handle module A
  - Migrator-2: Handle module B
  - Migrator-3: Handle module C
  - Test-updater: Update all tests

Phase 3:
  - Integration-tester: Verify everything works together
  - Reviewer: Final review
```

**Model tiers:** Analyst=Opus, Migrators=Sonnet, Tests=Haiku, Reviewer=Sonnet

---

## Pattern 6: Debug / Fix

**Trigger:** "Fix this bug...", "Why is this failing..."

```
Parallel:
  - Investigator-1: Trace the error path
  - Investigator-2: Check recent changes / git blame
  - Reproducer: Write a minimal reproduction

Synthesis:
  - Fixer: Apply the fix based on findings
  - Tester: Verify the fix
```

**Model tiers:** Investigators=Sonnet, Fixer=Sonnet, Tester=Haiku

---

## Pattern 7: Data Processing / Analysis

**Trigger:** "Analyze this data...", "Process these files..."

```
Phase 1:
  - Schema-analyst: Understand data structure

Phase 2 (parallel):
  - Processor-1: Handle batch 1
  - Processor-2: Handle batch 2
  - Processor-N: Handle batch N

Phase 3:
  - Aggregator: Combine results
  - Visualizer: Create charts/summaries
```

**Model tiers:** Schema=Sonnet, Processors=Haiku, Aggregator=Sonnet

---

## Pattern 8: Planning / Strategy

**Trigger:** "Plan a...", "Strategy for...", "How should we..."

```
Phase 1 (parallel):
  - Market-researcher: Market analysis
  - Competitor-analyst: Competitor landscape
  - Technical-analyst: Technical feasibility

Phase 2:
  - Strategist: Synthesize into strategy options

Phase 3 (human checkpoint):
  - Queen presents options to user → user decides

Phase 4:
  - Planner: Create detailed action plan from chosen strategy
```

**Model tiers:** Researchers=Sonnet, Strategist=Opus, Planner=Sonnet

---

## Pattern 9: Pipeline (Multi-Phase Project)

**Trigger:** Large projects that need phases

```json
{
  "phases": [
    { "id": "discover", "pattern": "Research & Report" },
    { "id": "design", "pattern": "Planning / Strategy" },
    { "id": "build", "pattern": "Build Software" },
    { "id": "validate", "pattern": "Code Review / Audit" }
  ]
}
```

Each phase uses its own team. Output of each phase feeds into the next.

---

## Pattern 10: Simple Task (No Swarm)

**Trigger:** Simple question, quick fix, single-step task

```
Queen handles it directly. No agents spawned.
```

**IMPORTANT:** Not every task needs a swarm. If it's a simple question, translation, or one-file fix — just do it yourself. Don't over-engineer.

---

## Combining Patterns

Complex tasks often combine multiple patterns:

- "Build a SaaS product" → Pattern 8 (Planning) → Pattern 1 (Build) → Pattern 3 (Audit)
- "Write a research paper" → Pattern 2 (Research) → Pattern 4 (Content) with competitive spawning
- "Fix and improve the codebase" → Pattern 6 (Debug) + Pattern 5 (Refactor) + Pattern 3 (Audit)

The Queen decides which patterns apply and how to chain them.
