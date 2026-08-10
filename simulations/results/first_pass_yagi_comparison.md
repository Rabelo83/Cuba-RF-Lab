# First-Pass Comparison: Y900_5EL_SEED vs Y1800_5EL_SEED

Status: SIMULATED, BOTH CANDIDATES FAIL AS SEEDED

Date: 2026-08-09

This is the first-priority comparison from `simulations/nec/first_pass_queue.md`. Full detail for each candidate, including the solver validation, is in `simulations/results/y900_5el_seed_first_pass.md` and `simulations/results/y1800_5el_seed_first_pass.md`.

## Side-By-Side At Each Candidate's Target Center Frequency

| | Y900_5EL_SEED at 900 MHz | Y1800_5EL_SEED at 1800 MHz |
| --- | ---: | ---: |
| Forward gain | -0.75 dBi | -0.13 dBi |
| Front-to-back ratio | -4.98 dB | -4.25 dB |
| VSWR (50 ohm) | 13.08 | 12.77 |
| Best point in required band | -0.46 dBi at 925 MHz | +1.92 dBi at 1710 MHz |
| Net passive-chain estimate vs. Track A (good-case coax/coupler) | about -4.4 dB | about -2.8 dB |

## Comparison Verdict

Neither candidate is usable as seeded, so this is not yet a real "which one is better" comparison -- it is a "both fail, in the same way, for the same underlying reason" result. Both use the same naive, uniformly wavelength-scaled director geometry (`calculations/preliminary_antenna_geometry.py`'s `make_yagi` with identical length/position factors, just rescaled by target frequency), and both show the same signature: reflector-to-driven pairing behaves correctly, but adding the director elements degrades rather than improves forward gain across nearly the entire required band. The 1800 MHz candidate is marginally less bad at its very lowest required frequency (1710 MHz), but that is a narrow, likely coincidental crossing point, not evidence that the 1800 MHz topology is fundamentally sounder.

Neither candidate beats the Track A phone-at-RF-location baseline (`DECISIONS.md`, "Treat Phone-At-RF-Location As The Baseline To Beat"). Both trigger the stop conditions in `simulations/nec/first_pass_queue.md`: poor match not solvable with a simple low-cost feed, and gain too low to survive passive-chain losses.

## What This Does and Does Not Show

This shows the specific seed dimensions in `calculations/preliminary_antenna_geometry.py` do not form working Yagis at either band. It does not show that 900 MHz or 1800 MHz Yagis are inherently unworkable -- the solver validation (an independently chosen, textbook-ratio 3-element Yagi built with the same code) produced the expected roughly 9 dBi gain and healthy front-to-back ratio, proving the simulation approach itself is sound.

## Next Step

Before priorities 3-7 in `simulations/nec/first_pass_queue.md` (7-element Yagis, LPDA, biquads) are run, or before `Y900_5EL_SEED`/`Y1800_5EL_SEED` are retried, `calculations/preliminary_antenna_geometry.py` needs a real director design pass -- proper length taper and non-uniform, closer director spacing -- rather than the current uniform wavelength-scaled placeholder. Re-running the 7-element seeds against the same uniform-scaling method would likely reproduce the same failure, since they share the same director generation logic.
