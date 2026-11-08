---
id: "manufacturing-ai-week7/CLAUDE"
title: "claude entry point"
summary: "Repository entry point for claude"
domain: "manufacturing-ai-week7"
tags: ["agents"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "CLAUDE.md"
lang: "en"
sensitivity: "internal"
related: ["RULES.md"]
repo: "manufacturing-ai-week7"
device_scope: "all"
doc_type: "entrypoint"
source_of_truth: "CLAUDE.md"
---

# Agent entry point

Read [RULES.md](RULES.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [role](docs/agents/ROLE-claude.md).

## 멀티에이전트 핸드오프·정리·감시·훅 (docs/agents)
- 핸드오프 규칙: [docs/agents/handoffs/README.md](docs/agents/handoffs/README.md)
- 정리 담당: [docs/agents/ROLE-janitor.md](docs/agents/ROLE-janitor.md)
- 감시 담당: [docs/agents/ROLE-watchdog.md](docs/agents/ROLE-watchdog.md)
- 훅 목록: [docs/agents/HOOKS.md](docs/agents/HOOKS.md)

## 규칙 상속 (전역 → 지역)

전역: solucionemos-vault main의 `rules/INDEX.md`, Rule 00·01·02·04와 `~/.claude/CLAUDE.md`, `~/orca/CLAUDE.md`. 지역: [MODEL-SESSION-RULES.md](MODEL-SESSION-RULES.md), [ROLES.md](ROLES.md), [PM.md](PM.md), [ARCHITECTURE.md](ARCHITECTURE.md). 지역 규칙은 이 저장소의 맥락만 추가하며 전역 안전 및 승인 규칙을 완화할 수 없다.
