# Y900_5EL_OPT_V2_BW First-Pass NEC Result

Status: SIMULATED, WORKING CANDIDATE -- NEEDS A MATCHING NETWORK

Date: 2026-08-10

Solver: Python `necpp` 2.2.5 (NEC2 engine), free space, no ground plane.

Model file: `simulations/nec/optimize_yagi_directors.py` (search), `simulations/nec/run_optimized_yagi_first_pass.py` (characterization)

Raw data: `data/processed/y900_5el_opt_v2_bw_diameter_freq_sweep.csv`, `data/processed/y900_5el_opt_v2_bw_tolerance_sweep.csv`

Input geometry: `Y900_5EL_OPT_V2_BW` from `calculations/preliminary_antenna_geometry.py`.

## How This Geometry Was Found

`Y900_5EL_SEED` (uniform wavelength-scaled director geometry) failed NEC simulation across its entire required band (see `y900_5el_seed_first_pass.md`). Rather than substitute a second hand-guessed geometry, `simulations/nec/optimize_yagi_directors.py` used the validated NEC solver itself as an objective function for a SciPy Nelder-Mead local search: it varies the driven element and three director lengths/spacings (reflector fixed at the seed's own values) and asks NEC directly what each candidate geometry's gain is.

A first version optimized for gain at a single frequency (900 MHz only) and found an excellent peak (9.15 dBi) that collapsed to negative gain 25-60 MHz away -- a narrow, high-Q spike, not a usable design (see "Superseded Narrowband Version" below). This version instead optimizes for the worst-case (minimum) forward gain across all four required check points (900, 925, 945, 960 MHz) simultaneously, which produces a geometry that holds up across the whole required band rather than peaking at one point in it.

An earlier draft of this bandwidth-aware search had a real bug: it re-derived new physical (mm) dimensions at each checkpoint frequency's own wavelength instead of holding one fixed structure and only changing the test frequency. That produced a suspiciously perfect flat-gain result because it was silently evaluating four different rescaled antennas, not one real antenna's frequency response. The bug was caught by cross-checking the optimizer's own numbers against an independent re-simulation of the "same" geometry, which disagreed. The fix (hold mm dimensions fixed from a single reference wavelength, vary only the NEC test frequency) is in `objective_bandwidth()`, and the two code paths now agree exactly. The numbers below are post-fix.

## Headline Result

Forward gain is strong and essentially flat across the required band: 11.1 to 11.3 dBi at all four check points. This exceeds the project's placeholder assumption of 9 dBi for a 900 MHz Yagi (`calculations/desktop_link_budget_scenarios.md`). The radiating structure works. The problem is the native feed impedance, which swings widely across the band and is very poorly matched to 50 ohms at the top edge.

## Realized Gain, Impedance, and VSWR at Required Check Points

Conductor diameter 6 mm.

| Frequency | Feed impedance (ohm) | VSWR (50 ohm ref) | Forward gain | Mismatch loss | Net gain into 50 ohm coax |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 900 MHz | 45.5 +86.9j | 5.13 | 11.11 dBi | 2.63 dB | 8.48 dBi |
| 925 MHz | 95.1 +44.2j | 2.43 | 11.11 dBi | 0.83 dB | 10.28 dBi |
| 945 MHz | 13.3 +56.7j | 8.74 | 11.32 dBi | 4.33 dB | 6.99 dBi |
| 960 MHz | 2.8 +97.6j | 87.55 | 11.11 dBi | 13.50 dB | -2.40 dBi |

Mismatch loss = -10*log10(1 - |Gamma|^2), i.e. the fraction of forward power reflected by an unmatched 50 ohm feed. This is on top of, not instead of, the coax/connector/coupler losses in the link-budget scenarios.

Three of the four required check points give strong net gain even completely unmatched. The 960 MHz point is a real weak spot -- native impedance collapses to under 3 ohms resistive there, which is a hard mismatch regardless of antenna gain.

## Front-to-Back Ratio

A single-point sample at exactly phi=270 degrees is fragile -- optimized Yagi patterns can have a very narrow, deep null that a fabrication-tolerance fraction of a degree would move (this is exactly what produced a nonsensical "1009 dB" single-point reading during optimization; see the code comments in `optimize_yagi_directors.py`). Reported here instead: forward peak minus the highest gain anywhere in the 180-360 degree rear half (a robust, tolerance-insensitive figure).

At 900 MHz, nominal geometry: forward peak 11.11 dBi, rear-hemisphere peak 0.30 dBi, robust front-to-back = 10.80 dB. Solid, unremarkable-in-a-good-way directional performance -- not the exceptional 20+ dB figure the narrowband version showed, but not a weak point either.

## Conductor Diameter Sensitivity

Checked at 4, 6, and 8 mm (`data/processed/y900_5el_opt_v2_bw_diameter_freq_sweep.csv`). Gain stays strong across all three; the native-match problem at the top of the band persists at all three diameters, so diameter choice will not fix it on its own.

## Dimensional Tolerance Sensitivity

Same method as the seed results: every element's length shifted together, or every element's spacing shifted together, one dimension at a time, +/-1 mm and +/-3 mm. Full data in `data/processed/y900_5el_opt_v2_bw_tolerance_sweep.csv`.

Gain is notably robust: it stays in the 10.9-11.5 dBi range across every length and spacing perturbation tested, at 900/925/945 MHz. This is a meaningful practical result -- ordinary construction tolerance (a few mm) will not ruin this design's gain, unlike a high-Q design that would be tolerance-fragile. The 960 MHz point stays volatile under perturbation (VSWR ranges from about 39 to 145 depending on the exact offset), confirming the top-of-band mismatch is a structural property of this geometry, not something tolerance happens to be making worse.

## Pattern and Beamwidth (900 MHz, 6 mm conductor)

- Horizontal (azimuth) half-power beamwidth: about 49 degrees.
- Vertical (elevation) half-power beamwidth: about 60 degrees.
- Polarization: horizontal, as modeled (installer's mounting choice; real serving-site polarization is still an open question).
- Efficiency: lossless conductors modeled; real hardware realizes somewhat less.

## Net Passive-Chain Estimate

Using `calculations/desktop_link_budget_scenarios.md`'s method with the good-case loss stack (LMR-240, 5 m, 6 dB coupler, about 3.62 dB before the antenna) and this candidate's own net gain (already including its own mismatch loss):

- At 900/925/945 MHz: net gain 6.99-10.28 dBi minus 3.62 dB chain loss = roughly 3.4 to 6.7 dB advantage over Track A's 12 dB mid-case improvement claim is not quite the right comparison -- see `first_pass_yagi_comparison.md` for the full side-by-side against the Track A baseline.
- At 960 MHz: the chain is solidly negative (-2.40 - 3.62 = about -6.0 dB) until this candidate gets a matching network.

## What's Still Needed Before This Is Buildable

1. **A matching network.** This is the clear next step, not yet designed. A gamma match or hairpin match tuned near the center of the required band would recover most of the mismatch loss at 900-945 MHz; the 960 MHz point may need a broader-bandwidth matching approach or accepting reduced performance at that edge.
2. **Comparison against the LPDA, biquad, and Track A** per `antenna/candidate_comparison.md` -- not done yet, this file only establishes that this Yagi topology now works.
3. Field validation, once local measurement is possible again (`HANDOFF.md`).

## Superseded Narrowband Version (Y900_5EL_OPT_V1)

For the record: the single-frequency-optimized version reached 9.15 dBi and a genuinely excellent 21.7 dB robust front-to-back ratio exactly at 900 MHz, but collapsed to negative gain by 925 MHz and stayed negative through 960 MHz -- it does not satisfy the required band and is not recommended. See `y900_5el_seed_first_pass.md`'s sibling data in `data/processed/y900_5el_opt_v1_diameter_freq_sweep.csv` for the full sweep. Kept on file per the project's rule that failed/superseded iterations stay documented.
