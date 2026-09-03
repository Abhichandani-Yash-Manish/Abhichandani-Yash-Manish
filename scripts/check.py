#!/usr/bin/env python3
"""Profile integrity check.

Guards the four things that actually break a profile README:
referenced assets going missing, badge/stat widgets creeping back in,
the media budget ballooning, and links rotting.

    python3 scripts/check.py            # structure + budget
    python3 scripts/check.py --network  # also resolve every external link
"""
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MAX_MEDIA = 1_500_000

# Widget hosts the profile deliberately does not use: badge walls, fake stats,
# skill bars, view counters. Re-adding one should fail loudly, not slip through.
BANNED = ("shields.io", "skillicons.dev", "github-readme-stats", "streak-stats",
          "komarev.com", "github-profile-trophy", "readme-typing-svg",
          "capsule-render", "activity-graph")

# LinkedIn serves 999 to non-browser clients; a failure here would be noise.
SKIP_NETWORK = ("linkedin.com",)

text = README.read_text(encoding="utf-8")
errors = []

# 1. every locally referenced asset exists
local = set(re.findall(r'(?:src|href)="(\./[^"]+)"', text))
for rel in sorted(local):
    if not (ROOT / rel[2:]).is_file():
        errors.append(f"missing asset: {rel}")

# 2. no widget hosts
for host in BANNED:
    if host in text:
        errors.append(f"banned widget host present: {host}")

# 3. media budget
media = [p for p in (ROOT / "assets").rglob("*") if p.is_file()]
total = sum(p.stat().st_size for p in media)
if total > MAX_MEDIA:
    errors.append(f"media {total:,}B exceeds budget {MAX_MEDIA:,}B")

# 4. links resolve (opt-in)
if "--network" in sys.argv:
    urls = sorted(set(re.findall(r'https?://[^\s)"<>]+', text)))
    for url in urls:
        if any(h in url for h in SKIP_NETWORK):
            continue
        try:
            req = Request(url, method="HEAD", headers={"User-Agent": "profile-check"})
            code = urlopen(req, timeout=20).status
        except HTTPError as e:
            code = e.code
        except (URLError, OSError) as e:
            errors.append(f"unreachable: {url} ({e})")
            continue
        if code >= 400:
            errors.append(f"HTTP {code}: {url}")

print(f"assets referenced: {len(local)}   media: {total:,}B / {MAX_MEDIA:,}B")
for e in errors:
    print(f"  FAIL  {e}")
print("OK" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
