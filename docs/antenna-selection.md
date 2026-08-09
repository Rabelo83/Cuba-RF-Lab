# Antenna Selection

<span class="status-badge status-concept">Comparison required</span>
<span class="status-badge status-warning">LPDA is not pre-selected</span>

The project will not assume that the preliminary LPDA idea is the final antenna. It is only one candidate.

The goal is to find the best practical passive antenna system for ETECSA blackout conditions, using comparison, calculation, simulation, and later field testing.

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

[antenna/candidate_comparison.md](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/antenna/candidate_comparison.md)

