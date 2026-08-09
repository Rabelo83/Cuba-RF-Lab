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

## First Simulation Queue

The first pre-simulation worksheet is ready:

- [preliminary antenna geometry](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/calculations/preliminary_antenna_geometry.md)
- [antenna candidate first-pass CSV](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/antenna_candidate_first_pass.csv)
- [NEC first-pass queue](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/simulations/nec/first_pass_queue.md)

Current order:

1. 900 MHz 5-element Yagi seed
2. 1800 MHz 5-element Yagi seed
3. 900 MHz 7-element Yagi seed
4. 1800 MHz 7-element Yagi seed
5. 800-2200 MHz LPDA seed
6. 1800 MHz biquad seed
7. 2100 MHz biquad seed

These are simulation inputs only. They are not approved build dimensions.

## Candidate Ranking

This is a pre-measurement planning rank only.

| Rank | Candidate | Status |
| ---: | --- | --- |
| 1 | 900 MHz high-gain Yagi | Candidate |
| 2 | Broadband LPDA, about 800-2200 MHz | Candidate |
| 3 | Dual-band or nested 900/1800 MHz directional antenna | Candidate |
| 4 | 1800 MHz high-gain Yagi | Candidate |
| 5 | Panel or patch-array concepts | Candidate |
| 6 | Biquad or double-biquad | Candidate |
| 7 | Other passive directional designs | Add only if simulation gives a reason |

This ranking can change after source research, simulation, material review, passive-coupler testing, or blackout measurements.

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
