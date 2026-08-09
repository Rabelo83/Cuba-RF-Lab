# Research

<span class="status-badge status-concept">Research in progress</span>

Research claims must be sourced. Public assumptions are useful, but they are not final engineering facts until verified.

Research and simulations should move the project toward a low-cost public solution for Cuban blackout conditions. Track production cost, repairability, and local substitution alongside RF performance.

Current mode: local owner-side measurements are not available. Research must rely on dated public sources, manufacturer data, conservative assumptions, and scenario modeling until an external collaborator contributes field measurements.

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

This priority is a working baseline. It must be verified with current sources now and local measurements later if a collaborator can provide them.

Until local measurements exist, treat this priority as a scenario set rather than a confirmed local truth.

The preliminary LPDA is not selected by default. Antenna candidates must be compared with the weighted decision process in the antenna selection framework.

## Research Ledger

All source-backed claims should be entered in [research/sources.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/sources.md).
