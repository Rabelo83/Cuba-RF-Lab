# Project State

Date: 2026-08-09

Version: 0.1.0 research baseline

## Known Context

Project owner: Alfredo

Public display name: Cuba RF Lab

Repository name: `ETECSA-RF-Lab`

Target installation: Matanzas, Cuba

Primary need: resilient basic communication during blackouts, especially when the house has solar power but ETECSA/Cubacel cellular and Nauta Hogar infrastructure may be impaired.

Broader public objective: develop a practical solution that can help Cuban people struggling with communication during blackouts, with the lowest practical production cost and good real-world efficiency.

Current data constraint: the project owner cannot collect local measurements or material availability observations from Cuba at this time. Until a local collaborator contributes data, the project must rely on public sources, manufacturer data, calculations, simulations, conservative assumptions, and sensitivity analysis.

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

Current priority assumptions:

- 900 MHz first priority for lower-band resilience
- 1800 MHz second priority for LTE Band 3 performance
- Optional broadband research from about 800 MHz to 2200 MHz

Possible ETECSA behavior during outages includes shutting down 4G or 3G while lower-power or legacy service survives longer. This must eventually be measured locally by a collaborator before any final field-validated claim.

Because local measurement is not currently available, frequency choices must be ranked by current public sources and simulated as scenarios. No band-specific design may be called field validated until local measurements are contributed.

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
- Project roadmap shifted to desktop research and simulation first because owner-side local measurement/material collection is not currently possible.
- Calculation scripts created for wavelength, coax loss, and simple received-signal delta.
- Measurement CSV template created.
- No simulation results yet.
- No CAD files yet.
- No final dimensions yet.
- No approved blueprints yet.
- No antenna topology has been selected for fabrication-ready blueprints.

## Immediate Next Work

1. Verify current ETECSA band information with dated sources.
2. Build a source-backed list of realistic phones, coax, connectors, routers, coupler materials, and antenna materials that may be obtainable by Cuban users.
3. Create conservative link-budget scenarios for phone-first and passive antenna/coupler architectures.
4. Prepare first antenna models for simulation using realistic materials and tolerance ranges.
5. Keep field measurement and local availability data as an external validation gate, not a prerequisite for desktop engineering progress.
