# Project State

Date: 2026-08-09

Version: 0.1.0 research baseline

## Known Context

Project owner: Alfredo

Public display name: Cuba RF Lab

Repository name: `Cuba-RF-Lab`

Target installation: Matanzas, Cuba

Primary need: resilient basic communication during blackouts, especially when the house has solar power but ETECSA/Cubacel cellular and Nauta Hogar infrastructure may be impaired.

Broader public objective: develop a practical solution that can help Cuban people struggling with communication during blackouts, with the lowest practical production cost and good real-world efficiency.

Current data constraint: local measurements and material availability observations from Cuba are temporarily unavailable from the project owner. The owner expects to collect information later, but until then the project must rely on public sources, manufacturer data, calculations, simulations, conservative assumptions, and sensitivity analysis.

## Current Engineering Direction

The project is proceeding on two parallel tracks:

1. Track A: place an ordinary ETECSA-compatible phone at the best RF location, then bring data into the house over USB, Ethernet, Wi-Fi, or a bridge.
2. Track B: improve a local passive antenna-plus-phone-coupler concept using calculations, simulation, sourced material constraints, and later external field measurements if available.

## Existing Local Passive Concept

A locally sold passive kit in Matanzas has been observed. It appears to include:

- directional rooftop antenna
- coax cable
- passive phone coupling structure
- wood or nonmetal phone fixture
- ordinary phone placed near the coupler

The listing was described as a 4G antenna and had an approximate observed price of 6000 CUP. This is local feasibility evidence only. It is not technical proof and its dimensions must not be copied as a design.

## Frequency Baseline

Current public-source desktop baseline:

- 900 MHz first priority for lower-band resilience
- 1800 MHz second priority for LTE Band 3 performance
- Optional broadband research from about 800 MHz to 2200 MHz, especially to observe 2100 MHz behavior where relevant
- 700 MHz tracked as a possible lower-band LTE path, but not a first blueprint target yet

Possible ETECSA behavior during outages includes shutting down 4G or 3G while lower-power or legacy service survives longer. This must eventually be measured locally by the owner or a collaborator before any final field-validated claim.

Because local measurement is temporarily unavailable, frequency choices are now ranked by public sources and must be simulated as scenarios. No band-specific design may be called field validated until local measurements are contributed later.

## Current Repository Status

- Documentation baseline created.
- Public GitHub Pages site configured with MkDocs.
- Current live deployment path is branch-based Pages from `main`, using committed static MkDocs output at the repository root.
- Public `Keep It Simple` section added for bilingual plain-language build paths.
- Antenna selection framework added; LPDA is explicitly only one candidate topology.
- Public-benefit and low-production-cost objective added to project constraints.
- Public-production guardrails propagated across requirements, research, routerless architecture, coupler work, simulations, calculations, tests, materials, legal notes, CAD placeholders, images, data, and results documentation.
- Antenna comparison weights updated so low production cost and Cuban fabrication/repairability carry stronger decision weight while blackout connectivity remains the top priority.
- Cuba material availability now has a raw CSV ledger and template so owner-provided local observations can be saved as dated project data.
- Project roadmap shifted to desktop research and simulation first because owner-side local measurement/material collection is temporarily unavailable.
- Calculation scripts created for wavelength, coax loss, and simple received-signal delta.
- First public-source network/coax/passive-coupler source pass completed.
- `research/sources.md` now records source-backed 900 MHz and 1800 MHz baseline evidence plus coax and passive-coupler loss references.
- First desktop link-budget scenario set added in `calculations/desktop_link_budget_scenarios.md` and `data/processed/desktop_link_budget_scenarios.csv`.
- Architecture 2, phone at best RF location, is now explicitly the baseline to beat until passive antenna/coax/coupler losses are proven low enough.
- First pre-simulation antenna geometry seeds added in `calculations/preliminary_antenna_geometry.md` and `calculations/preliminary_antenna_geometry.py`.
- First antenna candidate worksheet added in `data/processed/antenna_candidate_first_pass.csv`.
- First NEC simulation queue added in `simulations/nec/first_pass_queue.md`.
- Python `necpp` 2.2.5 NEC2 solver installed in `.venv`; `scripts/nec_smoke_test.py` passed on 2026-08-09.
- Scientific Python support installed in `.venv`: `numpy`, `pandas`, `matplotlib`, and `scipy`; pinned in `requirements-engineering.txt`.
- Standalone/GUI solvers `xnec2c`, `nec2c`, and `openEMS` were not found in Homebrew/local checks as of 2026-08-09.
- Measurement CSV template created.
- First NEC simulation results are in (2026-08-09): `Y900_5EL_SEED` and `Y1800_5EL_SEED` both fail as seeded across their required bands (negative-to-marginal forward gain, VSWR above 11:1). Solver independently validated as correct.
- First working Yagi candidates found (2026-08-10): an NEC-driven local search (`simulations/nec/optimize_yagi_directors.py`) replaced the failed director geometry and found `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW`, both showing flat 11.1-11.5 dBi gain across their full required bands. Neither has a matching network yet -- native VSWR ranges from about 2.4 to 87.6 depending on frequency and band. See `simulations/results/first_pass_yagi_comparison.md`.
- No CAD files yet.
- No final dimensions yet.
- No approved blueprints yet.
- No antenna topology has been selected for fabrication-ready blueprints.

## Immediate Next Work

1. Design a matching network (gamma or hairpin match) for `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW`, most urgently for the 900 MHz candidate's 960 MHz weak point (-2.40 dBi net today, unmatched), and re-simulate with it in place.
2. Simulate the LPDA and biquad seed candidates (`simulations/nec/first_pass_queue.md` priorities 5-7) so the antenna comparison framework (`antenna/candidate_comparison.md`) has real data for more than one topology.
3. Search for current official ETECSA or Cuban regulatory source text to improve the band and import-rule evidence.
4. Build a source-backed list of realistic phones, coax, connectors, routers, coupler materials, and antenna materials that may be obtainable by Cuban users.
5. Keep field measurement and local availability data as an external validation gate, not a prerequisite for desktop engineering progress.
