# Simulation Results

Status: first results in

Store reviewed simulation outputs here. Raw generated outputs may be ignored if they are large, but summarized results must be documented.

Every reviewed result should state whether it improves the public solution: useful blackout connectivity, low RF loss, low production cost, local material compatibility, repairability, and comparison against other candidate topologies.

## Results On File

- `y900_5el_seed_first_pass.md` -- FAILS AS SEEDED. Negative-to-marginal forward gain and VSWR above 11:1 across the required 880-960 MHz band.
- `y1800_5el_seed_first_pass.md` -- FAILS AS SEEDED. Same failure mode across the required 1710-1880 MHz band.
- `first_pass_yagi_comparison.md` -- side-by-side comparison and root-cause note (uniform wavelength-scaled director geometry does not form a working array; solver independently validated as correct).
