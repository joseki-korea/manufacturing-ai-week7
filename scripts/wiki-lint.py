#!/usr/bin/env python3
"""Validate wiki front matter, citations, source hashes, links and index coverage."""
import hashlib, re, sys
from pathlib import Path
from urllib.parse import unquote
root = Path(__file__).resolve().parent.parent
wiki = root / 'docs/wiki'
errors = []
required = {'id','title','summary','domain','tags','owner','status','created','updated','source','lang','sensitivity','related'}
citation = re.compile(r'\[source: (.+?)#L(\d+) @([0-9a-f]{8})\]')
pages = sorted((wiki / 'pages').rglob('*.md'))
index = (wiki / 'index.md').read_text(encoding='utf-8')
for page in pages:
    text = page.read_text(encoding='utf-8')
    rel = page.relative_to(wiki).as_posix()
    if f']({rel})' not in index:
        errors.append(f'{rel}: orphan')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        errors.append(f'{rel}: missing front matter'); continue
    fields = dict(re.findall(r'^([a-z]+):\s*(.*)$', match.group(1), re.M))
    missing = required - fields.keys()
    if missing or any(not fields.get(k) for k in required):
        errors.append(f'{rel}: incomplete front matter {sorted(missing)}')
    if fields.get('sensitivity','').strip('"\'').lower() == 'secret':
        errors.append(f'{rel}: secret page')
    body = text[match.end():]
    for number, line in enumerate(body.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if not citation.search(line):
            errors.append(f'{rel}: unsupported line {number}')
    for source, line, digest in citation.findall(body):
        path = root / source
        if not path.is_file() or not path.resolve().is_relative_to(root.resolve()):
            errors.append(f'{rel}: missing source {source}'); continue
        if hashlib.sha256(path.read_bytes()).hexdigest()[:8] != digest:
            errors.append(f'{rel}: stale source {source}')
        if int(line) < 1 or int(line) > len(path.read_text(encoding='utf-8').splitlines()):
            errors.append(f'{rel}: invalid source line {source}:{line}')
for md in [wiki / 'index.md', wiki / 'SCHEMA.md', wiki / 'log.md', *pages]:
    text = md.read_text(encoding='utf-8')
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
        target = unquote(target.split('#', 1)[0])
        if target and not re.match(r'^[a-z]+:', target) and not (md.parent / target).exists():
            errors.append(f'{md.relative_to(root)}: broken link {target}')
if len(re.findall(r'^- \[.*?\]\(pages/[^)]+\.md\)', index, re.M)) != len(pages):
    errors.append('index count differs from pages count')
print('\n'.join(errors) if errors else f'PASS: {len(pages)} pages')
sys.exit(bool(errors))
