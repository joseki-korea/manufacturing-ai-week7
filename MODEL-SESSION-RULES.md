# Model and session rules

## Status
DRAFT

## Inheritance
Global vault rules → this file → repository context. Local rules cannot relax global rules.

## Model placement
Main and persona sessions use Claude Opus. Work seats use Codex Terra, Antigravity (AGY), and Claude Haiku in parallel, with one seat per repo or file.

## Naming
Use `<device4>-<session4>-<model>-<role>`, for example `NWKW-a1b2-terra-fix`.

## Context
At >=40% context usage or after one auto-compaction, write a handoff in `handoffs/active/` of at most 2000 tokens: role, progress, waiting, next, and ledger path. A successor seat resumes it and the old seat stays idle. No slash-reset injection.

## Approval
Merge, force push, deploy, and delete require CEO approval.
