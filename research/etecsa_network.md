# ETECSA/Cubacel Network Research

Status: public-source desktop baseline, local verification required

Access date for the current source pass: 2026-08-09.

## Current Working Assumptions

The project currently prioritizes these bands for engineering scenarios:

1. 900 MHz
2. 1800 MHz
3. 2100 MHz where relevant to broadband designs
4. 700 MHz as a secondary lower-band possibility, not a first blueprint target yet

Engineering interpretation:

- 900 MHz is the strongest public-source baseline for lower-band Cuban mobile service.
- 1800 MHz is the strongest public-source baseline for LTE Band 3 service.
- 2100 MHz and 700 MHz appear in third-party current band lists and should be included in broadband awareness, but they are not yet the primary low-cost antenna targets.

Band selection affects cost. A narrow, cheap antenna is useful only if that band remains available during blackouts at the target location.

## Public Source Baseline

| Band / Service | Evidence found | Source class | Confidence | Engineering use |
| --- | --- | --- | --- | --- |
| 3G Band 8, 900 MHz | Cuba.Travel lists phone compatibility for 3G Band 8 at 900 MHz. Granma's 2018 ETECSA forum describes 2G and 3G using 900 MHz. Powertec lists 3G B8 active. | B, E | High for national compatibility baseline; medium for any specific blackout location | Keep 900 MHz as a primary design and simulation target. |
| LTE Band 3, 1800 MHz | Cuba.Travel lists phone compatibility for 4G Band 3 at 1800 MHz. Granma's 2018 ETECSA forum described future 4G on 1800 MHz Band 3. Powertec lists B3 LTE active from 2019. | B, E | High for compatibility baseline; medium for outage availability | Keep 1800 MHz as a primary design and simulation target. |
| LTE or UMTS Band 1, 2100 MHz | Granma's 2018 ETECSA forum described 2100 MHz as being implemented for critical indoor places. Powertec lists B1 LTE active from 2023. | B, E | Medium | Include when evaluating broadband LPDA/panel concepts; do not optimize a first low-cost antenna around it alone. |
| LTE Band 28, 700 MHz | Granma's 2018 ETECSA forum mentioned 700 MHz as a future 4G expansion path after analog TV spectrum availability. Powertec lists B28 LTE active from 2023. | B, E | Medium | Track as a possible outage-resilient band; do not build first antenna assumptions around it until locally verified. |

## Desktop Engineering Implications

- 900 MHz and 1800 MHz remain the core comparison bands.
- A broadband 800-2200 MHz LPDA can hedge band uncertainty, but it must compete against simpler single-band and dual-band designs after system losses.
- 2100 MHz coverage is useful for broadband evaluation, but a 2100-only design does not fit the current low-cost blackout priority.
- 700 MHz could be important in some areas, but a practical 700 MHz directional antenna is larger and needs stronger evidence before it becomes a first public build target.
- All frequency conclusions remain pre-field-validation until local or collaborator measurements exist.

## Required Source Record

Every network claim must record:

- source URL
- source date
- access date
- source class
- confidence level
- affected region if known

Source classes:

- A: official ETECSA
- B: Cuban government or official publication
- C: equipment manufacturer
- D: peer-reviewed or engineering reference
- E: reputable technical third party
- F: forum, marketplace, anecdotal, or field observation

## Measurement Fields

When using a phone or field-test app, record:

- network type
- band
- channel or EARFCN if available
- RSRP
- RSRQ
- SINR
- RSSI if available
- serving cell identity if available
- test location
- blackout state
- whether basic communication worked
- minimum equipment used

## Current Gaps

- No current direct ETECSA technical band page has been found and added yet.
- No Matanzas field measurements have been added yet.
- No blackout-specific local band data has been added yet.
- No cell-site survival data exists for long outages.
- No local phone model has been locked as the reference endpoint.

## Next Research Actions

1. Search for current official ETECSA technical pages or regulatory frequency-plan documents.
2. Build simulations at 900 MHz and 1800 MHz first, with 2100 MHz included for broadband candidates.
3. Keep 700 MHz in the source ledger but defer low-cost blueprint work until stronger evidence exists.
4. Later, when data collection becomes possible, measure actual phone bands, RSRP, RSRQ, SINR, and app success during both normal power and blackout conditions.
