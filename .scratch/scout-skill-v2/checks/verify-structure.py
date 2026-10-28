"""Check local Markdown links/anchors in scout v2's maintained surfaces.

No network, credentials, or runtime business records are changed. This checks
navigation, not instruction semantics or external-site availability.
"""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
FILES = sorted((ROOT / '.agents/skills/startup-idea-scout').rglob('*.md')) + [
    ROOT / name for name in [
        'SKILL-MAP.md', 'FOUNDER-PROFILE.md', 'CONTEXT.md',
        'docs/startup-skills/source-catalog.md',
        'docs/startup-skills/research-guide.md',
        'docs/startup-skills/record-guide.md',
        'docs/startup-skills/tools.md',
        'docs/startup-skills/templates/scouting-report.md',
        'docs/startup-skills/templates/opportunity-summary.md',
        '.agents/skills/startup-opportunity-investigator/SKILL.md',
        '.agents/skills/startup-customer-connect/SKILL.md',
        '.scratch/scout-skill-v2/map.md',
        '.scratch/scout-skill-v2/issues/07-update-verify-scout.md',
        '.scratch/scout-skill-v2/checks/scout-v2-verification.md',
    ]
]


def anchors(text):
    found = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(f'{slug}-{count}' if count else slug)
    return found


errors = []
checked = 0
for source in FILES:
    body = source.read_text()
    # Ignore code fences: example generated links are not actual document links.
    body = re.sub(r'^```.*?^```\s*$', '', body, flags=re.M | re.S)
    for raw in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', body):
        if '{{' in raw:
            continue
        url = urlsplit(raw.strip('<>'))
        if url.scheme or url.netloc:
            continue
        target = (source.parent / unquote(url.path)).resolve() if url.path else source
        checked += 1
        if not target.exists():
            errors.append(f'{source.relative_to(ROOT)}: missing {raw}')
        elif url.fragment and target.is_file() and target.suffix == '.md':
            if unquote(url.fragment) not in anchors(target.read_text()):
                errors.append(f'{source.relative_to(ROOT)}: missing anchor {raw}')

for error in errors:
    print(error)
print(f'{len(FILES)} documents; {checked} local links/anchors checked; {len(errors)} errors')
raise SystemExit(bool(errors))
