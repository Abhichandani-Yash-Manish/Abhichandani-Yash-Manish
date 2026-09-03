#!/usr/bin/env python3
"""Generate assets/hero.svg. Deterministic: same tokens in, byte-identical SVG out.

Never hand-edit the SVG; edit the tokens here and re-run. CI asserts no diff.
Animation is CSS, not SMIL, so `prefers-reduced-motion` can actually switch it
off -- CSS cannot disable SMIL, which would make a reduced-motion claim a lie.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "hero.svg"

W, H = 1200, 320
ASPHALT = "#0A0C10"   # ground; dark in both GitHub themes so identity stays stable
HAIRLINE = "#1B212B"  # structure without noise
WHITE = "#F2F0EA"     # identity
RED = "#FF3040"       # callsign, starting lights
CYAN = "#5ED7E8"      # live / telemetry signal
STEEL = "#6B7480"     # utility copy

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

NAME = "YASH ABHICHANDANI"
CALLSIGN = "CODEDRIFTER_2507"
CAPABILITY = "FULL-STACK PRODUCTS   ·   APPLIED ML   ·   AGENTIC SYSTEMS"
FOOTER = "Gujarat, India   —   Computer Engineering @ DDU  ·  BS Data Science @ IIT Madras"

BASELINE = 262
AMP = 0.60      # keeps the trace inside its own band, clear of the capability line

# Lap-speed profile. Fixed points keep output deterministic.
TRACE = [
    (0, 46), (60, 30), (120, 22), (180, 44), (240, 68), (300, 40),
    (360, 18), (420, 26), (480, 58), (540, 72), (600, 38), (660, 20),
    (720, 30), (780, 62), (840, 50), (900, 24), (960, 34), (1020, 56),
    (1080, 42), (1140, 26), (1200, 34),
]


def trace_path() -> str:
    return "M " + " L ".join(f"{x},{BASELINE - y * AMP:.1f}" for x, y in TRACE)


def lights() -> str:
    """Five starting lights, illuminating left to right."""
    return "".join(
        f'<circle cx="{1136 - (4 - i) * 58}" cy="96" r="13" class="ring"/>'
        f'<circle cx="{1136 - (4 - i) * 58}" cy="96" r="9" class="lit l{i}"/>'
        for i in range(5)
    )


def build() -> str:
    alt = f"{NAME}, callsign {CALLSIGN}. Full-stack products, applied ML, agentic systems."
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{alt}">
<title>{NAME} — {CALLSIGN}</title>
<defs>
<linearGradient id="fade" x1="0" x2="1">
<stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
<stop offset="0.18" stop-color="{CYAN}" stop-opacity="0.85"/>
<stop offset="0.82" stop-color="{CYAN}" stop-opacity="0.85"/>
<stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
</linearGradient>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="6"/></clipPath>
</defs>
<style>
/* Only decoration animates -- never the text. `animation-fill-mode: backwards`
   means an animated element is at its `from` state during its delay, so any
   static rasterization (link preview, social card, thumbnailer) captures t=0.
   Animating the name would render it invisible in every such capture. Lights
   and trace are the only animated elements; all text is always visible. */
.ring {{ fill: none; stroke: {HAIRLINE}; stroke-width: 2; }}
.lit  {{ fill: {RED}; animation: lit .01s linear backwards; }}
.l0 {{ animation-delay: .3s }} .l1 {{ animation-delay: .5s }} .l2 {{ animation-delay: .7s }}
.l3 {{ animation-delay: .9s }} .l4 {{ animation-delay: 1.1s }}
.trace {{ fill: none; stroke: url(#fade); stroke-width: 2; stroke-linejoin: round;
          animation: draw 2.6s cubic-bezier(.2,.7,.3,1) 1.4s backwards; }}
@keyframes lit  {{ from {{ opacity: 0 }} }}
@keyframes draw {{ from {{ stroke-dasharray: 1; stroke-dashoffset: 1 }}
                  to  {{ stroke-dasharray: 1; stroke-dashoffset: 0 }} }}
@media (prefers-reduced-motion: reduce) {{
  .lit, .trace {{ animation: none; }}
}}
</style>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="{ASPHALT}"/>
<line x1="64" y1="208" x2="{W - 64}" y2="208" stroke="{HAIRLINE}" stroke-width="1"/>
<line x1="64" y1="286" x2="{W - 64}" y2="286" stroke="{HAIRLINE}" stroke-width="1"/>
{lights()}
<path class="trace" d="{trace_path()}" pathLength="1"/>
<text x="64" y="94" font-family="{MONO}" font-size="14" letter-spacing="5.5" fill="{RED}">{CALLSIGN}</text>
<text x="64" y="136" font-family="{MONO}" font-size="44" font-weight="700" fill="{WHITE}">{NAME}</text>
<text x="64" y="184" font-family="{MONO}" font-size="16" letter-spacing="2.6" fill="{CYAN}">{CAPABILITY}</text>
<text x="64" y="308" font-family="{MONO}" font-size="13" fill="{STEEL}">{FOOTER}</text>
</g>
</svg>
"""


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote assets/{OUT.name} ({OUT.stat().st_size} bytes)")
