#!/usr/bin/env python3
"""Generate the single editorial-race hero used by the profile README."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
HERO = ASSETS / "editorial-race-hero.svg"

# These belonged to the rejected dashboard-heavy direction. Keeping their removal in
# the generator prevents a later rebuild from accidentally restoring that visual wall.
STALE_GENERATED_ASSETS = (
    "hero.svg",
    "paddock.svg",
    "pit-crew.svg",
    "race-strategy.svg",
    "sector-globetrotter.svg",
    "sector-turnout.svg",
    "team-radio.svg",
)


def build_hero() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-labelledby="title desc">
  <title id="title">Yash Abhichandani — CodeDrifter 2507</title>
  <desc id="desc">An animated editorial motorsport identity card for Yash Abhichandani, a full-stack, applied machine-learning, and agentic-systems builder.</desc>
  <defs>
    <linearGradient id="asphalt" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#080A0D"/>
      <stop offset="0.58" stop-color="#0D1117"/>
      <stop offset="1" stop-color="#16090C"/>
    </linearGradient>
    <linearGradient id="signal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FF304A"/>
      <stop offset="0.56" stop-color="#F2F0EA"/>
      <stop offset="1" stop-color="#5ED7E8"/>
    </linearGradient>
    <pattern id="microGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M36 0H0V36" fill="none" stroke="#151A21" stroke-width="1"/>
    </pattern>
    <filter id="redGlow" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="nameWindow"><rect x="52" y="83" width="850" height="82"/></clipPath>
    <style>
      .display { font-family: "Arial Narrow", "Avenir Next Condensed", Impact, sans-serif; font-weight: 900; letter-spacing: -1.2px; }
      .sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; letter-spacing: 1.15px; }
      .light { fill: #271015; animation: ignite 9s ease-in-out infinite; }
      .light:nth-child(1) { animation-delay: 0s; }
      .light:nth-child(2) { animation-delay: .24s; }
      .light:nth-child(3) { animation-delay: .48s; }
      .light:nth-child(4) { animation-delay: .72s; }
      .light:nth-child(5) { animation-delay: .96s; }
      .trace { stroke-dasharray: 1240; stroke-dashoffset: 1240; animation: trace 9s cubic-bezier(.2,.75,.2,1) infinite; }
      .name { animation: resolve 9s cubic-bezier(.2,.8,.2,1) infinite; }
      .role { animation: settle 9s ease-in-out infinite; }
      .cursor { animation: blink 1.2s steps(1) infinite; }
      @keyframes ignite {
        0%, 5% { fill: #271015; filter: none; }
        9%, 28% { fill: #FF304A; filter: url(#redGlow); }
        33%, 100% { fill: #271015; filter: none; }
      }
      @keyframes trace {
        0%, 24% { stroke-dashoffset: 1240; opacity: .25; }
        43%, 87% { stroke-dashoffset: 0; opacity: 1; }
        100% { stroke-dashoffset: 0; opacity: .25; }
      }
      @keyframes resolve {
        0%, 32% { transform: translateY(52px); opacity: .08; }
        46%, 94% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(0); opacity: .72; }
      }
      @keyframes settle {
        0%, 42% { opacity: .18; }
        55%, 94% { opacity: 1; }
        100% { opacity: .75; }
      }
      @keyframes blink { 0%, 48% { opacity: 1; } 49%, 100% { opacity: .15; } }
      @media (prefers-reduced-motion: reduce) {
        .light { animation: none; fill: #FF304A; filter: none; }
        .trace { animation: none; stroke-dashoffset: 0; opacity: 1; }
        .name, .role, .cursor { animation: none; opacity: 1; transform: none; }
      }
    </style>
  </defs>

  <rect width="1200" height="320" rx="18" fill="url(#asphalt)"/>
  <rect x="1" y="1" width="1198" height="318" rx="17" fill="none" stroke="#222832" stroke-width="2"/>
  <rect x="18" y="18" width="1164" height="284" rx="10" fill="url(#microGrid)" opacity=".78"/>
  <path d="M18 61H1182" stroke="#222832"/>
  <path d="M18 272H1182" stroke="#222832"/>
  <rect x="18" y="18" width="7" height="284" rx="3.5" fill="#FF304A"/>

  <text x="52" y="43" class="mono" font-size="11" font-weight="700" fill="#5ED7E8">DRIVER PROFILE / 01</text>
  <circle cx="935" cy="39" r="4" fill="#55D6A8"/>
  <text x="948" y="43" class="mono" font-size="10" fill="#69717C">SYSTEMS ONLINE</text>
  <text x="1147" y="43" text-anchor="end" class="mono" font-size="10" fill="#69717C">GUJARAT · IN</text>

  <g transform="translate(52 79)">
    <circle class="light" cx="0" cy="0" r="7"/>
    <circle class="light" cx="25" cy="0" r="7"/>
    <circle class="light" cx="50" cy="0" r="7"/>
    <circle class="light" cx="75" cy="0" r="7"/>
    <circle class="light" cx="100" cy="0" r="7"/>
    <text x="126" y="4" class="mono" font-size="9" fill="#69717C">START SEQUENCE</text>
  </g>

  <g clip-path="url(#nameWindow)">
    <text class="display name" x="50" y="151" font-size="66" fill="#F2F0EA">YASH ABHICHANDANI</text>
  </g>
  <text class="mono role" x="55" y="184" font-size="13" font-weight="700" fill="#FF304A">CALLSIGN / CODEDRIFTER_2507</text>
  <text class="sans role" x="53" y="224" font-size="20" font-weight="650" fill="#F2F0EA">FULL-STACK</text>
  <text class="sans role" x="201" y="224" font-size="20" fill="#69717C">·</text>
  <text class="sans role" x="221" y="224" font-size="20" font-weight="650" fill="#F2F0EA">APPLIED ML</text>
  <text class="sans role" x="363" y="224" font-size="20" fill="#69717C">·</text>
  <text class="sans role" x="383" y="224" font-size="20" font-weight="650" fill="#F2F0EA">AGENTIC SYSTEMS</text>

  <path d="M53 249H633L659 230H735L758 255H867L894 211H954L976 232H1146" fill="none" stroke="#222832" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path class="trace" d="M53 249H633L659 230H735L758 255H867L894 211H954L976 232H1146" fill="none" stroke="url(#signal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="1146" cy="232" r="4" fill="#5ED7E8"/>

  <text x="52" y="291" class="mono" font-size="10" fill="#69717C">BUILD / TRACE / VERIFY</text>
  <text x="1148" y="291" text-anchor="end" class="mono" font-size="10" fill="#F2F0EA">TURNING AMBITIOUS IDEAS INTO SYSTEMS PEOPLE CAN USE<tspan class="cursor" fill="#FF304A">_</tspan></text>

  <text x="1153" y="164" text-anchor="end" class="display" font-size="128" fill="none" stroke="#222832" stroke-width="1">2507</text>
</svg>
"""


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    for name in STALE_GENERATED_ASSETS:
        stale = ASSETS / name
        if stale.exists():
            stale.unlink()
    HERO.write_text(build_hero(), encoding="utf-8")
    print(f"wrote {HERO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
