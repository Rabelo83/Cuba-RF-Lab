# Y1800_5EL_SEED First-Pass NEC Result

Status: SIMULATED, FAILS AS SEEDED

Date: 2026-08-09

Solver: Python `necpp` 2.2.5 (NEC2 engine), free space, no ground plane.

Model file: `simulations/nec/run_first_pass_yagi.py`

Raw data: `data/processed/y1800_5el_seed_diameter_freq_sweep.csv`, `data/processed/y1800_5el_seed_tolerance_sweep.csv`

Input geometry: `Y1800_5EL_SEED` from `calculations/preliminary_antenna_geometry.py`, unmodified.

## Headline Result

Same failure mode as `Y900_5EL_SEED` (see that file for the solver validation that rules out a code bug): forward gain is negative or near zero across almost the entire required 1710-1880 MHz band, VSWR referenced to 50 ohms is above 11:1 everywhere in that band, and the front-to-back ratio is negative (the "back" direction radiates more strongly than "front") for all but the very bottom edge of the sweep. This candidate fails the same stop conditions as the 900 MHz seed.

There is one partial exception worth recording: at 1710 MHz, the very bottom edge of the required sweep, forward gain is a modest +1.92 dBi with a small positive front-to-back ratio (+0.68 dB) -- still far short of a working Yagi, but the only check point in either candidate that is not outright negative. See the trend note below.

## Realized Gain, Impedance, and VSWR at Required Check Points

Conductor diameter 4 mm (middle of the swept 3/4/6 mm range).

| Frequency | Feed impedance (ohm) | VSWR (50 ohm ref) | Forward gain | Back gain | Front-to-back |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1710 MHz | 9.0 +55.5j | 12.52 | 1.92 dBi | 1.25 dBi | 0.68 dB |
| 1800 MHz | 43.4 +153.2j | 12.77 | -0.13 dBi | 4.12 dBi | -4.25 dB |
| 1840 MHz | 76.8 +193.3j | 11.83 | -0.14 dBi | 3.73 dBi | -3.88 dB |
| 1880 MHz | 124.5 +229.4j | 11.25 | -0.25 dBi | 3.39 dBi | -3.64 dB |

## Full 1710-1880 MHz Sweep (4 mm conductor)

10 MHz steps. Full data in the CSV.

| Frequency | Forward gain | Front-to-back |
| ---: | ---: | ---: |
| 1710 MHz | 1.92 dBi | 0.68 dB |
| 1720 MHz | -3.63 dBi | -7.05 dB |
| 1740 MHz | -2.28 dBi | -6.73 dB |
| 1760 MHz | -0.75 dBi | -5.21 dB |
| 1800 MHz | -0.13 dBi | -4.25 dB |
| 1840 MHz | -0.14 dBi | -3.88 dB |
| 1880 MHz | -0.25 dBi | -3.64 dB |

There is a sharp drop between 1710 MHz (the one usable-looking point) and 1720 MHz, then a slow partial recovery toward higher frequency that never gets back above 0 dBi within the required band. This step-like shape, rather than a smooth resonance curve, is itself a sign that this geometry is not behaving as a clean single-resonance Yagi in this band -- consistent with the `Y900_5EL_SEED` finding that the director dimensions in this seed family do not form a working array.

## Conductor Diameter Sensitivity

Checked at 3, 4, and 6 mm across the full frequency sweep (`data/processed/y1800_5el_seed_diameter_freq_sweep.csv`). The qualitative result is unchanged across all three: no diameter in this range recovers useful positive forward gain across the required band.

## Dimensional Tolerance Sensitivity

Same method as the 900 MHz file: every element's length shifted together, or every element's spacing shifted together, one dimension at a time. Nominal 4 mm conductor, four required check-point frequencies.

| Perturbation | 1800 MHz forward gain | 1800 MHz VSWR |
| --- | ---: | ---: |
| Nominal | -0.13 dBi | 12.77 |
| Length +1 mm | 0.05 dBi | 12.30 |
| Length -1 mm | -0.35 dBi | 13.30 |
| Length +3 mm | 0.24 dBi | 11.55 |
| Length -3 mm | -1.35 dBi | 15.32 |
| Spacing +1 mm | -0.16 dBi | 12.45 |
| Spacing -1 mm | -0.10 dBi | 13.14 |
| Spacing +3 mm | -0.22 dBi | 11.86 |
| Spacing -3 mm | -0.03 dBi | 13.57 |

Small length increases nudge gain slightly positive but never past about +0.24 dBi -- nowhere close to a usable directional gain, and VSWR stays above 11:1 throughout. Ordinary construction tolerance cannot rescue this candidate either.

## Pattern and Beamwidth (1800 MHz, 4 mm conductor)

- Horizontal (azimuth) half-power beamwidth: about 47 degrees. As with the 900 MHz candidate, this describes the shape of a weak lobe (forward gain near 0 dBi at the 1800 MHz center frequency), not a usable pattern.
- Vertical (elevation) half-power beamwidth: could not be determined within the sweep, for the same structural reason as `Y900_5EL_SEED` (a single-boom planar array with no vertical element stacking).
- Polarization: horizontal, as modeled. Real serving-site polarization is still an open question (`OPEN_QUESTIONS.md`).
- Efficiency: modeled with lossless conductors; real hardware will realize somewhat less gain than reported here.

## Feed and Matching Notes

Feed reactance is large and positive throughout the band (roughly +55 to +230 ohms), and resistance swings from under 10 ohms to over 120 ohms across the same sweep -- a moving target that a simple fixed matching network cannot track. This is a harder matching problem than the 900 MHz candidate's already-difficult one.

## Net Passive-Chain Estimate

Using `calculations/desktop_link_budget_scenarios.md`'s method, even the good-case loss stack (LMR-240, 5 m, 6 dB coupler: about 2.62 dB of chain loss before the antenna at 1800 MHz) leaves this candidate at roughly -0.13 - 2.62 = about -2.8 dB net at the 1800 MHz check point, and worse everywhere else in the band except the one anomalous 1710 MHz point. As seeded, this candidate does not beat the Track A phone-at-RF-location baseline either.

## Recommendation

Do not advance `Y1800_5EL_SEED` in its current form, for the same reason as `Y900_5EL_SEED`: the director length/spacing pattern in this seed family (uniform wavelength-scaled steps) does not produce a working Yagi. A revised geometry using an actual director design method is needed before a fair comparison against the 900 MHz candidate, the LPDA, or Track A can be made. See `simulations/results/y900_5el_seed_first_pass.md` for the solver validation that supports trusting this negative result.
