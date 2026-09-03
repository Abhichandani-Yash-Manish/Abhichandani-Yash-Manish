#!/usr/bin/env python3
"""Validate the local integrity and deliberate constraints of the profile README."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LOCAL_REFERENCE = re.compile(
    r"""(?:src|srcset|href)=["'](?P<html>\.?\.?/[^"'#?]+|\.?[^:"']+\.(?:svg|png|jpg|jpeg|webp))["']"""
    r"""|\[[^\]]*\]\((?P<markdown>\.?\.?/[^)#?]+)\)""",
    re.IGNORECASE,
)
EXTERNAL_URL = re.compile(r"""https?://[^\s)>"']+""")

REQUIRED_TEXT = (
    "Decision ledger",
    "Turnout Lab",
    "GlobeTrotter",
    "Capability, with receipts",
    "OBSERVE → QUESTION → DECIDE → BUILD → VERIFY",
)
FORBIDDEN_PROVIDERS = (
    "github-readme-stats",
    "streak-stats",
    "skillicons.dev",
    "img.shields.io",
    "platane/snk",
)
NETWORK_SKIP_HOSTS = {"linkedin.com", "www.linkedin.com", "in.linkedin.com"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def local_references(text: str) -> set[Path]:
    found: set[Path] = set()
    for match in LOCAL_REFERENCE.finditer(text):
        raw = match.group("html") or match.group("markdown")
        if not raw or raw.startswith(("http://", "https://", "mailto:")):
            continue
        cleaned = unquote(raw).split("#", 1)[0].split("?", 1)[0]
        found.add((ROOT / cleaned).resolve())
    return found


def validate_network(urls: list[str]) -> list[str]:
    errors: list[str] = []
    for url in urls:
        parsed = urlparse(url)
        if parsed.hostname in NETWORK_SKIP_HOSTS:
            print(f"SKIP: {url} (blocks automated checks)")
            continue
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "github-profile-integrity-check/1.0"},
            method="HEAD",
        )
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = response.status
            if status >= 400:
                errors.append(f"{url} returned HTTP {status}")
            else:
                print(f"OK:   {url} ({status})")
        except urllib.error.HTTPError as exc:
            errors.append(f"{url} returned HTTP {exc.code}")
        except (urllib.error.URLError, TimeoutError) as exc:
            errors.append(f"{url} could not be checked: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--network",
        action="store_true",
        help="also perform best-effort checks of external HTTP links",
    )
    args = parser.parse_args()

    errors: list[str] = []
    if not README.exists():
        fail("README.md is missing")
        return 1

    text = README.read_text(encoding="utf-8")

    for phrase in REQUIRED_TEXT:
        if phrase not in text:
            errors.append(f"required profile phrase is missing: {phrase!r}")

    lowered = text.lower()
    for provider in FORBIDDEN_PROVIDERS:
        if provider in lowered:
            errors.append(f"template-style external widget is forbidden: {provider}")

    references = sorted(local_references(text))
    if not references:
        errors.append("README contains no local visual assets")

    for path in references:
        if not path.is_relative_to(ROOT):
            errors.append(f"local reference escapes the repository: {path}")
            continue
        if not path.exists():
            errors.append(f"local reference does not exist: {path.relative_to(ROOT)}")
            continue
        if path.suffix.lower() == ".svg":
            try:
                root = ET.parse(path).getroot()
            except ET.ParseError as exc:
                errors.append(f"invalid SVG {path.relative_to(ROOT)}: {exc}")
                continue
            if not root.tag.endswith("svg"):
                errors.append(f"asset is not an SVG root: {path.relative_to(ROOT)}")

    urls = sorted({url.rstrip(".,") for url in EXTERNAL_URL.findall(text)})
    if len(urls) < 10:
        errors.append(f"expected at least 10 evidence/contact URLs, found {len(urls)}")

    if args.network:
        errors.extend(validate_network(urls))

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(
        f"Profile verified: {len(references)} local assets, "
        f"{len(urls)} external evidence/contact URLs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
