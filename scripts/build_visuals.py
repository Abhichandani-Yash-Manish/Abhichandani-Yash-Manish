#!/usr/bin/env python3
"""Build the profile's motorsport engineering visual system."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

C = {
    "carbon": "#03050A",
    "cockpit": "#07101B",
    "panel": "#0B1726",
    "panel2": "#101F31",
    "white": "#F8FBFF",
    "muted": "#8494A8",
    "line": "#1D3045",
    "grid": "#122235",
    "red": "#FF254A",
    "cyan": "#00E5FF",
    "violet": "#9A6CFF",
    "green": "#26E6A4",
    "yellow": "#FFC857",
}


def frame(title: str, description: str, height: int, body: str, *, animated: bool = False) -> str:
    animation = """
      .light { animation: ignite 4.8s ease-in-out infinite; }
      .l1 { animation-delay: 0s; } .l2 { animation-delay: .28s; }
      .l3 { animation-delay: .56s; } .l4 { animation-delay: .84s; }
      .l5 { animation-delay: 1.12s; }
      .trace { stroke-dasharray: 1250; animation: trace 3.2s cubic-bezier(.2,.8,.2,1) both; }
      .pulse { animation: pulse 2.3s ease-in-out infinite; }
      @keyframes ignite {
        0%, 8% { fill: #28101A; filter: none; }
        14%, 52% { fill: #FF254A; filter: url(#redGlow); }
        60%, 100% { fill: #28101A; filter: none; }
      }
      @keyframes trace { from { stroke-dashoffset: 1250; } to { stroke-dashoffset: 0; } }
      @keyframes pulse { 0%, 100% { opacity: .35; } 50% { opacity: 1; } }
      @media (prefers-reduced-motion: reduce) {
        .light { animation: none; fill: #FF254A; }
        .trace, .pulse { animation: none; stroke-dashoffset: 0; opacity: 1; }
      }
    """ if animated else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{C['carbon']}"/>
      <stop offset=".58" stop-color="{C['cockpit']}"/>
      <stop offset="1" stop-color="#17070C"/>
    </linearGradient>
    <linearGradient id="signal" x1="0" x2="1">
      <stop offset="0" stop-color="{C['red']}"/>
      <stop offset=".48" stop-color="{C['violet']}"/>
      <stop offset="1" stop-color="{C['cyan']}"/>
    </linearGradient>
    <pattern id="grid" width="38" height="38" patternUnits="userSpaceOnUse">
      <path d="M38 0H0V38" fill="none" stroke="{C['grid']}" stroke-width="1"/>
    </pattern>
    <pattern id="checks" width="24" height="24" patternUnits="userSpaceOnUse">
      <rect width="12" height="12" fill="{C['white']}"/><rect x="12" y="12" width="12" height="12" fill="{C['white']}"/>
    </pattern>
    <filter id="redGlow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="7" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="cyanGlow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .display {{ font-family: "Arial Narrow", "Avenir Next Condensed", Impact, sans-serif; font-weight: 900; font-stretch: condensed; letter-spacing: -1.4px; }}
      .body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; letter-spacing: 1.25px; }}
      {animation}
    </style>
  </defs>
  <rect width="1200" height="{height}" rx="28" fill="url(#bg)"/>
  <rect x="1" y="1" width="1198" height="{height - 2}" rx="27" fill="none" stroke="{C['line']}" stroke-width="2"/>
  <rect x="20" y="20" width="1160" height="{height - 40}" rx="18" fill="url(#grid)" opacity=".72"/>
  {body}
</svg>
"""


def hero() -> str:
    body = f"""
  <path d="M0 94H1200" stroke="{C['red']}" stroke-width="2" opacity=".85"/>
  <path d="M0 100H1200" stroke="{C['cyan']}" stroke-width="1" opacity=".18"/>
  <path d="M0 0H176L125 94H0Z" fill="url(#checks)" opacity=".13"/>
  <path d="M1200 600H1004L1064 506H1200Z" fill="url(#checks)" opacity=".08"/>

  <text x="54" y="57" class="mono" font-size="13" font-weight="800" fill="{C['cyan']}">PROFILE TELEMETRY / ONLINE</text>
  <circle cx="32" cy="52" r="5" fill="{C['green']}" class="pulse"/>
  <text x="708" y="57" text-anchor="end" class="mono" font-size="12" fill="{C['muted']}">GUJARAT, INDIA · UTC+05:30</text>

  <g transform="translate(760 32)">
    <rect width="378" height="48" rx="24" fill="{C['carbon']}" stroke="{C['line']}"/>
    <g transform="translate(33 24)"><circle class="light l1" r="10" fill="#28101A"/></g>
    <g transform="translate(77 24)"><circle class="light l2" r="10" fill="#28101A"/></g>
    <g transform="translate(121 24)"><circle class="light l3" r="10" fill="#28101A"/></g>
    <g transform="translate(165 24)"><circle class="light l4" r="10" fill="#28101A"/></g>
    <g transform="translate(209 24)"><circle class="light l5" r="10" fill="#28101A"/></g>
    <text x="353" y="29" text-anchor="end" class="mono" font-size="10" font-weight="800" fill="{C['muted']}">READY / 05</text>
  </g>

  <text x="54" y="145" class="mono" font-size="13" font-weight="800" fill="{C['red']}">CALLSIGN / CODEDRIFTER_2507</text>
  <text x="50" y="229" class="display" font-size="88" fill="{C['white']}">LIGHTS OUT.</text>
  <text x="50" y="313" class="display" font-size="88" fill="{C['red']}">SYSTEMS ON.</text>
  <text x="55" y="365" class="body" font-size="25" font-weight="650" fill="{C['white']}">Yash Abhichandani</text>
  <text x="55" y="398" class="body" font-size="18" fill="{C['muted']}">Computer Engineering × Data Science</text>

  <g transform="translate(56 431)">
    <rect width="152" height="34" rx="17" fill="{C['panel2']}" stroke="{C['red']}"/>
    <text x="76" y="22" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">FULL-STACK</text>
    <rect x="164" width="146" height="34" rx="17" fill="{C['panel2']}" stroke="{C['cyan']}"/>
    <text x="237" y="22" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">APPLIED ML</text>
    <rect x="322" width="182" height="34" rx="17" fill="{C['panel2']}" stroke="{C['violet']}"/>
    <text x="413" y="22" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">AGENTIC SYSTEMS</text>
  </g>

  <g transform="translate(690 128)">
    <path d="M103 31C34 68 8 151 54 214C89 262 161 259 204 224C256 181 310 205 350 159C401 99 353 34 288 27C230 21 171-5 103 31Z" fill="none" stroke="{C['line']}" stroke-width="13"/>
    <path class="trace" d="M103 31C34 68 8 151 54 214C89 262 161 259 204 224C256 181 310 205 350 159C401 99 353 34 288 27C230 21 171-5 103 31Z" fill="none" stroke="url(#signal)" stroke-width="4"/>
    <circle cx="103" cy="31" r="9" fill="{C['red']}" filter="url(#redGlow)"/>
    <circle cx="350" cy="159" r="7" fill="{C['cyan']}" filter="url(#cyanGlow)"/>
    <text x="204" y="115" text-anchor="middle" class="display" font-size="46" fill="{C['white']}">Y/A</text>
    <text x="204" y="142" text-anchor="middle" class="mono" font-size="10" fill="{C['muted']}">BUILD / TRACE / VERIFY</text>
  </g>

  <path d="M690 431H1142" stroke="{C['line']}" stroke-width="2"/>
  <g transform="translate(690 454)">
    <text y="0" class="mono" font-size="10" fill="{C['muted']}">CURRENT MODE</text>
    <text y="27" class="display" font-size="24" fill="{C['green']}">SHIP WITH PROOF</text>
    <text x="235" y="0" class="mono" font-size="10" fill="{C['muted']}">FUEL</text>
    <text x="235" y="27" class="display" font-size="24" fill="{C['yellow']}">CURIOSITY</text>
  </g>

  <rect x="50" y="516" width="1092" height="48" rx="8" fill="{C['panel']}" stroke="{C['line']}"/>
  <text x="72" y="547" class="mono" font-size="13" font-weight="850" fill="{C['white']}">I BUILD FAST. <tspan fill="{C['red']}">I REFUSE TO SHIP BLIND.</tspan></text>
  <text x="1120" y="547" text-anchor="end" class="mono" font-size="10" fill="{C['muted']}">SCROLL FOR RACE DATA ↓</text>
"""
    return frame(
        "Lights out. Systems on. Yash Abhichandani.",
        "A motorsport engineering profile for Yash Abhichandani, also known as CodeDrifter 2507. Full-stack systems, applied machine learning, and agentic workflows.",
        600,
        body,
        animated=True,
    )


def strategy() -> str:
    body = f"""
  <text x="48" y="52" class="mono" font-size="12" font-weight="800" fill="{C['red']}">RACE STRATEGY / HOW I BUILD</text>
  <text x="48" y="111" class="display" font-size="48" fill="{C['white']}">NO VANITY LAPS.</text>
  <text x="48" y="147" class="body" font-size="16" fill="{C['muted']}">Speed matters. So do the systems that keep the result honest when pressure arrives.</text>

  <g transform="translate(48 191)">
    <path d="M0 0H1088" stroke="{C['line']}" stroke-width="8" stroke-linecap="round"/>
    <path d="M0 0H1088" stroke="url(#signal)" stroke-width="3" stroke-linecap="round"/>
    <g transform="translate(40)"><circle r="10" fill="{C['red']}"/><text y="39" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">AUDIT DATA</text></g>
    <g transform="translate(310)"><circle r="10" fill="{C['yellow']}"/><text y="39" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">DESIGN CONTRACTS</text></g>
    <g transform="translate(590)"><circle r="10" fill="{C['violet']}"/><text y="39" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">BUILD FALLBACKS</text></g>
    <g transform="translate(850)"><circle r="10" fill="{C['cyan']}"/><text y="39" text-anchor="middle" class="mono" font-size="10" font-weight="800" fill="{C['white']}">TEST JOURNEYS</text></g>
    <g transform="translate(1060)"><circle r="10" fill="{C['green']}"/><text y="39" text-anchor="end" class="mono" font-size="10" font-weight="800" fill="{C['white']}">SHIP PROOF</text></g>
  </g>
"""
    return frame(
        "Race strategy — no vanity laps",
        "Yash's engineering loop: audit data, design contracts, build fallbacks, test real journeys, and ship evidence.",
        260,
        body,
    )


def sector_turnout() -> str:
    body = f"""
  <text x="48" y="50" class="mono" font-size="12" font-weight="850" fill="{C['red']}">SECTOR 01 / MODEL INTEGRITY</text>
  <text x="48" y="108" class="display" font-size="45" fill="{C['white']}">THE PERFECT SCORE WAS A <tspan fill="{C['red']}">RED FLAG.</tspan></text>
  <text x="48" y="144" class="body" font-size="16" fill="{C['muted']}">Turnout Lab found the benchmark leak before the model could exploit it.</text>
  <g transform="translate(48 178)">
    <rect width="248" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="18" y="30" class="display" font-size="28" fill="{C['red']}">100 / 100</text><text x="18" y="54" class="mono" font-size="9" fill="{C['muted']}">TEST ROWS OVERLAPPED</text>
    <rect x="264" width="190" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="282" y="30" class="display" font-size="28" fill="{C['white']}">397</text><text x="282" y="54" class="mono" font-size="9" fill="{C['muted']}">LEAKAGE-SAFE ROWS</text>
    <rect x="470" width="190" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="488" y="30" class="display" font-size="28" fill="{C['cyan']}">25</text><text x="488" y="54" class="mono" font-size="9" fill="{C['muted']}">OUTER CV FOLDS</text>
    <rect x="676" width="190" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="694" y="30" class="display" font-size="28" fill="{C['white']}">0.635</text><text x="694" y="54" class="mono" font-size="9" fill="{C['muted']}">ROC-AUC</text>
    <rect x="882" width="206" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="900" y="30" class="display" font-size="28" fill="{C['green']}">+5.1%</text><text x="900" y="54" class="mono" font-size="9" fill="{C['muted']}">BRIER SKILL</text>
  </g>
"""
    return frame(
        "Sector 01 — Turnout Lab",
        "The perfect score was a red flag. Turnout Lab quarantined 100 overlapping test records and reported leakage-safe grouped evaluation across 25 outer folds.",
        292,
        body,
    )


def sector_globe() -> str:
    body = f"""
  <text x="48" y="50" class="mono" font-size="12" font-weight="850" fill="{C['cyan']}">SECTOR 02 / PRODUCT RESILIENCE</text>
  <text x="48" y="108" class="display" font-size="43" fill="{C['white']}">THE DEMO DOESN'T BREAK WHEN <tspan fill="{C['cyan']}">THE API DOES.</tspan></text>
  <text x="48" y="144" class="body" font-size="16" fill="{C['muted']}">GlobeTrotter keeps the planning journey alive with durable data, keyless maps, and deliberate fallbacks.</text>
  <g transform="translate(48 178)">
    <rect width="220" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="18" y="30" class="display" font-size="28" fill="{C['cyan']}">55</text><text x="18" y="54" class="mono" font-size="9" fill="{C['muted']}">DESTINATION DOSSIERS</text>
    <rect x="236" width="220" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="254" y="30" class="display" font-size="28" fill="{C['violet']}">390</text><text x="254" y="54" class="mono" font-size="9" fill="{C['muted']}">CURATED ACTIVITIES</text>
    <rect x="472" width="180" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="490" y="30" class="display" font-size="28" fill="{C['yellow']}">3</text><text x="490" y="54" class="mono" font-size="9" fill="{C['muted']}">NAV LANGUAGES</text>
    <rect x="668" width="420" height="74" rx="12" fill="{C['panel2']}" stroke="{C['line']}"/>
    <text x="686" y="30" class="display" font-size="25" fill="{C['green']}">ZERO REQUIRED PAID KEYS</text><text x="686" y="54" class="mono" font-size="9" fill="{C['muted']}">CORE JOURNEY REMAINS DEMONSTRABLE</text>
  </g>
"""
    return frame(
        "Sector 02 — GlobeTrotter",
        "The demo does not break when the API does. GlobeTrotter provides 55 destination dossiers, 390 activities, three navigation languages, and no required paid API keys.",
        292,
        body,
    )


def paddock() -> str:
    body = f"""
  <text x="48" y="50" class="mono" font-size="12" font-weight="850" fill="{C['violet']}">PADDOCK / SELECTED BUILDS</text>
  <text x="48" y="108" class="display" font-size="44" fill="{C['white']}">DIFFERENT SYSTEMS. SAME STANDARD.</text>
  <text x="48" y="142" class="body" font-size="16" fill="{C['muted']}">Every project below has a different failure mode—and a public trail you can inspect.</text>
  <g transform="translate(48 174)">
    <rect width="258" height="58" rx="10" fill="{C['panel2']}" stroke="{C['red']}"/><text x="18" y="25" class="display" font-size="19" fill="{C['white']}">F1 APEX</text><text x="18" y="44" class="mono" font-size="8" fill="{C['muted']}">MOTORSPORT PRODUCT</text>
    <rect x="276" width="258" height="58" rx="10" fill="{C['panel2']}" stroke="{C['cyan']}"/><text x="294" y="25" class="display" font-size="19" fill="{C['white']}">PRISM IEMS</text><text x="294" y="44" class="mono" font-size="8" fill="{C['muted']}">AGENTIC INSTITUTION OPS</text>
    <rect x="552" width="258" height="58" rx="10" fill="{C['panel2']}" stroke="{C['yellow']}"/><text x="570" y="25" class="display" font-size="19" fill="{C['white']}">COSMIC LENS</text><text x="570" y="44" class="mono" font-size="8" fill="{C['muted']}">SCIENTIFIC EXPLORATION</text>
    <rect x="828" width="260" height="58" rx="10" fill="{C['panel2']}" stroke="{C['green']}"/><text x="846" y="25" class="display" font-size="19" fill="{C['white']}">PHARMAGUARD / BEOS+</text><text x="846" y="44" class="mono" font-size="8" fill="{C['muted']}">PUBLIC-IMPACT SYSTEMS</text>
  </g>
"""
    return frame(
        "The paddock — selected builds",
        "Selected systems across motorsport, agentic institution operations, scientific exploration, pharmacy operations, and blood emergency coordination.",
        270,
        body,
    )


def pit_crew() -> str:
    body = f"""
  <text x="48" y="50" class="mono" font-size="12" font-weight="850" fill="{C['yellow']}">PIT CREW / TECHNOLOGY UNDER THE BODYWORK</text>
  <text x="48" y="103" class="display" font-size="39" fill="{C['white']}">TOOLS CHANGE. THE ENGINEERING LOOP DOESN'T.</text>
  <g transform="translate(48 140)">
    <rect width="252" height="136" rx="14" fill="{C['panel2']}" stroke="{C['red']}"/>
    <text x="18" y="29" class="mono" font-size="10" font-weight="850" fill="{C['red']}">01 / PRODUCT</text>
    <text x="18" y="61" class="display" font-size="21" fill="{C['white']}">TYPESCRIPT · REACT</text><text x="18" y="86" class="display" font-size="21" fill="{C['white']}">NEXT.JS · PRISMA</text><text x="18" y="113" class="mono" font-size="9" fill="{C['muted']}">AUTH · STATE · PERSISTENCE</text>
    <rect x="270" width="252" height="136" rx="14" fill="{C['panel2']}" stroke="{C['cyan']}"/>
    <text x="288" y="29" class="mono" font-size="10" font-weight="850" fill="{C['cyan']}">02 / INTELLIGENCE</text>
    <text x="288" y="61" class="display" font-size="21" fill="{C['white']}">PYTHON · SCIKIT</text><text x="288" y="86" class="display" font-size="21" fill="{C['white']}">LANGGRAPH · RAG</text><text x="288" y="113" class="mono" font-size="9" fill="{C['muted']}">CALIBRATION · EVALUATION</text>
    <rect x="540" width="252" height="136" rx="14" fill="{C['panel2']}" stroke="{C['violet']}"/>
    <text x="558" y="29" class="mono" font-size="10" font-weight="850" fill="{C['violet']}">03 / DATA</text>
    <text x="558" y="61" class="display" font-size="21" fill="{C['white']}">POSTGRES · SQLITE</text><text x="558" y="86" class="display" font-size="21" fill="{C['white']}">SUPABASE · TURSO</text><text x="558" y="113" class="mono" font-size="9" fill="{C['muted']}">SCHEMAS · MIGRATIONS · AUDIT</text>
    <rect x="810" width="278" height="136" rx="14" fill="{C['panel2']}" stroke="{C['green']}"/>
    <text x="828" y="29" class="mono" font-size="10" font-weight="850" fill="{C['green']}">04 / DELIVERY</text>
    <text x="828" y="61" class="display" font-size="21" fill="{C['white']}">GIT · CI · VERCEL</text><text x="828" y="86" class="display" font-size="21" fill="{C['white']}">DOCKER · BROWSER QA</text><text x="828" y="113" class="mono" font-size="9" fill="{C['muted']}">REPRODUCIBLE · TESTED · SHIPPED</text>
  </g>
  <text x="48" y="318" class="mono" font-size="10" fill="{C['muted']}">NO PERCENTAGE BARS. FOLLOW THE CODE, TESTS, ARTIFACTS, AND LIVE JOURNEYS.</text>
"""
    return frame(
        "Pit crew — technology under the bodywork",
        "A capability map across product engineering, intelligent systems, data, and delivery. Claims point to inspectable code and live systems instead of skill percentages.",
        350,
        body,
    )


def radio() -> str:
    body = f"""
  <path d="M48 46H60V196H48" fill="none" stroke="{C['red']}" stroke-width="7"/>
  <circle cx="93" cy="59" r="6" fill="{C['green']}" class="pulse"/>
  <text x="112" y="64" class="mono" font-size="12" font-weight="850" fill="{C['green']}">TEAM RADIO / CHANNEL OPEN</text>
  <text x="80" y="123" class="display" font-size="42" fill="{C['white']}">BRING THE AMBITIOUS IDEA.</text>
  <text x="80" y="166" class="display" font-size="42" fill="{C['red']}">I'LL BRING THE SYSTEM QUESTIONS.</text>
  <text x="80" y="208" class="mono" font-size="10" fill="{C['muted']}">BUILT UNDER PRESSURE · EXPLAINED AFTER THE CHEQUERED FLAG</text>
  <path d="M820 197H1140" stroke="url(#signal)" stroke-width="4"/>
"""
    return frame(
        "Team radio — channel open",
        "Bring the ambitious idea. I will bring the system questions. Built under pressure and explained after the chequered flag.",
        240,
        body,
        animated=True,
    )


BUILDERS = {
    "hero": hero,
    "race-strategy": strategy,
    "sector-turnout": sector_turnout,
    "sector-globetrotter": sector_globe,
    "paddock": paddock,
    "pit-crew": pit_crew,
    "team-radio": radio,
}


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    for generated in ASSETS.glob("*.svg"):
        generated.unlink()
    for name, builder in BUILDERS.items():
        destination = ASSETS / f"{name}.svg"
        destination.write_text(builder(), encoding="utf-8")
        print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
