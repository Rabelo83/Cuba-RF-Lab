# Y900_5EL_SEED First-Pass NEC Result

Status: SIMULATED, FAILS AS SEEDED

Date: 2026-08-09

Solver: Python `necpp` 2.2.5 (NEC2 engine), free space, no ground plane.

Model file: `simulations/nec/run_first_pass_yagi.py`

Raw data: `data/processed/y900_5el_seed_diameter_freq_sweep.csv`, `data/processed/y900_5el_seed_tolerance_sweep.csv`

Input geometry: `Y900_5EL_SEED` from `calculations/preliminary_antenna_geometry.py`, unmodified.

## Headline Result

As literally seeded, this candidate does not function as a working Yagi across its required 880-960 MHz band. Forward gain is at or below 0 dBi (worse than a plain isotropic radiator) across nearly the entire required band, feed VSWR referenced to 50 ohms exceeds 10:1 everywhere in the band, and the front-to-back ratio is small or the "front" direction is actually the weaker one. This fails the project's own stop conditions in `simulations/nec/first_pass_queue.md` ("poor match that cannot be solved with a simple, low-cost feed" and "gain too low to survive the passive-chain losses").

This is a finding about the pre-simulation geometry seed, not a claim that a 900 MHz Yagi cannot work. See Solver Validation below.

## Realized Gain, Impedance, and VSWR at Required Check Points

Conductor diameter 6 mm (middle of the swept 4/6/8 mm range).

| Frequency | Feed impedance (ohm) | VSWR (50 ohm ref) | Forward gain | Back gain | Front-to-back |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 900 MHz | 31.8 +131.9j | 13.08 | -0.75 dBi | 4.23 dBi | -4.98 dB |
| 925 MHz | 65.7 +178.3j | 11.67 | -0.46 dBi | 3.74 dBi | -4.20 dB |
| 945 MHz | 103.3 +210.8j | 11.06 | -0.54 dBi | 3.37 dBi | -3.91 dB |
| 960 MHz | 137.6 +230.6j | 10.75 | -0.63 dBi | 3.11 dBi | -3.74 dB |

Negative front-to-back values mean the "back" direction (toward the reflector) actually radiates more strongly than the "front" direction (toward the directors) at every required check point.

## Full 880-960 MHz Sweep (6 mm conductor)

5 MHz steps. Full data in the CSV.

| Frequency | Forward gain | Front-to-back |
| ---: | ---: | ---: |
| 880 MHz | -4.40 dBi | -8.59 dB |
| 890 MHz | -1.55 dBi | -5.91 dB |
| 900 MHz | -0.75 dBi | -4.98 dB |
| 920 MHz | -0.46 dBi | -4.30 dB |
| 940 MHz | -0.52 dBi | -3.97 dB |
| 960 MHz | -0.63 dBi | -3.74 dB |

Gain rises slightly as frequency increases toward the low end of the swept range then flattens out negative; it does not cross into positive, useful directive gain anywhere in the required band. A quick check below 880 MHz would likely show the same trend continuing, but that is outside the required band and was not pursued further in this pass.

## Conductor Diameter Sensitivity

Checked at 4, 6, and 8 mm across the full frequency sweep (`data/processed/y900_5el_seed_diameter_freq_sweep.csv`). Thicker conductor shifts the impedance curve and shape of the gain-vs-frequency trend somewhat, but does not change the qualitative result: forward gain stays at or below roughly 0 dBi across the required band for all three diameters.

## Dimensional Tolerance Sensitivity

Applied uniformly: every element's length shifted by the same offset, or every element's spacing along the boom shifted by the same offset (not both at once, and not per-element random error). Nominal 6 mm conductor, four required check-point frequencies.

| Perturbation | 900 MHz forward gain | 900 MHz VSWR |
| --- | ---: | ---: |
| Nominal | -0.75 dBi | 13.08 |
| Length +1 mm | -0.56 dBi | 12.86 |
| Length -1 mm | -1.10 dBi | 13.36 |
| Length +3 mm | -0.41 dBi | 12.56 |
| Length -3 mm | -3.07 dBi | 14.09 |
| Spacing +1 mm | -0.76 dBi | 12.84 |
| Spacing -1 mm | -0.74 dBi | 13.32 |
| Spacing +3 mm | -0.78 dBi | 12.37 |
| Spacing -3 mm | -0.73 dBi | 13.83 |

None of these +/-1 mm or +/-3 mm perturbations recover useful positive gain or a workable VSWR. The candidate is not simply "close but sensitive to tolerance" — it is off by a wide margin that ordinary construction tolerance cannot fix.

## Pattern and Beamwidth (900 MHz, 6 mm conductor)

- Horizontal (azimuth) half-power beamwidth: about 49 degrees, centered on the forward direction as modeled. Because forward gain itself is negative here, this beamwidth number describes the shape of a weak, not-yet-useful lobe, not a usable antenna pattern.
- Vertical (elevation) half-power beamwidth: could not be determined; gain never dropped 3 dB from its peak across the +/-90 degree elevation sweep. This is expected for a single-boom planar array with no vertical stacking, and is not itself a defect.
- Polarization: horizontal, as modeled (elements and boom both horizontal). A real installation could equally mount this design rotated 90 degrees for vertical polarization; `OPEN_QUESTIONS.md` still needs the actual serving-site polarization before this choice can be made.
- Efficiency: modeled with perfect (lossless) conductors. Real copper/aluminum ohmic loss, joints, and any matching network would reduce realized gain further below what is reported here.

## Feed and Matching Notes

Feed resistance and reactance both move a long way from 50 ohms across the whole band (reactance alone is +90 to +230 ohms). This is not a "add a small matching stub" situation; it needs a deliberate matching network, and even then the underlying radiation pattern (negative-to-marginal forward gain) is the bigger problem, not just the match.

## Net Passive-Chain Estimate

Using the method in `calculations/desktop_link_budget_scenarios.md`, even the good-case loss stack (LMR-240, 5 m, 6 dB coupler: about 3.62 dB of chain loss before the antenna) cannot be closed by a -0.75 dBi antenna. The passive chain delta at 900 MHz for this seed, as built, is roughly -0.75 - 3.62 = about -4.4 dB in the good case and far worse in the typical case -- solidly negative, and worse than simply standing the phone at the same RF location (see `DECISIONS.md`, "Treat Phone-At-RF-Location As The Baseline To Beat"). This candidate, as seeded, does not beat the Track A baseline.

## Solver Validation

Before trusting a negative-gain result, the solver and modeling approach were checked three ways:

1. A single isolated `driven` element alone (no reflector or directors) reproduced known dipole physics: about 2.21 dBi gain and front-to-back ratio of 0 dB (symmetric, as expected for a bare dipole), matching the textbook value of about 2.15 dBi for a thin half-wave dipole and matching `scripts/nec_smoke_test.py`'s own 900 MHz dipole result (2.20 dBi).
2. Adding just the seed's `reflector` to the `driven` element (still the project's own seed dimensions) produced a healthy, expected result: 5.7 dBi forward gain and +9.8 dB front-to-back ratio. The reflector half of the seed geometry behaves correctly.
3. An independently chosen, textbook-ratio 3-element Yagi (reflector about 5% longer than driven, director about 5% shorter, tighter director spacing than this seed uses) built with the exact same code produced 9.11 dBi forward gain and +7.2 dB front-to-back ratio at 900 MHz -- the shape of result expected from a working Yagi.

This isolates the problem to this seed's specific director length/spacing combination (uniform 0.20-wavelength position steps and very shallow 0.01-wavelength length tapering between directors), not to the simulation code. `calculations/preliminary_antenna_geometry.py` already documents these as "simple wavelength-scaled starting ratios, not an optimized design" -- this first NEC pass confirms that caveat was necessary and that real director design (proper length taper and closer, non-uniform spacing) is required before this topology can be fairly evaluated.

## Recommendation

Do not advance `Y900_5EL_SEED` in its current form. Before any further comparison against `Y1800_5EL_SEED`, the LPDA, or Track A, generate a revised 900 MHz Yagi geometry using an actual director design method (rather than uniform wavelength scaling) and re-run this same script against it. Keep this result on file per the project's stop-condition documentation rule -- it prevents re-deriving the same failure later.
