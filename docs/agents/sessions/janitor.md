---
id: "manufacturing-ai-week7/docs/agents/sessions/janitor"
title: "janitor session"
summary: "janitor session"
domain: "manufacturing-ai"
tags: ["documentation", "repository"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "docs/agents/sessions/janitor.md"
lang: "en"
sensitivity: "public"
related: ["README.md"]
repo: "manufacturing-ai-week7"
device_scope: "all"
doc_type: "guide"
source_of_truth: "docs/agents/sessions/janitor.md"
---

# janitor session

Role: Monitor context usage and recommend handoff and cleanup at the configured threshold.

Input: task and applicable rules.

Output: scoped result and verification evidence.

Forbidden: secrets, unapproved external changes, or self-approval.

Handoff: record status, risks, and next action; see [RULES.md](../../../RULES.md).
