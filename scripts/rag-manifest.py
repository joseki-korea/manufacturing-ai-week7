#!/usr/bin/env python3
"""Build a local, deterministic heading-based Markdown inventory (no embeddings)."""
import fnmatch, hashlib, json, re, subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
patterns = [x.strip() for x in (root / '.ragignore').read_text().splitlines() if x.strip() and not x.lstrip().startswith('#')]
def ignored(path):
    ignored = False
    for pattern in patterns:
        neg = pattern.startswith('!')
        raw = pattern.lstrip('!')
        anchored = raw.startswith('/')
        p = raw.lstrip('/')
        directory = p.endswith('/')
        p = p.rstrip('/')
        parts = path.split('/')
        match = (path == p if anchored and not directory else
                 any(fnmatch.fnmatchcase(part, p) for part in parts[:-1]) if directory and '/' not in p and not anchored else
                 path.startswith(p + '/') if directory else
                 fnmatch.fnmatchcase(path, p) or ('/' not in p and fnmatch.fnmatchcase(parts[-1], p)))
        if match:
            ignored = not neg
    return ignored

def metadata(text):
    data = {}
    if text.startswith('---\n'):
        front = text.split('\n---', 1)[0].splitlines()[1:]
        for line in front:
            m = re.match(r'^(tags|lang|sensitivity):\s*(.*)$', line)
            if m:
                data[m[1]] = m[2].strip().strip("'\"")
    return data

paths = subprocess.check_output(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=root).decode().split('\0')
records = []
for name in sorted(set(paths)):
    if not name.lower().endswith('.md') or ignored(name):
        continue
    path = root / name
    if not path.is_file() or path.is_symlink():
        continue
    text = path.read_text(encoding='utf-8')
    meta = metadata(text)
    if meta.get('sensitivity', '').lower() == 'secret':
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    headings = [(m.start(), m.group(1).strip()) for m in re.finditer(r'^#{1,6}\s+(.+?)\s*$', text, re.M)]
    if not headings:
        headings = [(0, '(document)')]
    for i, (_, heading) in enumerate(headings, 1):
        tags = meta.get('tags', '').strip('[]')
        records.append(dict(id=f'{name}#{i}', path=name, heading=heading, sha8=digest,
                            tags=[x.strip().strip("'\"") for x in tags.split(',') if x.strip()],
                            lang=meta.get('lang') or 'und', sensitivity=meta.get('sensitivity') or 'internal'))
out = root / 'docs/_meta/rag-manifest.jsonl'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(''.join(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n' for row in records), encoding='utf-8')
print(f'{len(records)} chunks')
