# Antenna Candidate Comparison Framework

Status: PRE-MEASUREMENT FRAMEWORK

Date: 2026-08-09

## Purpose

This file prevents the project from locking onto any single antenna topology too early.

The preliminary 9-element LPDA concept is only one candidate. It is not the final antenna, not the preferred antenna, and not approved build data.

The objective is to discover the best practical passive antenna system for the ETECSA blackout problem, not to validate a previous idea.

## Architectures To Compare

### Architecture 1: Passive Coax/Coupler

```text
ETECSA tower
-> directional antenna
-> coax
-> passive phone coupler
-> ordinary ETECSA phone
```

Any antenna used here must overcome coax, connector, matching, and passive-coupler losses.

### Architecture 2: Phone At RF Location

```text
ETECSA tower
-> ordinary ETECSA phone positioned at the best RF location
-> USB, Ethernet, or Wi-Fi
-> house network
```

This is the baseline architecture. A passive antenna/coupler system must be compared against simply putting the phone where the RF is stronger.

## Net RF Improvement Rule

Do not use advertised antenna gain alone as evidence of better performance.

```text
Net RF improvement =
directional antenna gain
- coax loss
- connector loss
- matching loss
- passive coupling loss
- miscellaneous implementation loss
```

If net RF improvement is not enough to beat the ordinary phone placed at the best RF location, the passive antenna system is not the practical winner.

## First Desktop Link-Budget Screen

The first scenario table is recorded in:

`calculations/desktop_link_budget_scenarios.md`

Current pre-measurement result:

- A good-case 900 MHz passive Yagi chain is approximately break-even versus placing the phone at the same RF location.
- A typical-risk 900 MHz passive chain loses badly if RG-58-class coax and high passive-coupler loss are used.
- A good-case 1800 MHz passive Yagi chain can produce a small RF-power win, but this is not enough by itself to select it.
- A strong 1800 MHz passive win appears possible only with short low-loss coax, low matching loss, a very good passive coupler, and cost/availability proof.
- Directivity may still improve SINR even when net RSRP improvement is small, so simulation must include radiation pattern, beamwidth, front-to-back ratio, and expected interference environment.

Engineering consequence: Architecture 2 remains the baseline to beat until the passive chain can prove enough margin after real losses.

## Required Candidate Set

| ID | Candidate | Status |
| --- | --- | --- |
| A1 | Broadband LPDA, about 800-2200 MHz | Candidate only |
| A2 | High-gain Yagi around 1800 MHz / LTE Band 3 | Candidate only |
| A3 | High-gain Yagi around 900 MHz | Candidate only |
| A4 | Dual-band or nested 900/1800 MHz directional antenna | Candidate only |
| A5 | Biquad or double-biquad where technically appropriate | Candidate only |
| A6 | Panel or patch-array concepts | Candidate only |
| A7 | Other passive directional designs that simulation suggests may outperform these | Candidate only |

## Required Metrics Before Blueprint Approval

Every serious candidate must be calculated or simulated where technically possible for:

- realized gain at 900 MHz
- realized gain at 1800 MHz
- performance around 2100 MHz when relevant
- usable bandwidth
- S11 or return loss
- VSWR
- feed-point impedance
- front-to-back ratio
- horizontal radiation pattern
- vertical radiation pattern
- beamwidth
- polarization
- expected efficiency
- physical dimensions
- boom length
- element count
- conductor diameter sensitivity
- construction tolerances
- sensitivity to dimensional errors
- feed complexity
- balun or matching requirements
- coax requirements
- likely coax losses
- passive-coupler implications
- expected performance through a passive phone coupler
- ease of fabrication in Cuba
- availability of materials
- repairability
- weatherproofing complexity
- estimated component cost
- import considerations for individual components

## Weighted Decision Criteria

Scores use 0 to 5:

- 0: unacceptable or unknown risk
- 1: weak
- 3: workable
- 5: strong

Weights total 100.

| Criterion | Weight |
| --- | ---: |
| Connectivity during an ETECSA blackout | 18 |
| Useful performance at 900 MHz and/or 1800 MHz | 12 |
| Stable SINR and useful directivity, not only high RSRP | 10 |
| Low RF loss and high system efficiency after coax, matching, connectors, and coupler | 10 |
| Compatibility with an ordinary ETECSA phone | 9 |
| Passive RF operation | 7 |
| Ability to fabricate or repair in Cuba | 12 |
| Ability to import individual ordinary components legally | 6 |
| Low production cost | 12 |
| Reasonable mechanical size | 3 |
| Weatherproofing practicality | 1 |

## Production Cost Rule

The best antenna is not automatically the one with the highest simulated peak gain.

For this project, the selected antenna must be cost-effective:

- low material cost
- low tool requirement
- simple enough to fabricate repeatedly
- repairable with ordinary materials
- tolerant of small construction errors
- useful after coax, connector, matching, and passive-coupler losses
- practical for Cuban import and local substitution constraints

If two designs perform similarly, choose the cheaper, simpler, more repairable design.

A topology should not win on antenna score alone if the complete system is harder or more expensive to reproduce publicly than the phone-at-RF-location architecture.

## Pre-Measurement Provisional Research Ranking

This is a planning rank only. It is not antenna selection and not blueprint approval. The ranking expresses what to study first, not what to fabricate.

| Rank | Candidate | Provisional score | Why it ranks here before measurement |
| ---: | --- | ---: | --- |
| 1 | 900 MHz high-gain Yagi | 78 | Strong blackout-resilience candidate if lower-band service survives; simple passive construction; larger size is the main penalty. |
| 2 | Broadband LPDA, 800-2200 MHz | 74 | Good hedge against uncertain bands; moderate gain and feed complexity may be less useful if passive-coupler loss is high. |
| 3 | Dual-band or nested 900/1800 MHz directional antenna | 70 | Could match the real project well, but complexity, tuning, and construction tolerance risks are higher. |
| 4 | 1800 MHz high-gain Yagi | 64 | Attractive if LTE Band 3 survives blackouts; risky if 4G is reduced or unavailable during outages. |
| 5 | Panel or patch-array concepts | 57 | Potentially weatherproof and compact at higher bands; 900 MHz practicality and fabrication details need proof. |
| 6 | Biquad or double-biquad | 52 | Simple at higher bands; less obviously suited for 900 MHz blackout resilience and passive phone coupling. |
| 7 | Other passive directional designs | TBD | Must be added only when calculations or simulation show a reason to compare them. |

## What Would Change The Ranking

- If field measurements show LTE Band 3 stays strong during blackouts, the 1800 MHz Yagi moves up.
- If 900 MHz is the only reliable outage service, the 900 MHz Yagi becomes the main antenna candidate.
- If phone-at-RF-location works well without coax, Architecture 2 may beat all passive antenna/coupler options.
- If passive coupler loss is large, high advertised antenna gain may still fail the net improvement test.
- If local materials cannot hold tight tolerances, simpler and more tolerant antennas move up.

## Approval Gate

No antenna design may move into `blueprints/approved/` until:

- calculations exist
- simulation exists
- assumptions are documented
- the design has been compared against competing topologies
- construction tolerances are documented
- the passive-coupler implications are documented
- a reason for selecting that topology is recorded in `DECISIONS.md`
