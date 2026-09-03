#!/usr/bin/env python3
"""Validate the profile's structure, media budget, and public evidence links."""

from __future__ import annotations

import argparse
import re
import struct
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets"
EXTERNAL_URL = re.compile(r"""https?://[^\s)>\"']+""")
HTML_LOCAL_ASSET = re.compile(
    r"""(?:src|srcset)=[\"'](?P<path>\.?\.?/[^\"'#?]+)[\"']""",
    re.IGNORECASE,
)

REQUIRED_TEXT = (
    "01 / initialize",
    "02 / featured builds",
    "03 / engineering telemetry",
    "04 / garage",
    "05 / team flight log",
    "06 / open channel",
    "i am happiest when the clock is running",
    "all 100 official test records overlapped training",
    "f1 apex",
    "turnout lab",
    "globetrotter",
    "prism iems",
    "pharmaguard",
    "beos+",
    "cosmic lens",
    "apex simulate",
)
FORBIDDEN_PROVIDERS = (
    "github-readme-stats",
    "streak-stats",
    "skillicons.dev",
    "img.shields.io",
    "platane/snk",
)
NETWORK_SKIP_HOSTS = {"linkedin.com", "www.linkedin.com", "in.linkedin.com"}

EXPECTED_ASSETS = {
    "editorial-race-hero.svg",
    "previews/f1-apex-loop.gif",
    "previews/f1-apex-static.png",
    "previews/globetrotter-loop.gif",
    "previews/globetrotter-static.png",
    "previews/turnout-lab.png",
    "previews/prism-iems.png",
}
EXPECTED_GIFS = {
    "previews/f1-apex-loop.gif",
    "previews/globetrotter-loop.gif",
}
EXPECTED_PNG_SIZE = {
    "previews/f1-apex-static.png": (960, 540),
    "previews/globetrotter-static.png": (960, 540),
    "previews/turnout-lab.png": (1440, 900),
    "previews/prism-iems.png": (2940, 1668),
}
MAX_GIF_BYTES = 2_500_000
MAX_MEDIA_BYTES = 8_000_000


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def referenced_assets(text: str) -> set[Path]:
    found: set[Path] = set()
    for match in HTML_LOCAL_ASSET.finditer(text):
        raw = unquote(match.group("path"))
        found.add((ROOT / raw).resolve())
    return found


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as image_file:
        header = image_file.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG header")
    return struct.unpack(">II", header[16:24])


def gif_info(path: Path) -> tuple[int, int, int]:
    """Return logical width, height, and image-frame count without dependencies."""

    data = path.read_bytes()
    if len(data) < 13 or data[:6] not in {b"GIF87a", b"GIF89a"}:
        raise ValueError("invalid GIF header")

    width, height = struct.unpack("<HH", data[6:10])
    packed = data[10]
    cursor = 13
    if packed & 0x80:
        cursor += 3 * (2 ** ((packed & 0x07) + 1))

    def skip_sub_blocks(position: int) -> int:
        while position < len(data):
            block_size = data[position]
            position += 1
            if block_size == 0:
                return position
            position += block_size
        raise ValueError("unterminated GIF data block")

    frames = 0
    while cursor < len(data):
        marker = data[cursor]
        cursor += 1
        if marker == 0x3B:  # trailer
            break
        if marker == 0x21:  # extension
            if cursor >= len(data):
                raise ValueError("truncated GIF extension")
            cursor += 1  # extension label
            cursor = skip_sub_blocks(cursor)
            continue
        if marker != 0x2C:  # image descriptor
            raise ValueError(f"unexpected GIF block marker 0x{marker:02x}")
        frames += 1
        if cursor + 9 > len(data):
            raise ValueError("truncated GIF image descriptor")
        local_packed = data[cursor + 8]
        cursor += 9
        if local_packed & 0x80:
            cursor += 3 * (2 ** ((local_packed & 0x07) + 1))
        if cursor >= len(data):
            raise ValueError("missing GIF LZW code size")
        cursor += 1
        cursor = skip_sub_blocks(cursor)

    return width, height, frames


def validate_network(urls: list[str]) -> list[str]:
    errors: list[str] = []
    for url in urls:
        parsed = urlparse(url)
        if parsed.hostname in NETWORK_SKIP_HOSTS:
            print(f"SKIP: {url} (blocks automated checks)")
            continue
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "github-profile-integrity-check/2.0"},
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
    lowered = text.lower()

    for phrase in REQUIRED_TEXT:
        if phrase not in lowered:
            errors.append(f"required profile phrase is missing: {phrase!r}")
    for provider in FORBIDDEN_PROVIDERS:
        if provider in lowered:
            errors.append(f"template-style external widget is forbidden: {provider}")

    if text.count("<details>") != 4:
        errors.append("each of the four featured builds must have one debrief")
    if text.count('prefers-reduced-motion: reduce') != 2:
        errors.append("both animated product loops need reduced-motion fallbacks")

    references = referenced_assets(text)
    referenced_relative: set[str] = set()
    for path in sorted(references):
        if not path.is_relative_to(ASSETS):
            errors.append(f"local media reference escapes assets/: {path}")
            continue
        relative = path.relative_to(ASSETS).as_posix()
        referenced_relative.add(relative)
        if not path.exists():
            errors.append(f"local media reference does not exist: assets/{relative}")

    if referenced_relative != EXPECTED_ASSETS:
        errors.append(
            "README media set differs from the editorial system: "
            f"missing={sorted(EXPECTED_ASSETS - referenced_relative)}, "
            f"unexpected={sorted(referenced_relative - EXPECTED_ASSETS)}"
        )

    present_assets = {
        path.relative_to(ASSETS).as_posix()
        for path in ASSETS.rglob("*")
        if path.is_file()
    }
    if present_assets != EXPECTED_ASSETS:
        errors.append(
            "repository contains stale or missing profile media: "
            f"missing={sorted(EXPECTED_ASSETS - present_assets)}, "
            f"stale={sorted(present_assets - EXPECTED_ASSETS)}"
        )

    hero = ASSETS / "editorial-race-hero.svg"
    if hero.exists():
        try:
            root = ET.parse(hero).getroot()
            if not root.tag.endswith("svg"):
                errors.append("hero asset does not have an SVG root")
            if root.attrib.get("width") != "1200" or root.attrib.get("height") != "320":
                errors.append("hero must remain 1200x320")
            children = {child.tag.rsplit("}", 1)[-1] for child in root}
            if not {"title", "desc"}.issubset(children):
                errors.append("hero SVG lacks title and description")
            hero_text = hero.read_text(encoding="utf-8")
            if "prefers-reduced-motion" not in hero_text or "@keyframes" not in hero_text:
                errors.append("hero needs both animation and a reduced-motion state")
        except ET.ParseError as exc:
            errors.append(f"invalid hero SVG: {exc}")

    for relative, expected_size in EXPECTED_PNG_SIZE.items():
        path = ASSETS / relative
        if not path.exists():
            continue
        try:
            actual_size = png_size(path)
            if actual_size != expected_size:
                errors.append(
                    f"assets/{relative} is {actual_size[0]}x{actual_size[1]}, "
                    f"expected {expected_size[0]}x{expected_size[1]}"
                )
        except ValueError as exc:
            errors.append(f"assets/{relative}: {exc}")

    for relative in EXPECTED_GIFS:
        path = ASSETS / relative
        if not path.exists():
            continue
        try:
            width, height, frames = gif_info(path)
            if (width, height) != (960, 540):
                errors.append(f"assets/{relative} must be 960x540, got {width}x{height}")
            if frames < 2:
                errors.append(f"assets/{relative} is not visibly animated")
            if path.stat().st_size >= MAX_GIF_BYTES:
                errors.append(
                    f"assets/{relative} exceeds the 2.5 MB loop budget "
                    f"({path.stat().st_size} bytes)"
                )
        except ValueError as exc:
            errors.append(f"assets/{relative}: {exc}")

    total_media_bytes = sum(
        path.stat().st_size for path in ASSETS.rglob("*") if path.is_file()
    )
    if total_media_bytes >= MAX_MEDIA_BYTES:
        errors.append(
            f"profile media exceeds the 8 MB budget ({total_media_bytes} bytes)"
        )

    alt_texts = [
        match.group("alt")
        for match in re.finditer(
            r"""<img\b[^>]*\balt=(?P<quote>[\"'])(?P<alt>.*?)(?P=quote)""",
            text,
            re.IGNORECASE,
        )
    ]
    if len(alt_texts) != 5:
        errors.append(f"expected five accessible visible images, found {len(alt_texts)}")
    if any(len(alt.strip()) < 40 for alt in alt_texts):
        errors.append("every visible image needs meaningful alternative text")

    remote_images = re.findall(
        r"""<img\b[^>]*\bsrc=[\"']https?://""", text, re.IGNORECASE
    )
    if remote_images:
        errors.append("remote image widgets are not allowed")

    urls = sorted({url.rstrip(".,") for url in EXTERNAL_URL.findall(text)})
    if len(urls) < 12:
        errors.append(f"expected at least 12 evidence/contact URLs, found {len(urls)}")
    if args.network:
        errors.extend(validate_network(urls))

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(
        "Profile verified: "
        f"{len(references)} local media references, "
        f"{len(urls)} external evidence/contact URLs, "
        f"{total_media_bytes / 1_000_000:.2f} MB total media."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
