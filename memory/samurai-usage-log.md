# SAMURAI Usage Log

Purpose: collect real evidence before implementing heavier v2.0 features (validation contracts, validator agent, serial execution).

Evidence gate from validation run 0509-0559-3926:
- Consider validation contracts after ≥3/10 runs show issues a contract would catch.
- Consider validator agent after ≥2 contract-based runs show Queen self-check missed issues a separate validator would catch.
- Consider sequential spawning after ≥2 runs show sequencing failures.

## Run Template

```markdown
## Run N — <date> — <run-id>
- Objective:
- Task type: research / code / content / planning / mixed
- Agents used:
- Completed? yes/no/partial
- Did output answer the request? yes/no/partial
- Issues found after delivery:
- Would a validation contract have caught this? yes/no/unclear
- Would a separate validator have caught this? yes/no/unclear
- Sequencing issue? yes/no
- Notes:
```

## Runs


## Run 1 — 2026-05-09 — 0509-0621-009a
- Objective: Audit and verify SAMURAI Phase 1 minimal fixes for regressions, prompt consistency, and CLI behavior; fix issues found within scope.
- Task type: code audit / verification
- Agents used: 1 (`code-auditor`, Sonnet)
- Completed? yes
- Did output answer the request? yes
- Issues found after delivery: 1 high-severity regression in `classify_task()` noun suppression; the auditor fixed it.
- Would a validation contract have caught this? yes — explicit expected classifier cases caught the regression.
- Would a separate validator have caught this? maybe — the single auditor already caught/fixed it because the prompt included concrete tests.
- Sequencing issue? no
- Notes: Evidence supports adding precise test expectations to future SAMURAI tasks. It does not yet prove a persistent need for a separate Validator agent.
