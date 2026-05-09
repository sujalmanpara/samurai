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

## Run 2 — 2026-05-09 — 0509-0635-9db2
- Objective: Research Factory AI Missions and SAMURAI validation patterns; produce source-grounded brief and self-check for unsupported claims.
- Task type: research
- Agents used: 1 (`researcher`, Sonnet)
- Completed? yes
- Did output answer the request? yes
- Issues found after delivery: none blocking; researcher self-identified terminological drift around "Validation Contract" not being verified as Factory's own term.
- Would a validation contract have caught this? yes — explicit claim-label requirements acted as a validation-contract surrogate and forced source verification.
- Would a separate validator have caught this? likely yes — a validator could cross-check that every claim in brief.md appears in claims-table.md and that PRIMARY SOURCE labels have verifiable URLs.
- Sequencing issue? no
- Notes: Strong evidence that research tasks benefit from first-class validation contracts / claim-label requirements. This is Run 2 supporting validation contract usefulness, but still only 1 run supporting separate Validator usefulness.

## Run 3 — 2026-05-09 — 0509-0902-2e77
- Objective: Design a lightweight validation-contract feature for SAMURAI based on evidence from Runs 1 and 2; produce an implementation-ready plan with risks, tests, and no overengineering.
- Task type: planning / design
- Agents used: 1 (`designer`, Sonnet)
- Completed? yes
- Did output answer the request? yes
- Issues found after delivery: none blocking.
- Would a validation contract have caught this? yes — upfront design constraints acted as an informal contract and prevented scope creep into full Validator/runtime designs.
- Would a separate validator have caught this? unclear — the designer's self-check was strong, but a validator could verify prompt-patches.md contains exact text and all required files exist.
- Sequencing issue? no
- Notes: Strong evidence that first-class validation contracts help planning/design tasks by making constraints explicit before execution. Existing Queen self-check is useful but insufficient alone because it checks completeness/coherence, not correctness against pre-written criteria.
