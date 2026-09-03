<div align="center">

<img src="./assets/hero.svg" width="100%" alt="Lights out. Systems on. Yash Abhichandani, CodeDrifter 2507, builds full-stack products, applied machine-learning systems, and agentic workflows. I build fast. I refuse to ship blind." />

<br>

[**ENTER THE PADDOCK**](https://github.com/Abhichandani-Yash-Manish?tab=repositories) &nbsp;·&nbsp; [**OPEN F1 TELEMETRY**](https://apexpredict.live) &nbsp;·&nbsp; [**LINKEDIN**](https://in.linkedin.com/in/yash-abhichandani-dev) &nbsp;·&nbsp; [**TEAM RADIO**](mailto:yashraj2507@gmail.com)

</div>

I am happiest when the clock is running, the data is messy, and the system still has to work. That is probably why I like both **hackathons** and **Formula 1**.

I am **Yash**—a Computer Engineering student at Dharmsinh Desai University and a Data Science student at IIT Madras. I build full-stack products, applied ML systems, and agentic workflows. I care about the parts that usually get hidden after a demo: leaked data, access boundaries, fallback paths, calibrated uncertainty, and whether somebody else can actually run the repository.

<img src="./assets/race-strategy.svg" width="100%" alt="Race strategy: no vanity laps. Audit data, design contracts, build fallbacks, test real journeys, and ship proof." />

<br>

<img src="./assets/sector-turnout.svg" width="100%" alt="Sector 01, model integrity. The perfect score was a red flag. Turnout Lab quarantined complete official test overlap before leakage-safe evaluation." />

<a href="https://github.com/Abhichandani-Yash-Manish/turnout-lab">
  <img src="./assets/showcase/turnout-lab.png" width="100%" alt="Turnout Lab Streamlit decision dashboard showing leakage-safe rows, repeated cross-validation metrics, Brier skill, and a single-registration scoring form." />
</a>

### Turnout Lab // leakage-aware attendance forecasting

The obvious job was to train a classifier. The important discovery was that **all 100 official test records also appeared in training**. I quarantined test-linked identities and feature fingerprints before development, then used group-safe validation, fold-local preprocessing, calibration, threshold diagnostics, and reproducible artifacts.

`397 leakage-safe rows` · `25 outer folds` · `ROC-AUC 0.635` · `Macro-F1 0.584` · `Brier skill +5.1%`

[**OPEN CASE FILE →**](https://github.com/Abhichandani-Yash-Manish/turnout-lab) &nbsp; [Data audit](https://github.com/Abhichandani-Yash-Manish/turnout-lab#data-quality-audit) · [Evaluation](https://github.com/Abhichandani-Yash-Manish/turnout-lab#model-comparison-and-selection) · [Model card](https://github.com/Abhichandani-Yash-Manish/turnout-lab#model-card-and-responsible-use)

<details>
<summary><strong>ENGINEER'S DEBRIEF / why this decision matters</strong></summary>

<br>

A model trained against that official split could look exceptional while measuring memorization. The final system instead reports modest signal honestly, separates attendance probability from input reliability, prevents student IDs from entering the model, and frames no-show risk as a prompt for supportive reminders—not punishment.

The repository includes the audit, executed notebook, repeated out-of-fold diagnostics, deterministic tests, batch scoring, scenario analysis, privacy-aware operational logging, and the exact 100-row submission artifact.

</details>

<br>

<img src="./assets/sector-globetrotter.svg" width="100%" alt="Sector 02, product resilience. The demo does not break when the API does. GlobeTrotter uses durable data and deliberate fallbacks." />

<a href="https://globetrotter-vert-ten.vercel.app">
  <img src="./assets/showcase/globetrotter.png" width="100%" alt="GlobeTrotter route planner showing a multi-city European itinerary, route map, trip budget, dates, and collaborative planning workspace." />
</a>

### GlobeTrotter // the trip survives the refresh

A collaborative workspace that turns a multi-city idea into a dated, costed itinerary that can be edited, checked, shared, published, and copied. The core journey stays demonstrable without paid services: persisted coordinates backstop routing, keyless maps keep geography visible, and dated offline references make currency limitations explicit.

`55 destination dossiers` · `390 activities` · `3 navigation languages` · `0 required paid API keys`

[**LAUNCH WORKSPACE →**](https://globetrotter-vert-ten.vercel.app) &nbsp; [Source](https://github.com/Abhichandani-Yash-Manish/GlobeTrotter) · [Architecture](https://github.com/Abhichandani-Yash-Manish/GlobeTrotter#architecture) · [Verification](https://github.com/Abhichandani-Yash-Manish/GlobeTrotter#verification)

<details>
<summary><strong>ENGINEER'S DEBRIEF / what lives below the interface</strong></summary>

<br>

Role-aware collaboration, invitation tokens, transactional trip copying, budget controls, trip-health checks, persistent SQLite/Turso storage, seeded editorial data, multilingual navigation, and explicit degraded modes. The deployment is part of the evidence; the interface is not a mockup.

</details>

<br>

<img src="./assets/paddock.svg" width="100%" alt="Paddock of selected builds: F1 Apex, PRISM IEMS, Cosmic Lens, PharmaGuard, and BEOS Plus." />

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://apexpredict.live"><img src="./assets/showcase/f1-apex.png" width="100%" alt="F1 Apex telemetry command center with race-session status, prediction controls, next-race countdown, and a dark red motorsport interface." /></a>
      <br><br>
      <strong>F1 APEX // race weekend, engineered</strong><br>
      <sub>Predictions, leagues, standings, rivalries, scoring, and telemetry-oriented interaction—wrapped in the product language that made me want to build it.</sub><br><br>
      <a href="https://apexpredict.live"><strong>LIVE TELEMETRY →</strong></a> · <a href="https://github.com/Abhichandani-Yash-Manish/F1-Prefictor-Vibe_Project">SOURCE</a>
    </td>
    <td width="50%" valign="top">
      <a href="https://prism-iems.vercel.app"><img src="./assets/showcase/prism-iems.png" width="100%" alt="PRISM IEMS institutional war room displaying intervention risks, escalation metrics, and operational decision cards." /></a>
      <br><br>
      <strong>PRISM IEMS // institution ops with guardrails</strong><br>
      <sub>A role-based institutional system exploring observable agent workflows, intervention queues, approval boundaries, and evidence-aware operations.</sub><br><br>
      <a href="https://prism-iems.vercel.app"><strong>OPEN WAR ROOM →</strong></a> · <a href="https://github.com/Abhichandani-Yash-Manish/prism-iems">SOURCE</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://cosmiclens-iota.vercel.app"><img src="./assets/showcase/cosmic-lens.png" width="100%" alt="Cosmic Lens astronomy platform landing page with a star field and navigation for archives, data analysis, infographics, timeline, and community." /></a>
      <br><br>
      <strong>COSMIC LENS // signal in the early universe</strong><br>
      <sub>A team-built astronomy experience for archiving, analysing, visualising, and discussing high-redshift observations.</sub><br><br>
      <a href="https://cosmiclens-iota.vercel.app"><strong>START EXPLORING →</strong></a> · <a href="https://github.com/Abhichandani-Yash-Manish/Cosmic-Lens-by-Team-Void_Pointers">SOURCE</a>
    </td>
    <td width="50%" valign="top">
      <br>
      <code>PUBLIC IMPACT / DOUBLE HEADER</code>
      <h3>PharmaGuard</h3>
      <p>Pharmacy inventory workflows around FEFO dispatch, expiry visibility, alerts, and demand forecasting.</p>
      <a href="https://github.com/Abhichandani-Yash-Manish/Void-Pointers-Aetrix-2026-"><strong>INSPECT PHARMAGUARD →</strong></a>
      <br><br>
      <h3>BEOS+</h3>
      <p>A blood-emergency coordination prototype spanning hospital inventory, live emergency mapping, and donor-alert workflows.</p>
      <a href="https://beos-plus.vercel.app"><strong>OPEN BEOS+ →</strong></a> · <a href="https://github.com/Abhichandani-Yash-Manish/BEOS_PLUS">SOURCE</a>
      <br><br>
      <code>IN THE GARAGE</code>
      <p><a href="https://github.com/Abhichandani-Yash-Manish/apex-simulate"><strong>APEX SIMULATE</strong></a> — strategy-simulation and telemetry-lake experiments.</p>
      <p><a href="https://github.com/Abhichandani-Yash-Manish/ClubAtlas"><strong>CLUBATLAS</strong></a> — a grounded campus-club assistant with safe action boundaries.</p>
    </td>
  </tr>
</table>

<br>

<img src="./assets/pit-crew.svg" width="100%" alt="Pit crew capability map across TypeScript and React products, Python machine learning and RAG, relational data systems, and tested delivery." />

The stack is not the personality. The decisions are. I use **TypeScript, React, Next.js, Python, scikit-learn, LangGraph, SQL, Supabase, Turso, Git, CI, Docker, and browser-level QA** when they earn their place in the system.

<details>
<summary><strong>PIT WALL NOTES / how I work with a team</strong></summary>

<br>

Hackathons taught me to move quickly. Engineering taught me what must remain after the chequered flag: a repository someone else can run, boundaries someone else can explain, a main journey that stays intact while features evolve, and limitations a reviewer does not have to discover by accident.

I like ambitious teams, small testable interfaces, clear ownership, honest demos, and the moment a wild idea becomes a system we can defend.

</details>

<br>

<img src="./assets/team-radio.svg" width="100%" alt="Team radio channel open. Bring the ambitious idea and Yash will bring the system questions." />

<div align="center">

### Yash Abhichandani

Gujarat, India · Computer Engineering × Data Science · Formula 1 brain, engineering hands

[**EMAIL**](mailto:yashraj2507@gmail.com) &nbsp;·&nbsp; [**LINKEDIN**](https://in.linkedin.com/in/yash-abhichandani-dev) &nbsp;·&nbsp; [**ALL REPOSITORIES**](https://github.com/Abhichandani-Yash-Manish?tab=repositories)

<sub>Built under pressure. Explained after the chequered flag.</sub>

</div>
