---
id: "manufacturing-ai-week7/wiki/schema"
title: "위키 작성 규칙"
summary: "수집, 질의, 검증 절차"
domain: "manufacturing-ai-week7"
tags: ["wiki"]
owner: "repository maintainers"
status: "draft"
created: "2026-11-08"
updated: "2026-11-08"
source: "docs/wiki/SCHEMA.md"
lang: "ko"
sensitivity: "internal"
related: []
---

# 위키 작성 규칙

## Ingest

원본은 저장소의 코드와 문서이며 복사하지 않는다. 주제마다 소문자 kebab-case 파일 하나를 사용하고 필수 정보칸을 채운다. 각 사실에 `[source: 경로#L줄 @sha8]`을 붙인다. sha8은 원본 파일 전체의 SHA-256 앞 8자리다. 비밀, 개인정보, 내부 수치는 위키에 적지 않는다. 수집할 때 목록과 로그를 갱신하고 `python3 scripts/rag-manifest.py`를 실행한다.

## Query

목록에서 주제 페이지를 찾고 인용된 원본의 해당 줄을 확인한다. 근거가 없거나 오래되었다면 답변을 보류한다.

## Lint

`python3 scripts/wiki-lint.py`를 실행하여 정보칸, 인용, 원본 해시, 링크와 목록을 점검한다. 비밀 검사는 별도로 수행한다.

## 페이지 종류

개요, 모듈, 개념, 엔터티, 방법, FAQ를 사용한다. 제목은 의미 단위로 나누고 각 절은 A4 한 장 이내로 유지한다. 표에는 머리줄을, 그림에는 짧은 설명을 둔다.
