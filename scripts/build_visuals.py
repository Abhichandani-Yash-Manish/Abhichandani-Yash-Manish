#!/usr/bin/env python3
"""Build the profile's light and dark SVG instrument panels."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

PALETTES = {
    "light": {
        "bg": "#F3F7FA",
        "panel": "#E8F0F5",
        "panel2": "#DDE9F0",
        "ink": "#10243C",
        "muted": "#536C7E",
        "grid": "#D2E1E9",
        "line": "#B6CAD6",
        "signal": "#2D6CDF",
        "signal2": "#7158D9",
        "decision": "#FF705D",
        "verify": "#178F7F",
        "white": "#FFFFFF",
    },
    "dark": {
        "bg": "#0C1B2A",
        "panel": "#112A3D",
        "panel2": "#17364B",
        "ink": "#F4F8FB",
        "muted": "#94ACBD",
        "grid": "#1B3850",
        "line": "#2B4C63",
        "signal": "#73A2FF",
        "signal2": "#A58BFF",
        "decision": "#FF806D",
        "verify": "#2CB4A1",
        "white": "#FFFFFF",
    },
}


def shell(title: str, description: str, height: int, p: dict[str, str], body: str, *, animate: bool = False) -> str:
    motion = """
      .draw { stroke-dasharray: 1500; stroke-dashoffset: 0; animation: draw 1.8s cubic-bezier(.2,.75,.25,1) .15s both; }
      .arrive { opacity: 1; animation: arrive .3s ease-out both; }
      .a1 { animation-delay: .35s; } .a2 { animation-delay: .65s; }
      .a3 { animation-delay: .95s; } .a4 { animation-delay: 1.25s; }
      .a5 { animation-delay: 1.55s; }
      .scan { animation: scan 4s ease-in-out infinite; }
      @keyframes draw { from { stroke-dashoffset: 1500; } to { stroke-dashoffset: 0; } }
      @keyframes arrive { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes scan { 0%, 100% { opacity: .15; } 50% { opacity: .65; } }
      @media (prefers-reduced-motion: reduce) {
        .draw, .arrive, .scan { animation: none; opacity: 1; stroke-dashoffset: 0; }
      }
    """ if animate else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{p['grid']}" stroke-width="1"/>
    </pattern>
    <linearGradient id="signalFade" x1="0" x2="1">
      <stop offset="0" stop-color="{p['signal']}"/>
      <stop offset=".58" stop-color="{p['signal2']}"/>
      <stop offset="1" stop-color="{p['decision']}"/>
    </linearGradient>
    <style>
      .display {{ font-family: "Arial Narrow", "Avenir Next Condensed", "Roboto Condensed", sans-serif; font-weight: 850; letter-spacing: -1.8px; }}
      .body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; letter-spacing: 1.5px; }}
      {motion}
    </style>
  </defs>
  <rect width="1200" height="{height}" rx="32" fill="{p['bg']}"/>
  <rect x="18" y="18" width="1164" height="{height - 36}" rx="22" fill="url(#grid)" opacity=".78"/>
  <rect x="18.5" y="18.5" width="1163" height="{height - 37}" rx="22" fill="none" stroke="{p['line']}"/>
  {body}
</svg>
"""


def hero(p: dict[str, str]) -> str:
    body = f"""
  <path d="M40 78H52V132H40" fill="none" stroke="{p['decision']}" stroke-width="7"/>
  <text x="72" y="82" class="mono" font-size="15" font-weight="750" fill="{p['signal']}">ENGINEERING FLIGHT RECORDER / YAM-PROFILE</text>
  <text x="1128" y="82" class="mono" font-size="14" text-anchor="end" fill="{p['muted']}">GUJARAT · INDIA</text>

  <text x="72" y="168" class="display" font-size="69" fill="{p['ink']}">YASH</text>
  <text x="72" y="236" class="display" font-size="69" fill="{p['ink']}">ABHICHANDANI</text>
  <text x="76" y="282" class="body" font-size="27" font-weight="680" fill="{p['muted']}">I audit the assumption. Then I build the system.</text>
  <rect x="76" y="307" width="470" height="38" rx="19" fill="{p['panel']}"/>
  <text x="96" y="332" class="mono" font-size="13" font-weight="750" fill="{p['signal']}">COMPUTER ENGINEERING × DATA SCIENCE</text>

  <g transform="translate(878 196)">
    <circle r="134" fill="{p['panel']}" stroke="{p['line']}" stroke-width="2"/>
    <circle r="108" fill="none" stroke="{p['grid']}" stroke-width="1"/>
    <circle r="82" fill="none" stroke="{p['signal']}" stroke-width="2" stroke-dasharray="3 10"/>
    <path class="scan" d="M0 0L76-64A100 100 0 0 1 99 14Z" fill="{p['signal']}" opacity=".25"/>
    <path d="M-104 4A104 104 0 0 1 66-81" fill="none" stroke="url(#signalFade)" stroke-width="8" stroke-linecap="round"/>
    <circle cx="-104" cy="4" r="8" fill="{p['decision']}"/>
    <circle cx="66" cy="-81" r="8" fill="{p['verify']}"/>
    <text y="-5" class="display" font-size="59" text-anchor="middle" fill="{p['ink']}">Y/A</text>
    <text y="28" class="mono" font-size="12" font-weight="750" text-anchor="middle" fill="{p['muted']}">SYSTEMS / ML / PRODUCT</text>
  </g>

  <g transform="translate(1026 137)">
    <rect width="102" height="42" rx="8" fill="{p['panel2']}"/>
    <text x="12" y="17" class="mono" font-size="9" fill="{p['muted']}">MODE</text>
    <text x="12" y="33" class="mono" font-size="12" font-weight="800" fill="{p['verify']}">BUILD</text>
  </g>
  <g transform="translate(1026 188)">
    <rect width="102" height="42" rx="8" fill="{p['panel2']}"/>
    <text x="12" y="17" class="mono" font-size="9" fill="{p['muted']}">METHOD</text>
    <text x="12" y="33" class="mono" font-size="12" font-weight="800" fill="{p['signal']}">VERIFY</text>
  </g>
  <g transform="translate(1026 239)">
    <rect width="102" height="42" rx="8" fill="{p['panel2']}"/>
    <text x="12" y="17" class="mono" font-size="9" fill="{p['muted']}">STATUS</text>
    <text x="12" y="33" class="mono" font-size="12" font-weight="800" fill="{p['decision']}">CURIOUS</text>
  </g>

  <path d="M72 421H226L262 387H417L460 431H622L670 374H828L873 416H1128" fill="none" stroke="{p['line']}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path class="draw" d="M72 421H226L262 387H417L460 431H622L670 374H828L873 416H1128" fill="none" stroke="url(#signalFade)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>

  <g class="arrive a1"><circle cx="112" cy="421" r="9" fill="{p['bg']}" stroke="{p['signal']}" stroke-width="4"/><text x="112" y="470" class="mono" font-size="12" font-weight="800" text-anchor="middle" fill="{p['muted']}">OBSERVE</text></g>
  <g class="arrive a2"><circle cx="307" cy="387" r="9" fill="{p['bg']}" stroke="{p['signal']}" stroke-width="4"/><text x="307" y="470" class="mono" font-size="12" font-weight="800" text-anchor="middle" fill="{p['muted']}">QUESTION</text></g>
  <g class="arrive a3"><circle cx="536" cy="431" r="10" fill="{p['decision']}" stroke="{p['bg']}" stroke-width="4"/><text x="536" y="470" class="mono" font-size="12" font-weight="850" text-anchor="middle" fill="{p['decision']}">DECIDE</text></g>
  <g class="arrive a4"><circle cx="748" cy="374" r="9" fill="{p['bg']}" stroke="{p['signal2']}" stroke-width="4"/><text x="748" y="470" class="mono" font-size="12" font-weight="800" text-anchor="middle" fill="{p['muted']}">BUILD</text></g>
  <g class="arrive a5"><circle cx="1011" cy="416" r="10" fill="{p['verify']}" stroke="{p['bg']}" stroke-width="4"/><text x="1011" y="470" class="mono" font-size="12" font-weight="850" text-anchor="middle" fill="{p['verify']}">VERIFY</text></g>
  <text x="1128" y="510" class="mono" font-size="10" text-anchor="end" fill="{p['muted']}">THE DECISION IS PART OF THE DELIVERABLE</text>
"""
    return shell(
        "Yash Abhichandani — Engineering Flight Recorder",
        "I audit the assumption, then I build the system. Computer Engineering and Data Science.",
        540,
        p,
        body,
        animate=True,
    )


def principles(p: dict[str, str]) -> str:
    body = f"""
  <text x="58" y="65" class="mono" font-size="14" font-weight="800" fill="{p['signal']}">OPERATING SYSTEM / FOUR NON-NEGOTIABLES</text>
  <text x="1142" y="65" class="mono" font-size="12" text-anchor="end" fill="{p['muted']}">PROOF &gt; THEATRE</text>
  <path d="M58 88H1142" stroke="{p['line']}" stroke-width="2"/>

  <g transform="translate(58 112)">
    <rect width="252" height="105" rx="15" fill="{p['panel']}"/>
    <text x="20" y="36" class="mono" font-size="12" font-weight="800" fill="{p['decision']}">01 / DATA</text>
    <text x="20" y="72" class="display" font-size="28" fill="{p['ink']}">BEFORE MODEL</text>
  </g>
  <g transform="translate(326 112)">
    <rect width="252" height="105" rx="15" fill="{p['panel']}"/>
    <text x="20" y="36" class="mono" font-size="12" font-weight="800" fill="{p['signal']}">02 / CONTRACTS</text>
    <text x="20" y="72" class="display" font-size="28" fill="{p['ink']}">BEFORE SCREENS</text>
  </g>
  <g transform="translate(594 112)">
    <rect width="252" height="105" rx="15" fill="{p['panel']}"/>
    <text x="20" y="36" class="mono" font-size="12" font-weight="800" fill="{p['signal2']}">03 / FALLBACKS</text>
    <text x="20" y="72" class="display" font-size="28" fill="{p['ink']}">BEFORE DEMOS</text>
  </g>
  <g transform="translate(862 112)">
    <rect width="280" height="105" rx="15" fill="{p['panel']}"/>
    <text x="20" y="36" class="mono" font-size="12" font-weight="800" fill="{p['verify']}">04 / EVIDENCE</text>
    <text x="20" y="72" class="display" font-size="28" fill="{p['ink']}">BEFORE CLAIMS</text>
  </g>
  <path d="M80 236H1120" stroke="url(#signalFade)" stroke-width="5" stroke-linecap="round"/>
"""
    return shell(
        "Operating system — four non-negotiables",
        "Data before model, contracts before screens, fallbacks before demos, evidence before claims.",
        270,
        p,
        body,
    )


def turnout(p: dict[str, str]) -> str:
    body = f"""
  <text x="58" y="65" class="mono" font-size="14" font-weight="800" fill="{p['decision']}">FEATURED TRACE / 01 / APPLIED ML</text>
  <text x="58" y="123" class="display" font-size="50" fill="{p['ink']}">TURNOUT LAB</text>
  <text x="58" y="169" class="display" font-size="35" fill="{p['decision']}">WHEN THE BENCHMARK WAS THE BUG.</text>

  <g transform="translate(58 207)">
    <rect width="630" height="142" rx="18" fill="{p['panel']}"/>
    <path d="M42 71H142M190 71H290M338 71H438M486 71H586" stroke="{p['line']}" stroke-width="5" stroke-linecap="round"/>
    <g transform="translate(42 36)"><circle cx="0" cy="35" r="18" fill="{p['decision']}"/><text x="0" y="41" class="mono" font-size="12" font-weight="900" text-anchor="middle" fill="{p['white']}">!</text><text x="0" y="105" class="mono" font-size="11" font-weight="800" text-anchor="start" fill="{p['muted']}">OVERLAP</text></g>
    <g transform="translate(190 36)"><circle cx="0" cy="35" r="18" fill="{p['bg']}" stroke="{p['signal']}" stroke-width="4"/><text x="0" y="41" class="mono" font-size="11" font-weight="900" text-anchor="middle" fill="{p['signal']}">Q</text><text x="0" y="105" class="mono" font-size="11" font-weight="800" text-anchor="start" fill="{p['muted']}">QUARANTINE</text></g>
    <g transform="translate(338 36)"><circle cx="0" cy="35" r="18" fill="{p['bg']}" stroke="{p['signal2']}" stroke-width="4"/><text x="0" y="41" class="mono" font-size="10" font-weight="900" text-anchor="middle" fill="{p['signal2']}">CV</text><text x="0" y="105" class="mono" font-size="11" font-weight="800" text-anchor="start" fill="{p['muted']}">GROUPED OOF</text></g>
    <g transform="translate(486 36)"><circle cx="0" cy="35" r="18" fill="{p['verify']}"/><text x="0" y="41" class="mono" font-size="11" font-weight="900" text-anchor="middle" fill="{p['white']}">✓</text><text x="0" y="105" class="mono" font-size="11" font-weight="800" text-anchor="start" fill="{p['muted']}">CALIBRATE</text></g>
  </g>

  <g transform="translate(720 52)">
    <rect width="422" height="297" rx="20" fill="{p['panel2']}"/>
    <text x="24" y="38" class="mono" font-size="12" font-weight="800" fill="{p['muted']}">RECORDED EVIDENCE</text>
    <text x="24" y="102" class="display" font-size="49" fill="{p['decision']}">100 / 100</text>
    <text x="26" y="128" class="mono" font-size="11" font-weight="750" fill="{p['muted']}">TEST RECORDS OVERLAPPED TRAINING</text>
    <path d="M24 150H398" stroke="{p['line']}" stroke-width="2"/>
    <text x="24" y="203" class="display" font-size="38" fill="{p['signal']}">25</text>
    <text x="90" y="202" class="mono" font-size="12" font-weight="750" fill="{p['muted']}">OUTER FOLDS</text>
    <text x="24" y="254" class="display" font-size="32" fill="{p['ink']}">0.635</text>
    <text x="144" y="253" class="mono" font-size="11" fill="{p['muted']}">ROC-AUC</text>
    <text x="248" y="254" class="display" font-size="32" fill="{p['ink']}">0.221</text>
    <text x="358" y="253" class="mono" font-size="11" fill="{p['muted']}">BRIER</text>
    <rect x="24" y="270" width="374" height="5" rx="2.5" fill="url(#signalFade)"/>
  </g>

  <text x="58" y="391" class="mono" font-size="13" font-weight="850" fill="{p['verify']}">HONEST SIGNAL &gt; PERFECT STORY</text>
  <text x="1142" y="391" class="mono" font-size="12" font-weight="750" text-anchor="end" fill="{p['muted']}">OPEN CASE FILE →</text>
"""
    return shell(
        "Turnout Lab — when the benchmark was the bug",
        "100 of 100 test records overlapped training. The response was quarantine, grouped validation, and calibrated evaluation across 25 outer folds.",
        430,
        p,
        body,
    )


def globe(p: dict[str, str]) -> str:
    body = f"""
  <text x="58" y="65" class="mono" font-size="14" font-weight="800" fill="{p['signal']}">FEATURED TRACE / 02 / FULL-STACK PRODUCT</text>
  <text x="58" y="123" class="display" font-size="50" fill="{p['ink']}">GLOBETROTTER</text>
  <text x="58" y="169" class="display" font-size="35" fill="{p['signal']}">A TRAVEL PRODUCT THAT SURVIVES THE DEMO.</text>

  <g transform="translate(58 212)">
    <path d="M14 70H163L205 25H363L410 94H567L620 47H768" fill="none" stroke="{p['line']}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M14 70H163L205 25H363L410 94H567L620 47H768" fill="none" stroke="url(#signalFade)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    <g><circle cx="14" cy="70" r="10" fill="{p['decision']}"/><text x="14" y="132" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">IDEA</text></g>
    <g><circle cx="205" cy="25" r="10" fill="{p['bg']}" stroke="{p['signal']}" stroke-width="4"/><text x="205" y="132" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">PLAN</text></g>
    <g><circle cx="410" cy="94" r="10" fill="{p['bg']}" stroke="{p['signal2']}" stroke-width="4"/><text x="410" y="132" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">COLLABORATE</text></g>
    <g><circle cx="620" cy="47" r="10" fill="{p['verify']}"/><text x="620" y="132" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">PUBLISH</text></g>
    <g><circle cx="768" cy="47" r="10" fill="{p['signal']}"/><text x="768" y="132" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">COPY</text></g>
  </g>

  <g transform="translate(862 66)">
    <rect width="280" height="270" rx="20" fill="{p['panel2']}"/>
    <text x="24" y="38" class="mono" font-size="12" font-weight="800" fill="{p['muted']}">PRODUCT PAYLOAD</text>
    <text x="24" y="102" class="display" font-size="49" fill="{p['signal']}">55</text>
    <text x="100" y="100" class="mono" font-size="12" font-weight="750" fill="{p['muted']}">DESTINATIONS</text>
    <text x="24" y="163" class="display" font-size="49" fill="{p['signal2']}">390</text>
    <text x="125" y="161" class="mono" font-size="12" font-weight="750" fill="{p['muted']}">ACTIVITIES</text>
    <text x="24" y="218" class="display" font-size="34" fill="{p['verify']}">3</text>
    <text x="66" y="216" class="mono" font-size="12" font-weight="750" fill="{p['muted']}">NAV LANGUAGES</text>
    <rect x="24" y="234" width="232" height="5" rx="2.5" fill="url(#signalFade)"/>
  </g>

  <rect x="58" y="358" width="498" height="40" rx="20" fill="{p['panel']}"/>
  <text x="82" y="383" class="mono" font-size="12" font-weight="850" fill="{p['verify']}">NO REQUIRED PAID API KEYS / CORE JOURNEY PERSISTS</text>
  <text x="1142" y="383" class="mono" font-size="12" font-weight="750" text-anchor="end" fill="{p['muted']}">LAUNCH WORKSPACE →</text>
"""
    return shell(
        "GlobeTrotter — a travel product that survives the demo",
        "A persistent collaborative travel workspace with 55 destinations, 390 activities, three navigation languages, keyless maps, and no required paid API keys.",
        430,
        p,
        body,
    )


def circuit(p: dict[str, str]) -> str:
    body = f"""
  <text x="58" y="65" class="mono" font-size="14" font-weight="800" fill="{p['signal2']}">BUILD CIRCUIT / SYSTEMS WITH DIFFERENT FAILURE MODES</text>
  <text x="1142" y="65" class="mono" font-size="12" text-anchor="end" fill="{p['muted']}">NO SKILL BARS. FOLLOW THE EVIDENCE.</text>

  <path d="M189 151C96 201 104 348 222 400C370 465 474 361 582 390C728 429 805 484 973 399C1105 332 1088 182 961 140C828 96 734 180 608 147C454 106 318 81 189 151Z" fill="none" stroke="{p['line']}" stroke-width="15" stroke-linecap="round"/>
  <path d="M189 151C96 201 104 348 222 400C370 465 474 361 582 390C728 429 805 484 973 399C1105 332 1088 182 961 140C828 96 734 180 608 147C454 106 318 81 189 151Z" fill="none" stroke="url(#signalFade)" stroke-width="5" stroke-linecap="round" stroke-dasharray="5 12"/>

  <g transform="translate(600 281)">
    <circle r="104" fill="{p['panel2']}" stroke="{p['signal']}" stroke-width="3"/>
    <circle r="80" fill="{p['bg']}" stroke="{p['grid']}" stroke-width="2"/>
    <text y="-8" class="display" font-size="52" text-anchor="middle" fill="{p['ink']}">Y/A</text>
    <text y="24" class="mono" font-size="11" font-weight="800" text-anchor="middle" fill="{p['muted']}">BUILD CORE</text>
    <text y="47" class="mono" font-size="9" text-anchor="middle" fill="{p['verify']}">SYSTEMS / ML / PRODUCT</text>
  </g>

  <g transform="translate(177 145)">
    <circle r="15" fill="{p['decision']}" stroke="{p['bg']}" stroke-width="5"/>
    <rect x="-78" y="27" width="205" height="67" rx="12" fill="{p['panel']}"/>
    <text x="-60" y="55" class="display" font-size="23" fill="{p['ink']}">TURNOUT LAB</text>
    <text x="-60" y="78" class="mono" font-size="10" fill="{p['muted']}">ML INTEGRITY</text>
  </g>
  <g transform="translate(260 402)">
    <circle r="15" fill="{p['signal']}" stroke="{p['bg']}" stroke-width="5"/>
    <rect x="-70" y="-101" width="220" height="67" rx="12" fill="{p['panel']}"/>
    <text x="-52" y="-73" class="display" font-size="23" fill="{p['ink']}">GLOBETROTTER</text>
    <text x="-52" y="-50" class="mono" font-size="10" fill="{p['muted']}">PRODUCT SYSTEMS</text>
  </g>
  <g transform="translate(773 432)">
    <circle r="15" fill="{p['signal2']}" stroke="{p['bg']}" stroke-width="5"/>
    <rect x="-85" y="-103" width="190" height="67" rx="12" fill="{p['panel']}"/>
    <text x="-67" y="-75" class="display" font-size="23" fill="{p['ink']}">PRISM IEMS</text>
    <text x="-67" y="-52" class="mono" font-size="10" fill="{p['muted']}">AGENT WORKFLOWS</text>
  </g>
  <g transform="translate(1020 356)">
    <circle r="15" fill="{p['verify']}" stroke="{p['bg']}" stroke-width="5"/>
    <rect x="-195" y="29" width="243" height="67" rx="12" fill="{p['panel']}"/>
    <text x="-177" y="57" class="display" font-size="23" fill="{p['ink']}">PHARMAGUARD / BEOS+</text>
    <text x="-177" y="80" class="mono" font-size="10" fill="{p['muted']}">PUBLIC-IMPACT SYSTEMS</text>
  </g>
  <g transform="translate(954 139)">
    <circle r="15" fill="{p['signal']}" stroke="{p['bg']}" stroke-width="5"/>
    <rect x="-145" y="28" width="190" height="67" rx="12" fill="{p['panel']}"/>
    <text x="-127" y="56" class="display" font-size="23" fill="{p['ink']}">F1 APEX</text>
    <text x="-127" y="79" class="mono" font-size="10" fill="{p['muted']}">MOTORSPORT PRODUCT</text>
  </g>
"""
    return shell(
        "Build Circuit",
        "A project circuit connecting Turnout Lab, GlobeTrotter, PRISM IEMS, PharmaGuard, BEOS Plus, and F1 Apex to different engineering boundaries.",
        520,
        p,
        body,
    )


def channel(p: dict[str, str]) -> str:
    body = f"""
  <path d="M48 56H60V112H48" fill="none" stroke="{p['verify']}" stroke-width="7"/>
  <text x="82" y="73" class="mono" font-size="14" font-weight="800" fill="{p['verify']}">OPEN CHANNEL / COLLABORATION</text>
  <text x="82" y="137" class="display" font-size="44" fill="{p['ink']}">BRING THE AMBITIOUS IDEA.</text>
  <text x="82" y="181" class="display" font-size="44" fill="{p['signal']}">I'LL BRING THE SYSTEM QUESTIONS.</text>
  <path d="M82 218H1118" stroke="url(#signalFade)" stroke-width="5" stroke-linecap="round"/>
  <text x="82" y="258" class="mono" font-size="12" font-weight="800" fill="{p['muted']}">EMAIL · LINKEDIN · GITHUB</text>
  <text x="1118" y="258" class="mono" font-size="11" text-anchor="end" fill="{p['muted']}">OBSERVE → QUESTION → DECIDE → BUILD → VERIFY</text>
"""
    return shell(
        "Open collaboration channel",
        "Bring the ambitious idea. I will bring the system questions.",
        300,
        p,
        body,
    )


BUILDERS = {
    "hero": hero,
    "operating-system": principles,
    "turnout-trace": turnout,
    "globetrotter-trace": globe,
    "build-circuit": circuit,
    "open-channel": channel,
}


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    for name, builder in BUILDERS.items():
        for theme, palette in PALETTES.items():
            destination = ASSETS / f"{name}-{theme}.svg"
            destination.write_text(builder(palette), encoding="utf-8")
            print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
