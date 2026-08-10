# Y1800_5EL_OPT_V2_BW First-Pass NEC Result

Status: SIMULATED, WORKING CANDIDATE -- NEEDS A MATCHING NETWORK

Date: 2026-08-10

Solver: Python `necpp` 2.2.5 (NEC2 engine), free space, no ground plane.

Model file: `simulations/nec/optimize_yagi_directors.py` (search), `simulations/nec/run_optimized_yagi_first_pass.py` (characterization)

Raw data: `data/processed/y1800_5el_opt_v2_bw_diameter_freq_sweep.csv`, `data/processed/y1800_5el_opt_v2_bw_tolerance_sweep.csv`

Input geometry: `Y1800_5EL_OPT_V2_BW` from `calculations/preliminary_antenna_geometry.py`.

## How This Geometry Was Found

Same method as `Y900_5EL_OPT_V2_BW` (see that file for the full methodology, including the rescaling bug that was caught and fixed before trusting these numbers): a SciPy Nelder-Mead search using the validated NEC solver as the objective function, optimizing worst-case forward gain across the four required check points (1710, 1800, 1840, 1880 MHz) for one fixed physical geometry. Reflector length/position fixed at the original seed's values; driven element and three directors searched.

## Headline Result

Forward gain is strong and flat across the required band: 11.1 to 11.5 dBi at all four check points -- close to the project's placeholder assumption of 12 dBi for an 1800 MHz Yagi (`calculations/desktop_link_budget_scenarios.md`). As with the 900 MHz candidate, the radiating structure works; native impedance match is the remaining problem, though notably better-behaved here than the 900 MHz version.

## Realized Gain, Impedance, and VSWR at Required Check Points

Conductor diameter 4 mm.

| Frequency | Feed impedance (ohm) | VSWR (50 ohm ref) | Forward gain | Mismatch loss | Net gain into 50 ohm coax |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1710 MHz | 9.2 +36.0j | 8.30 | 11.08 dBi | 4.16 dB | 6.92 dBi |
| 1800 MHz | 28.4 +75.8j | 6.21 | 11.08 dBi | 3.21 dB | 7.87 dBi |
| 1840 MHz | 29.2 +73.5j | 5.82 | 11.49 dBi | 3.01 dB | 8.48 dBi |
| 1880 MHz | 8.1 +103.3j | 32.46 | 11.08 dBi | 9.36 dB | 1.72 dBi |

Every required check point stays net-positive even completely unmatched, including the weakest point (1880 MHz, +1.72 dBi). This is a materially better outcome than the 900 MHz candidate, whose weakest point goes negative.

## Front-to-Back Ratio

Same robust method as the 900 MHz file (forward peak minus the highest gain anywhere in the rear 180-360 degree half, not a single fragile point sample). At 1800 MHz, nominal geometry: forward peak 11.08 dBi, rear-hemisphere peak 1.52 dBi, robust front-to-back = 9.56 dB. Solid, workable directionality.

## Conductor Diameter Sensitivity

Checked at 3, 4, and 6 mm (`data/processed/y1800_5el_opt_v2_bw_diameter_freq_sweep.csv`). Gain stays strong across all three. The 1880 MHz mismatch persists at all three diameters.

## Dimensional Tolerance Sensitivity

Same method as the other results files: every element's length shifted together, or every element's spacing shifted together, +/-1 mm and +/-3 mm. Full data in `data/processed/y1800_5el_opt_v2_bw_tolerance_sweep.csv`.

Gain mostly stays strong (10-11.8 dBi) under length/spacing perturbation, with one notable fragile point: at +3 mm spacing offset, 1880 MHz gain drops to -2.7 dBi (VSWR also becomes extreme there). Given 1800 MHz element lengths and gaps are under 90 mm, a +3 mm spacing error is a proportionally large (roughly 3-5%) construction error -- worth flagging for the eventual build documentation as a tolerance to hold reasonably tightly, but not disqualifying: the nominal design and smaller (+/-1 mm) errors hold up fine.

## Pattern and Beamwidth (1800 MHz, 4 mm conductor)

- Horizontal (azimuth) half-power beamwidth: about 46 degrees.
- Vertical (elevation) half-power beamwidth: about 55 degrees.
- Polarization: horizontal, as modeled.
- Efficiency: lossless conductors modeled; real hardware realizes somewhat less.

## Net Passive-Chain Estimate

Using `calculations/desktop_link_budget_scenarios.md`'s method with the good-case loss stack (LMR-240, 5 m, 6 dB coupler, about 2.62 dB before the antenna at 1800 MHz) and this candidate's own net gain (already including its own mismatch loss): net gain 6.92-8.48 dBi across three of four check points minus 2.62 dB chain loss leaves a meaningfully positive passive-chain delta -- see `first_pass_yagi_comparison.md` for the full comparison against the Track A phone-at-RF-location baseline.

## What's Still Needed Before This Is Buildable

1. **A matching network**, same as the 900 MHz candidate, though the case for one is less urgent here since even the unmatched worst case stays net-positive. A gamma or hairpin match would still meaningfully improve the 1710/1880 MHz edges.
2. **Comparison against the LPDA, biquad, and Track A** per `antenna/candidate_comparison.md` -- not done yet.
3. Field validation, once local measurement is possible again (`HANDOFF.md`).

## Superseded Narrowband Version (Y1800_5EL_OPT_V1)

The single-frequency-optimized version reached 8.56 dBi and a 21.7 dB robust front-to-back ratio exactly at 1800 MHz, but fell to negative gain by 1880 MHz. Not recommended; kept on file in `y1800_5el_seed_first_pass.md`'s sibling data (`data/processed/y1800_5el_opt_v1_diameter_freq_sweep.csv`) per the project's rule that superseded iterations stay documented.
