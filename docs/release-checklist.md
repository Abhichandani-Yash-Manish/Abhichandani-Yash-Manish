# Profile release checklist

## Local integrity

- [ ] `python3 scripts/build_visuals.py` produces no hero diff.
- [ ] `python3 scripts/verify_profile.py` passes.
- [ ] `git diff --check` passes.
- [ ] The asset directory contains one hero, two GIFs, two reduced-motion fallbacks, and two static project captures—nothing else.
- [ ] Both GIFs are 960×540, six seconds, 10 FPS, visibly multi-frame, and below 2.5 MB.
- [ ] Total local README media remains below 8 MB.
- [ ] All project statements still match public repository evidence.

## Render review

- [ ] Hero is readable before, during, and after animation.
- [ ] Reduced-motion mode shows the hero's final state and static product fallbacks.
- [ ] GitHub desktop at 1440 px is checked in light mode.
- [ ] GitHub desktop at 1440 px is checked in dark mode.
- [ ] GitHub mobile at 390 px has no clipped text or unreadable project copy.
- [ ] The project order is F1 Apex, Turnout Lab, GlobeTrotter, PRISM IEMS.
- [ ] There are no remote image widgets, broken media, accidental credentials, or personal demo data.

## Signed-out evidence check

- [ ] [F1 Apex](https://apexpredict.live) opens to the public command center.
- [ ] [Turnout Lab](https://github.com/Abhichandani-Yash-Manish/turnout-lab) exposes the case study and measured artifacts.
- [ ] [GlobeTrotter](https://globetrotter-vert-ten.vercel.app/share/demo-europe-trip) opens the published itinerary without credentials.
- [ ] [PRISM IEMS](https://prism-iems.vercel.app) opens its public entry experience.
- [ ] Every garage source/live link opens.
- [ ] Email and LinkedIn target the intended destinations.

## Pull request boundary

- [ ] GitHub Actions passes on the latest commit.
- [ ] PR title describes the editorial race-console reset.
- [ ] PR body names the content, motion, performance, and verification decisions.
- [ ] The final GitHub-rendered diff is reviewed before approval.
- [ ] `main` remains unchanged until the user approves the PR.
- [ ] Use a squash merge after approval so the rejected visual iterations do not enter `main` as separate commits.

## Optional profile metadata

- [ ] Keep `CodeDrifter_2507` as the callsign while `Yash Abhichandani` remains the primary identity.
- [ ] Suggested bio: `Computer Engineering + IITM Data Science student building full-stack products, honest ML systems, and F1 software.`
- [ ] Suggested pin order: F1 Apex, Turnout Lab, GlobeTrotter, PRISM IEMS, Cosmic Lens, PharmaGuard or BEOS+.
