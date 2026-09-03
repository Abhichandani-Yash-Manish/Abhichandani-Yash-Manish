# Pit Wall — profile design system

This document protects the profile's point of view when projects change. It is not part of the public reading path.

## Brief

- **Subject:** Yash Abhichandani, an engineering student whose Formula 1 obsession and systems mindset reinforce each other.
- **Audience:** technical reviewers, developer-community leads, hackathon judges, recruiters, and future collaborators.
- **Single job:** create a memorable identity in five seconds, prove technical judgment in sixty, then route the reader to live evidence.

The profile is not a résumé pasted into Markdown. It is a motorsport engineering dossier.

## Thesis

> I build fast. I refuse to ship blind.

Formula 1 is the organizing grammar, not decoration:

```text
LIGHTS OUT → SECTORS → PADDOCK → PIT CREW → TEAM RADIO
```

The sequence mirrors how a visitor reads the profile: identity, operating method, flagship evidence, project range, capability, contact.

## Visual system

| Token | Value | Use |
|:--|:--|:--|
| Carbon | `#03050A` | Primary surface |
| Cockpit | `#07101B` | Deep-blue technical surface |
| Racing red | `#FF254A` | Consequential decisions and motorsport energy |
| Telemetry cyan | `#00E5FF` | System signals and resilient product work |
| Violet | `#9A6CFF` | Agentic/data-system accents |
| Verification green | `#26E6A4` | Tested or supported outcomes |
| Warm yellow | `#FFC857` | Curiosity, tools, and secondary telemetry |

All generated panels stay dark in both GitHub themes. That is a deliberate identity decision: the profile should feel like the same cockpit in every environment, not a generic light/dark dashboard pair.

## Signature risk

The hero uses an animated five-light gantry and a circuit trace. Motion is concentrated there, remains legible when animation fails, and respects `prefers-reduced-motion`. The rest of the profile is static.

Project screenshots are the primary visual evidence. The custom SVG system supplies narrative and telemetry; it never replaces proof of the actual products.

## Content rules

1. Keep “Lights out. Systems on.” and “I build fast. I refuse to ship blind.” as the identity anchors.
2. F1 terminology must describe real information architecture—not fill empty space.
3. Feature no metric without a reproducible source repository.
4. Use screenshots only from current public builds or repository documentation.
5. Keep two flagship sectors deeper than the rest of the paddock.
6. Label prototypes and experiments honestly; do not imply production readiness.
7. Avoid third-party stat widgets, fake progress meters, contribution theatre, and percentage-based skill bars.
8. When a better project arrives, replace a paddock entry instead of endlessly lengthening the README.
9. Rebuild visuals with `python3 scripts/build_visuals.py`; generated SVGs are not edited by hand.

## Maintenance

Run:

```bash
python3 scripts/build_visuals.py
python3 scripts/verify_profile.py
python3 scripts/verify_profile.py --network
```

Review the content whenever a deployment, repository name, measured metric, or current project status changes.
