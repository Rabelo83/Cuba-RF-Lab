# Research

<span class="status-badge status-concept">Research in progress</span>

Research claims must be sourced. Public assumptions are useful, but they are not final engineering facts until verified.

Research and simulations should move the project toward a low-cost public solution for Cuban blackout conditions. Track production cost, repairability, and local substitution alongside RF performance.

Current mode: local owner-side measurements are temporarily unavailable. Research must rely on dated public sources, manufacturer data, conservative assumptions, and scenario modeling until the owner or a collaborator can contribute field measurements later.

Current desktop baseline added on 2026-08-09:

- Public sources support 900 MHz and 1800 MHz as the main working bands.
- 700 MHz and 2100 MHz remain secondary awareness bands until stronger local or official evidence exists.
- Coax and passive-coupler losses are large enough that passive antenna gain must be evaluated as a complete system.
- The phone-at-best-RF-location architecture remains the baseline to beat.
- The first two queued NEC simulations ran on 2026-08-09: both the 900 MHz and 1800 MHz five-element Yagi seed geometries failed across their required bands.
- An NEC-driven redesign on 2026-08-10 found working replacements for both bands: flat, strong simulated gain across the full required range. A matching network is the next step before either is usable with ordinary coax.
- Python `necpp` NEC2 solver is installed, smoke-tested, and now used for real candidate simulation.

## Priority Research Areas

| Area | Purpose | Repository Source |
| --- | --- | --- |
| ETECSA network | Verify current bands, source classes, and local relevance. | [research/etecsa_network.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/etecsa_network.md) |
| Blackout behavior | Track which services survive long outages. | [research/blackout_behavior.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/blackout_behavior.md) |
| Antennas | Compare LPDA, Yagi, biquad, panel, reflector, and MIMO ideas. | [research/antennas.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/antennas.md) |
| Antenna selection | Rank candidates and compare them against phone-at-RF-location after all passive-system losses. | [antenna/candidate_comparison.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/antenna/candidate_comparison.md) |
| Coax | Compare feedline loss at 900, 1800, and 2100 MHz. | [research/coax.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/coax.md) |
| Passive coupling | Study phone coupler geometries and repeatable test fixtures. | [research/passive_coupling.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/passive_coupling.md) |
| Phone RF | Record available phone model, bands, tethering, and antenna position. | [research/phone_rf.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/phone_rf.md) |
| Cuba import rules | Separate confirmed law, interpretation, uncertainty, and anecdotes. | [research/cuba_import_rules.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/cuba_import_rules.md) |

## Source Classes

| Class | Meaning |
| --- | --- |
| A | official ETECSA |
| B | Cuban government or official publication |
| C | equipment manufacturer |
| D | peer-reviewed or engineering reference |
| E | reputable technical third party |
| F | forum, marketplace, anecdotal, or field observation |

## Current Working Band Priorities

1. 900 MHz
2. 1800 MHz
3. Optional broadband coverage from about 800 MHz to 2200 MHz

This priority is now supported by a first public-source pass, but it must still be verified with local measurements later when the owner or a collaborator can provide them.

Until local measurements exist, treat this priority as a scenario set rather than a confirmed local truth.

The preliminary LPDA is not selected by default. Antenna candidates must be compared with the weighted decision process in the antenna selection framework.

## Current Desktop Link-Budget Finding

The first desktop scenario set indicates that passive antenna/coax/coupler designs are most sensitive to:

- passive-coupler loss
- coax type and length
- matching loss
- whether directivity improves SINR enough to matter

See:

- [Desktop link-budget scenarios](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/calculations/desktop_link_budget_scenarios.md)
- [Processed scenario CSV](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/desktop_link_budget_scenarios.csv)

## Current Antenna Simulation Result

<span class="status-badge status-concept">Working candidates found, both bands</span>
<span class="status-badge status-warning">Matching network still needed</span>

The two highest-priority candidates, a 900 MHz and an 1800 MHz five-element Yagi, were first simulated using the original preliminary geometry seeds. Both failed across their required bands: forward gain was negative-to-marginal and feed VSWR stayed above 11:1 throughout. Rather than guess a second set of dimensions, the director geometry was redesigned using the NEC solver itself as the search objective (a local numerical optimization, not a formula or a recalled published table). The result: both bands now have a working candidate with flat, strong simulated gain (11.1-11.5 dBi) across their entire required range.

The remaining gap is impedance matching, not gain. Neither candidate has a matching network yet, so native VSWR is poor at some frequencies (worst for the 900 MHz candidate, at the top of its band). Designing and simulating that match is the next concrete step. After that, the LPDA and biquad candidates still need their first simulation before any topology can be called a project recommendation.

See:

- [Side-by-side comparison and full timeline](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/first_pass_yagi_comparison.md) -- start here
- [900 MHz Yagi working candidate](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y900_5el_opt_v2_bw_first_pass.md)
- [1800 MHz Yagi working candidate](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y1800_5el_opt_v2_bw_first_pass.md)
- [900 MHz Yagi original seed result (failed, superseded)](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y900_5el_seed_first_pass.md)
- [1800 MHz Yagi original seed result (failed, superseded)](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y1800_5el_seed_first_pass.md)
- [Preliminary antenna geometry](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/calculations/preliminary_antenna_geometry.md)
- [Antenna candidate first-pass CSV](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/antenna_candidate_first_pass.csv)
- [NEC first-pass queue](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/nec/first_pass_queue.md)

## Research Ledger

Public website source links:

- [Sources / Fuentes](sources.md)

Repository source ledger:

- [research/sources.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/sources.md)

All source-backed claims should be entered in the repository source ledger first, then summarized on the public website when they affect engineering decisions.
