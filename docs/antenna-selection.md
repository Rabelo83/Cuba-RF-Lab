# Antenna Selection

<span class="status-badge status-concept">Comparison required</span>
<span class="status-badge status-warning">LPDA is not pre-selected</span>

The project will not assume that the preliminary LPDA idea is the final antenna. It is only one candidate.

The goal is to find the best practical passive antenna system for ETECSA blackout conditions, using comparison, calculation, simulation, and later field testing. The winning design must also be low-cost enough to be useful as a public solution, not only technically impressive.

## Architectures

### Passive Coax/Coupler

```text
ETECSA tower
-> directional antenna
-> coax
-> passive phone coupler
-> ordinary ETECSA phone
```

### Phone At RF Location

```text
ETECSA tower
-> ordinary ETECSA phone at the best RF location
-> USB, Ethernet, or Wi-Fi
-> house network
```

The passive antenna path must beat the simpler phone-at-RF-location path after losses are included.

## Net Improvement Rule

```text
Net RF improvement =
directional antenna gain
- coax loss
- connector loss
- matching loss
- passive coupling loss
- miscellaneous implementation loss
```

Advertised antenna gain alone is not enough.

If two antennas provide similar useful connectivity, choose the one with lower production cost, easier repair, simpler tools, and better local substitution options.

## Current Desktop Finding

The first conservative link-budget scenarios show that the passive antenna path is dominated by coax loss and passive-coupler loss.

Current interpretation:

- phone-at-best-RF-location is the baseline to beat
- 900 MHz remains important for blackout resilience, but a 900 MHz passive chain can lose its gain in the coupler and coax
- 1800 MHz passive designs can be physically smaller and may produce a small RF-power win in good cases
- no passive antenna wins on advertised gain alone
- SINR improvement from directionality may still be valuable and must be simulated

Scenario details:

[calculations/desktop_link_budget_scenarios.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/calculations/desktop_link_budget_scenarios.md)

## Simulation Status

<span class="status-badge status-concept">Working Yagi candidates found, both bands</span>
<span class="status-badge status-warning">Matching network still needed</span>

The 900 MHz and 1800 MHz five-element Yagi candidates have now been through NEC2 simulation. The original preliminary geometry seeds failed across their required bands (negative-to-marginal gain, poor match). Rather than guess a second set of dimensions, the director geometry was redesigned using the NEC solver itself as a numerical search objective. The result: both bands now have a working candidate with flat, strong simulated gain (11.1-11.5 dBi) across their full required range. Neither has a matching network yet -- that is the current blocker before either is field-ready, not gain.

Full detail and the complete failed-to-working timeline:

- [Side-by-side comparison and timeline](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/first_pass_yagi_comparison.md) -- start here
- [900 MHz Yagi working candidate](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y900_5el_opt_v2_bw_first_pass.md)
- [1800 MHz Yagi working candidate](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/results/y1800_5el_opt_v2_bw_first_pass.md)
- [preliminary antenna geometry](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/calculations/preliminary_antenna_geometry.md)
- [antenna candidate first-pass CSV](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/antenna_candidate_first_pass.csv)
- [NEC first-pass queue](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/nec/first_pass_queue.md)

These are simulated dimensions, not approved build dimensions -- no matching network, and no other topology has been compared yet.

Current local solver:

- Python `necpp` NEC2 solver installed in `.venv`
- smoke test: `.venv/bin/python scripts/nec_smoke_test.py`
- optional standalone tools `xnec2c`, `nec2c`, and `openEMS` are not installed locally

## Candidate Ranking

This is a pre-measurement planning rank, updated as simulation results come in.

| Rank | Candidate | Status |
| ---: | --- | --- |
| 1 | 1800 MHz 5-element Yagi (NEC-optimized) | Simulated, working, needs matching network -- every required check point stays net-positive even unmatched |
| 2 | 900 MHz 5-element Yagi (NEC-optimized) | Simulated, working, needs matching network -- one required check point (960 MHz) is net-negative unmatched |
| 3 | Broadband LPDA, about 800-2200 MHz | Not yet simulated |
| 4 | Dual-band or nested 900/1800 MHz directional antenna | Not yet simulated |
| 5 | Panel or patch-array concepts | Not yet simulated |
| 6 | Biquad or double-biquad | Not yet simulated |
| 7 | Other passive directional designs | Add only if simulation gives a reason |

This ranking can change after the LPDA and biquad are simulated, matching networks are designed, material review, passive-coupler testing, or blackout measurements.

## Approval Rule

No antenna goes into approved blueprints until it has:

- calculations
- simulation
- documented assumptions
- comparison against other topologies
- construction tolerances
- passive-coupler implications
- a written selection reason in `DECISIONS.md`

Detailed framework:

[antenna/candidate_comparison.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/antenna/candidate_comparison.md)
