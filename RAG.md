---
id: "manufacturing-ai-week7/RAG"
title: "RAG ingestion"
summary: "RAG ingestion"
domain: "manufacturing-ai"
tags: ["documentation", "repository"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "RAG.md"
lang: "en"
sensitivity: "public"
related: ["README.md"]
repo: "manufacturing-ai-week7"
device_scope: "all"
doc_type: "guide"
source_of_truth: "RAG.md"
---

# RAG ingestion

Index reviewed Markdown sections with stable IDs and source paths. Exclude credentials, generated outputs, binary files, and datasets. See [.ragignore](.ragignore) and [rag-manifest.json](rag-manifest.json).

## Wiki

The topic wiki is in `docs/wiki/`; start at `docs/wiki/index.md` and follow citations to repository sources. Run `python3 scripts/wiki-lint.py` to validate it and `python3 scripts/rag-manifest.py` to regenerate the heading inventory in `docs/_meta/rag-manifest.jsonl`. Embeddings are generated locally outside this repository.
