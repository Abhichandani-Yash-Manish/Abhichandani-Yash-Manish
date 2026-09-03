# Editorial race console — profile design contract

This document protects the README's point of view when projects change. It is intentionally outside the public reading path.

## Brief

- **Subject:** Yash Abhichandani, an engineering student whose Formula 1 interest and systems mindset reinforce each other.
- **Audience:** technical reviewers, developer-community leads, hackathon judges, recruiters, and future collaborators.
- **Job:** establish a memorable identity in five seconds, prove technical judgment in sixty, then route the reader to working evidence.
- **Tone:** personal, exact, ambitious, and explainable. Never corporate theatre.

## Design thesis

The profile is a GitHub README first and an editorial race console second.

Native Markdown carries the argument. One animated hero establishes identity; two real product loops prove motion; two static captures slow the page down where evidence matters more than spectacle. Formula 1 language communicates hierarchy and personal taste—it does not rename every ordinary software concept.

## Visual system

| Token | Value | Use |
|:--|:--|:--|
| Asphalt | `#080A0D` | Hero ground |
| Graphite | `#0D1117` | Primary technical surface |
| Warm white | `#F2F0EA` | Identity and readable type |
| Racing red | `#FF304A` | Callsign, starting lights, consequential emphasis |
| Telemetry cyan | `#5ED7E8` | Live/system signal |
| Steel | `#69717C` | Utility copy |
| Hairline | `#222832` | Structure without visual noise |

The hero is always dark so its identity remains stable in GitHub light and dark themes. Everything below it uses GitHub's native theme.

## Signature risk

The 1200×320 hero stages a calm nine-second sequence:

1. Five starting lights illuminate.
2. A telemetry/circuit line draws across the frame.
3. The name and callsign resolve.
4. The capability line settles into a readable final state.

If animation is unsupported, the SVG is still legible. `prefers-reduced-motion` removes every transition and exposes the final composition.

## Motion and media budget

- Exactly one animated SVG hero.
- Exactly two six-second product GIFs, captured from public applications.
- GIF canvas: 960×540 at 10 FPS.
- Maximum loop size: 2.5 MB each.
- Maximum total local media: 8 MB.
- Every GIF has a static PNG fallback selected by reduced-motion media preference.
- Turnout Lab and PRISM IEMS remain static evidence captures.

## Content rules

1. Keep the personal opening about clocks, messy data, hackathons, and Formula 1.
2. Feature four projects deeply and keep the garage to four compact entries.
3. Give every featured project one mission, one technology line, one meaningful decision, and live/source evidence.
4. Put secondary detail behind one native `<details>` debrief.
5. Audit claims against the linked repository or deployed product.
6. Report measured ML performance honestly, including weak or modest signal.
7. Do not use activity widgets, generic badge walls, fabricated statistics, or percentage skill bars.
8. Do not use official Formula 1 or team logos in custom profile artwork.
9. When a stronger project arrives, replace an entry instead of extending the page indefinitely.
10. Regenerate the hero with `python3 scripts/build_visuals.py`; do not hand-edit the generated SVG.

## Maintenance gate

```bash
python3 scripts/build_visuals.py
git diff --exit-code -- assets/editorial-race-hero.svg
python3 scripts/verify_profile.py
python3 scripts/verify_profile.py --network
```

Re-record a loop only when the linked production interface materially changes. Review every deployment, repository name, metric, and contact URL before release.
