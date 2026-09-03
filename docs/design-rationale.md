# Decision Trace — profile system

This document keeps the profile coherent when projects change. It is not part of the public reading path.

## The brief

- **Subject:** Yash Abhichandani as an engineering student who turns ambiguous problems into inspectable systems.
- **Audience:** technical reviewers, recruiters, hackathon judges, developer-community leads, and potential collaborators.
- **Single job:** prove engineering judgment within one minute, then route the reader to the strongest evidence.

The profile is not a résumé, an activity dashboard, or a technology inventory.

## The thesis

> The decision is part of the deliverable.

The recurring sequence is:

\`\`\`text
OBSERVE → QUESTION → DECIDE → BUILD → VERIFY
\`\`\`

Projects earn space in the decision ledger when they contain a defensible constraint, a consequential decision, and public evidence. Recency or visual polish alone is not enough.

## Visual system

| Token | Light | Dark | Use |
|:--|:--|:--|:--|
| Canvas | \`#F3F7FA\` | \`#0C1B2A\` | Cool engineering-paper surface |
| Ink | \`#10243C\` | \`#F4F8FB\` | Primary type |
| Signal | \`#2D6CDF\` | \`#73A2FF\` | Trace and navigation |
| Decision | \`#FF705D\` | \`#FF806D\` | The consequential choice |
| Verification | \`#178F7F\` | \`#2CB4A1\` | Tested outcome |
| Grid | \`#D8E5EC\` | \`#1B3850\` | Measurement context |

The hero uses a condensed system-font stack for the name, the platform UI stack for prose, and a monospace stack only for recorder labels. No external font or image provider is required.

## The one aesthetic risk

The hero treats the engineering method as a telemetry trace. It animates once from observation to verification and remains fully legible without animation. Formula 1 influences the visual grammar, but does not become the profile's subject.

Everything below the hero stays quiet: native Markdown headings, tables, prose, and links. There are no statistic widgets, skill-logo walls, trophies, contribution snakes, or decorative badges.

## Content rules

1. Lead with two decision-led case studies, not six equal cards.
2. Link capabilities to repositories, tests, artifacts, or live journeys.
3. Say “explores” when a secondary project has not received a current implementation audit.
4. Do not call a prototype production-ready.
5. Do not publish a number that cannot be reproduced from the linked repository.
6. Keep current-focus text broad enough to remain true for several months.
7. When a stronger project arrives, replace a ledger entry; do not endlessly extend the README.

## Maintenance

Review the profile when:

- a flagship project becomes runnable or stops being runnable;
- a repository is renamed;
- a deployment URL changes;
- a technical claim changes;
- the current focus materially changes.

Run:

\`\`\`bash
python3 scripts/verify_profile.py
python3 scripts/verify_profile.py --network
\`\`\`

The second command performs best-effort external-link checks. LinkedIn is deliberately skipped because it rejects automated requests.
