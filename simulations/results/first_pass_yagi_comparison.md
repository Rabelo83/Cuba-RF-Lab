# Yagi Comparison: From Failed Seeds To Working Candidates

Status: WORKING CANDIDATES FOUND FOR BOTH BANDS -- MATCHING NETWORK STILL NEEDED

Date: 2026-08-09 (initial failure), updated 2026-08-10 (working candidates)

This started as the priority-1/2 comparison from `simulations/nec/first_pass_queue.md` (900 MHz vs 1800 MHz five-element Yagi). It has grown into a full story: the original seed geometry failed, was independently diagnosed, and was replaced with an NEC-optimized geometry that works. Full detail for each candidate is in the individual results files listed below.

## Timeline

1. **`Y900_5EL_SEED` / `Y1800_5EL_SEED` (uniform wavelength-scaled directors): failed.** Negative-to-marginal forward gain and VSWR above 11:1 across both required bands. See `y900_5el_seed_first_pass.md`, `y1800_5el_seed_first_pass.md`.
2. **Solver validated independently** (isolated dipole matched textbook physics; a hand-built textbook-ratio Yagi hit the expected ~9 dBi) to rule out a code bug before trusting the failure.
3. **`Y900_5EL_OPT_V1` / `Y1800_5EL_OPT_V1` (NEC-optimized, single-frequency objective): narrowband spike, not usable.** 9.15 dBi / 8.56 dBi exactly at the target frequency, collapsing to negative gain a short distance away in the required band.
4. **`Y900_5EL_OPT_V2_BW` / `Y1800_5EL_OPT_V2_BW` (NEC-optimized, bandwidth-aware objective): working.** Flat 11.1-11.5 dBi gain across all four required check points in both bands. See `y900_5el_opt_v2_bw_first_pass.md`, `y1800_5el_opt_v2_bw_first_pass.md`.
5. A real bug was caught and fixed during step 4: an early version of the bandwidth-aware search silently rescaled the antenna's physical size to each test frequency instead of holding one fixed structure and only changing the frequency -- caught by cross-checking the optimizer's own numbers against an independent re-simulation, which disagreed until the bug was fixed. The numbers in this document are post-fix and the two code paths now agree.

## Side-By-Side: Working Candidates (V2_BW)

| | Y900_5EL_OPT_V2_BW | Y1800_5EL_OPT_V2_BW |
| --- | ---: | ---: |
| Forward gain, required band | 11.1-11.3 dBi (flat) | 11.1-11.5 dBi (flat) |
| Robust front-to-back (center freq) | 10.80 dB | 9.56 dB |
| VSWR range, required band | 2.4 to 87.6 | 5.8 to 32.5 |
| Weakest required check point | 960 MHz: -2.40 dBi net (unmatched) | 1880 MHz: +1.72 dBi net (unmatched) |
| Best required check point | 925 MHz: +10.28 dBi net (unmatched) | 1840 MHz: +8.48 dBi net (unmatched) |
| Tolerance robustness | Gain stable under +/-1/+/-3 mm perturbation | Gain stable except one fragile point (+3 mm spacing at 1880 MHz) |

"Net" = forward gain minus this candidate's own native mismatch loss at that frequency (see the individual results files); it does not yet include coax/connector/coupler losses.

## Comparison Verdict

Both bands now have a real working Yagi candidate -- a fundamentally different situation from the first pass, where neither band had anything usable. The 1800 MHz candidate is the stronger of the two as things stand today: every required check point stays net-positive even with no matching network at all, while the 900 MHz candidate's top-of-band point (960 MHz) goes solidly negative unmatched. Neither has a matching network designed yet; that is the clear next step for both, and would likely close most of the remaining gap, especially for the 900 MHz candidate's weak point.

Neither candidate has yet been compared against the LPDA or biquad topologies (`antenna/candidate_comparison.md`), which have not been simulated. This result establishes that the Yagi topology itself is viable at both bands -- it does not yet establish that Yagi is the best topology.

Using the desktop link-budget method (`calculations/desktop_link_budget_scenarios.md`, good-case loss stack: LMR-240, 5 m, 6 dB coupler), most of the required band for both candidates now shows a positive passive-chain delta versus the Track A phone-at-RF-location baseline -- the first time this project has had simulation-backed evidence that Track B could win, rather than an assumed placeholder. This is not yet a recommendation to build; the coupler-loss risk (3-12 dB depending on real-world coupler quality) still dominates the outcome more than antenna design does, and that number remains a source-backed estimate, not a project measurement.

## Next Step

Design a matching network (gamma match or hairpin match, most urgently for `Y900_5EL_OPT_V2_BW`'s 960 MHz weak point) and re-simulate with it in place. After that, move on to simulating the LPDA and biquad candidates (`simulations/nec/first_pass_queue.md` priorities 5-7) so the antenna comparison framework has real data for all topologies, not just Yagi.
