# NEC First-Pass Simulation Queue

Status: working candidates found for priorities 1 and 2; matching network needed next; priorities 3-7 still pending

Date: 2026-08-09, updated 2026-08-10

## Priority 1 and 2 Result

`Y900_5EL_SEED` and `Y1800_5EL_SEED` (uniform wavelength-scaled directors) failed as seeded: negative or near-zero forward gain across nearly the entire required band, VSWR above 11:1 throughout. The solver was independently validated (isolated dipole and a hand-built textbook-ratio Yagi both matched expected physics), so this was a real property of the seed's director geometry, not a simulation bug.

An NEC-driven local search (`simulations/nec/optimize_yagi_directors.py`) then found working replacements, `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW`: flat 11.1-11.5 dBi forward gain across all four required check points in both bands. Both still need a matching network before their native impedance (VSWR 2.4-87.6 depending on frequency) is usable with ordinary 50 ohm coax.

Full detail: `simulations/results/first_pass_yagi_comparison.md` (start here), `simulations/results/y900_5el_seed_first_pass.md`, `simulations/results/y1800_5el_seed_first_pass.md`, `simulations/results/y900_5el_opt_v2_bw_first_pass.md`, `simulations/results/y1800_5el_opt_v2_bw_first_pass.md`.

## Immediate Next Step

Design a matching network (gamma or hairpin match) for `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW` and re-simulate with it in place, most urgently for the 900 MHz candidate's 960 MHz weak point (currently -2.40 dBi net, unmatched).

## Remaining Queue

Do not run `Y900_7EL_SEED` / `Y1800_7EL_SEED` from the original uniform-scaling seed family -- they would likely reproduce the original failure the same way `Y900_5EL_SEED`/`Y1800_5EL_SEED` did. If a higher-gain 7-element candidate is wanted, it should extend the working `*_OPT_V2_BW` geometry (add two more optimized directors) rather than the failed uniform-scaling method.

LPDA and biquad seeds (priorities 5-7) use different geometry generators, not the failed director-scaling method, and have not been simulated yet. These are next after the matching network work above.

Local check on 2026-08-09:

- Python `necpp` 2.2.5 installed in `.venv`.
- `scripts/nec_smoke_test.py` passed with a simple 900 MHz dipole model.
- `xnec2c`, `nec2c`, and `openEMS` were not found.

This file defines the first simulation pass so model generation and results stay aligned with the engineering target.

## Input Geometry

Use:

- `calculations/preliminary_antenna_geometry.py`
- `calculations/preliminary_antenna_geometry.md`
- `data/processed/antenna_candidate_first_pass.csv`

All values are pre-simulation seeds only. They are not final dimensions.

## Simulation Order

| Priority | Candidate | Reason |
| ---: | --- | --- |
| 1 | Y900_5EL_SEED | Primary lower-band, simpler and cheaper than 7-element version. |
| 2 | Y1800_5EL_SEED | Compact LTE Band 3 candidate; useful cost/size comparison. |
| 3 | Y900_7EL_SEED | Tests whether extra 900 MHz gain margin is worth size and tolerance cost. |
| 4 | Y1800_7EL_SEED | Tests whether high-band passive-chain margin can beat phone-at-RF-location. |
| 5 | LPDA_800_2200_SEED | Band-uncertainty hedge; must prove complexity is justified. |
| 6 | BIQUAD_1800_SEED | Simple compact high-band reference. |
| 7 | BIQUAD_2100_SEED | Secondary high-band reference for broadband awareness. |

## Frequency Sweeps

| Candidate family | Sweep | Check points |
| --- | --- | --- |
| 900 MHz Yagi | 880-960 MHz, 5 MHz step | 900, 925, 945, 960 MHz |
| 1800 MHz Yagi | 1710-1880 MHz, 10 MHz step | 1710, 1800, 1840, 1880 MHz |
| LPDA | 800-2200 MHz, 25 MHz step | 800, 900, 1800, 2100, 2200 MHz |
| 1800 MHz biquad | 1710-1880 MHz, 10 MHz step | 1710, 1800, 1840, 1880 MHz |
| 2100 MHz biquad | 1920-2170 MHz, 10 MHz step | 1920, 2100, 2170 MHz |

## Material/Tolerance Sweeps

Run each practical wire/tube antenna with:

- conductor diameter: 4 mm, 6 mm, 8 mm for Yagi and LPDA where practical
- conductor diameter: 2 mm, 3 mm, 4 mm for biquad wire
- element length error: nominal, +1 mm, -1 mm, +3 mm, -3 mm
- element spacing error: nominal, +1 mm, -1 mm, +3 mm, -3 mm
- feed gap/matching assumption documented separately

## Required Outputs

For each candidate, save a summarized result in `simulations/results/` with:

- solver and version
- model file path
- target frequency sweep
- realized gain at required check points
- S11 or return loss
- VSWR
- feed-point impedance
- front-to-back ratio
- horizontal pattern
- vertical pattern
- half-power beamwidth
- polarization
- efficiency estimate
- construction tolerance sensitivity
- feed and matching notes
- net passive-chain estimate after coax, connector, matching, passive-coupler, and miscellaneous losses
- comparison against phone-at-RF-location

## Stop Conditions

Stop advancing a candidate if simulation shows:

- poor match that cannot be solved with a simple, low-cost feed
- gain too low to survive the passive-chain losses
- beamwidth too narrow for practical aiming by non-specialists
- construction tolerance too tight for ordinary tools
- material or feed complexity too high for low-cost public fabrication

Any candidate that fails should remain documented; failed candidates help prevent repeated work.
