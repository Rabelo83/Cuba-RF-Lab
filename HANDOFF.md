# Handoff

Date: 2026-08-09

The project is Cuba RF Lab. The GitHub repository name remains `ETECSA-RF-Lab`. It aims to improve blackout-resilient communications for a house in Matanzas, Cuba, using legal, low-cost, modular, repairable systems centered on ordinary phones, passive antennas, passive couplers, and data transport by USB, Ethernet, or Wi-Fi.

The broader goal is to offer a useful solution for Cuban people struggling with communication during blackouts. Future research and simulation work should lead toward the lowest practical production cost with useful real-world efficiency, not toward expensive lab-only performance.

Current data constraint: the project owner cannot collect local RF measurements or material availability observations from Cuba at this time. The next phase must rely on public sources, manufacturer data, conservative calculations, simulations, and sensitivity analysis. Field validation remains required before any final public blueprint.

Critical boundary: do not design active cellular repeaters, RF amplifiers, jammers, IMSI catchers, base station emulators, or anything intended to bypass ETECSA controls.

Current strategy has two tracks:

1. Track A: place an ETECSA-compatible Android phone at the best RF location and bring data into the house.
2. Track B: improve a local passive directional antenna plus phone-coupler concept through calculation, simulation, and later external measurement if available.

Priority bands are currently assumed to be 900 MHz and 1800 MHz, with optional research from roughly 800 to 2200 MHz. This still needs current source verification, and later local measurements if a collaborator becomes available.

No buildable antenna blueprint exists yet. Do not create final fabrication dimensions until research, calculations, and simulation are ready.

Current repository state:

- Local git repository initialized on branch `main`.
- GitHub remote: `https://github.com/Rabelo83/ETECSA-RF-Lab.git`.
- Initial project baseline committed and pushed.
- GitHub Pages site configured with MkDocs in `mkdocs.yml`.
- Validation workflow added at `.github/workflows/pages.yml`.
- Expected public site URL: `https://rabelo83.github.io/ETECSA-RF-Lab/`.
- GitHub Pages was observed serving branch/Jekyll output from `README.md`, which looked different from local MkDocs.
- Current fix: commit generated MkDocs static output at repository root and use `.nojekyll`, so branch-based GitHub Pages from `main` matches local.
- Public `Keep It Simple` section added in `docs/keep-it-simple.md`, `docs/simple-path-a-phone.md`, and `docs/simple-path-b-passive.md`.
- `Keep It Simple` is bilingual and intentionally plain-language: blueprints, materials, and build/test steps only for each project path.
- `AGENTS.md` and `docs/collaboration.md` now explain the website publishing workflow and `Keep It Simple` rules for future AI/human contributors.
- Antenna selection must use `antenna/candidate_comparison.md`; the preliminary LPDA is only one candidate and no antenna topology is selected yet.
- The passive antenna/coupler path must be compared against phone-at-RF-location using net RF improvement after coax, connector, matching, passive-coupler, and miscellaneous losses.
- Production cost, repairability, local material substitution, import risk, and real-world usefulness are now top-level constraints.
- A project-wide documentation pass propagated the public mission into requirements, research, routerless, coupler, simulation, calculation, testing, material, legal, CAD, image, data, result, and website-collaboration notes.
- Antenna candidate weighting now gives stronger explicit weight to low production cost and ability to fabricate or repair in Cuba while keeping blackout connectivity as the highest-weight criterion.
- Owner-provided material availability in Cuba should be appended to `data/raw/material_availability_cuba.csv` using the columns in `data/templates/material_availability_cuba.csv`; keep dated rows rather than replacing old observations.
- Owner-side local data collection is not currently possible, so new availability and measurement data should come from public sources or future external collaborators and must be labeled by source class and confidence.
- Starter scripts were run successfully.
- Python compile check passed with `PYTHONPYCACHEPREFIX` set to `/private/tmp/etecsa_rf_lab_pycache` because the default macOS bytecode cache path was outside the writable workspace.
- Site search now indexes bilingual content correctly: `plugins.search.lang` in `mkdocs.yml` is set to `[en, es]` so Spanish terms get proper Lunr stemming (the Spanish and multi-language Lunr modules were already bundled with the theme but unused). Rebuilt and pushed as commit `a2361ac`.
- A suspected mobile-layout overflow bug on the homepage architecture diagram was investigated and ruled out: initial headless-Chrome screenshots looked clipped, but that was a testing artifact (headless Chrome clamps its internal window below ~500px while still saving the screenshot at the requested smaller size). Verified with real Chrome DevTools Protocol mobile emulation (390x844, `mobile: true`) that `document.documentElement.scrollWidth` equals `window.innerWidth` with no overflow. No site change was needed or made for this.
- Remaining known gap in bilingual handling: `<html lang="en">` is hardcoded site-wide even though `Keep It Simple` pages are roughly half Spanish, and no Spanish text is wrapped in `lang="es"`. Not fixed yet; affects screen-reader pronunciation and language-based SEO.

Recommended next task: fill `research/sources.md` and `research/etecsa_network.md` with dated source citations for current ETECSA bands, then create conservative desktop link-budget scenarios for phone-first and passive antenna/coupler paths. Do not wait for local measurements to begin simulation, but do not call any design field validated without them.
