# Profile design contract

Kept out of the public reading path. Its job is to stop this README being rewritten
a ninth time for reasons that are not content.

## Why this document exists

The profile went through seven redesigns without shipping. Each pass renamed section
headers — `PADDOCK`, `PIT WALL`, `TELEMETRY`, `GARAGE`, `FLIGHT LOG` — rather than
changing what the page said. The naming layer was decorative, and decoration invites
repainting.

**The rule that follows from that:** Formula 1 is identity, not taxonomy. It lives in
the hero, the red accent, the opening paragraph, and the two projects that are
genuinely F1 software. It does not rename ordinary software concepts. Section headers
stay plain English; the `01 /` numbering carries the console feel on its own.

Test before adding any themed label: if renaming it back to plain English loses no
information, it was decoration — don't add it.

## Audience

Hackathon and developer-community readers, plus engineers and potential collaborators.
Not recruiter-first. So the tone is "here is how I build, let's build something,"
and **the engineering decision for each project stays visible in the body** rather than
folded into `<details>`. That visibility is the differentiator; hiding it would make
this one more student README with screenshots.

## Visual system

| Token | Value | Use |
|:--|:--|:--|
| Asphalt | `#0A0C10` | Hero ground |
| Warm white | `#F2F0EA` | Identity and readable type |
| Racing red | `#FF3040` | Callsign, starting lights |
| Telemetry cyan | `#5ED7E8` | Live / system signal |
| Steel | `#6B7480` | Utility copy |
| Hairline | `#1B212B` | Structure without noise |

The hero is always dark so identity stays stable in both GitHub themes. Everything
below it uses GitHub's native theme.

## Media budget

- One generated animated SVG hero, ~3.5 KB.
- Static WebP product captures at 1280×720, roughly 30–50 KB each.
- Total under 1.5 MB, enforced by `scripts/check.py`. Current usage is about 127 KB.
- No GIFs. An earlier revision carried 3.4 MB of loops including a single 1.97 MB GIF;
  the products are live and linkable, and a working link is stronger evidence than a
  loop of one.

## Hero animation

Generated only — never hand-edit `assets/hero.svg`; edit `scripts/hero.py` and re-run.
CI asserts the SVG matches its generator.

Animation is **CSS, not SMIL**, because CSS cannot disable SMIL and a
`prefers-reduced-motion` block over SMIL would be a claim the file does not honor.

**Only decoration animates — never the text.** The lights and the telemetry trace are
the sole animated elements; the name, callsign, capability line, and footer are always
visible.

This is not a stylistic preference. `animation-fill-mode: backwards` holds an element
at its `from` state throughout its delay, so anything that rasterizes the SVG at t=0 —
a link preview, a social card, a thumbnailer, a slow first paint — captures that state.
An earlier revision faded the name in over a 0.15s delay, and a t=0 capture of it showed
an all-but-empty hero with only the callsign readable. Text carries the information;
animating it makes the information conditional on timing.

The decorative sequence resolves in about 3 seconds.

## Content rules

1. Keep the opening about the clock, messy data, hackathons, and Formula 1. It earns
   the theme by tying it to an engineering disposition rather than a hobby.
2. Feature four projects deeply; keep the secondary list to four compact entries.
3. Every featured project gets one purpose line, one technology line, one **visible**
   engineering decision, and live/source evidence.
4. Report measured performance honestly, including weak signal. Turnout Lab's modest
   numbers are the point of Turnout Lab.
5. No activity widgets, badge walls, percentage skill bars, view counters, or
   fabricated statistics. `scripts/check.py` fails the build on the known hosts.
6. No official Formula 1 or team logos in custom artwork.
7. When a stronger project arrives, replace an entry rather than extending the page.
8. Claims must match the linked repository or deployed product.

## Maintenance

```bash
python3 scripts/hero.py                      # regenerate hero
git diff --exit-code -- assets/hero.svg      # must be clean
python3 scripts/check.py                     # assets, widgets, budget
python3 scripts/check.py --network           # link rot (also runs weekly in CI)
```

Render review before merge: desktop 1440 px in **both** light and dark mode, and
mobile 390 px for clipping.

## Profile surface beyond the README

The README's argument is only as credible as the repo grid beneath it. Keep these true:

- Repo names match the product names used here (`apex-predict`, `pharmaguard`,
  `cosmic-lens`).
- Every public repo has a description and topics.
- Pinned order: Apex Predict, Turnout Lab, GlobeTrotter, PRISM IEMS, PharmaGuard,
  Cosmic Lens. **Pins are UI-only** — GitHub exposes no API mutation for them.
- Profile fields (name, website, bio) need the `user` OAuth scope, which the default
  `gh` token does not carry: `gh auth refresh -s user`, or edit in Settings.
