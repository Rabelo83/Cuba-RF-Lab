# Decisions

## 2026-08-09: Use Two Parallel Tracks

Decision: pursue both a routerless phone-at-best-RF-location architecture and an improved passive antenna/coupler architecture.

Reason: the routerless path may be simpler and more robust, while the passive coupler path may match local Cuban materials and avoid dedicated LTE router service.

## 2026-08-09: Do Not Make Dedicated ETECSA Router Service Primary

Decision: do not make an expensive dedicated ETECSA modem/router/uSIM service the primary solution.

Reason: project economics favor ordinary phones and modular consumer networking.

## 2026-08-09: Prefer Ordinary Phones

Decision: use an ETECSA-compatible Android phone or similar consumer cellular device as the preferred cellular endpoint.

Reason: ordinary phones are easier to obtain, replace, test, and power than specialized cellular routers.

## 2026-08-09: Prefer Passive RF Systems

Decision: prioritize passive antennas, passive couplers, and legal consumer data transport.

Reason: this avoids unauthorized active cellular repeaters and keeps the project aligned with legal and safety boundaries.

## 2026-08-09: Prioritize 900 MHz and 1800 MHz

Decision: use 900 MHz and 1800 MHz as the initial engineering priorities.

Reason: public information suggests these are important ETECSA/Cubacel bands, but they still require current local verification.

## 2026-08-09: Require Real Blackout Measurements

Decision: no final design can rely only on normal-power signal readings.

Reason: ETECSA site behavior may change during blackouts.

## 2026-08-09: Minimize Long Cellular-Frequency Coax

Decision: avoid transporting weak cellular RF over long coax where practical.

Reason: coax loss at 900 to 2100 MHz can erase antenna benefit, especially with thin or unknown cable.

## 2026-08-09: Repository Is Source of Truth

Decision: all important project knowledge must live in repository files.

Reason: future AI and human collaborators need continuity without relying on chat history.

## 2026-08-09: Antenna Topology Must Be Selected By Comparison

Decision: do not assume the preliminary LPDA concept is final or preferred. Before any fabrication-ready antenna blueprint, compare multiple passive antenna topologies using `antenna/candidate_comparison.md`.

Reason: the real objective is the best practical passive antenna system for ETECSA blackout conditions, not validation of an earlier idea. The winning topology must beat competing designs and must be compared against the simpler phone-at-RF-location architecture after coax, connector, matching, and passive-coupler losses.

## 2026-08-09: Optimize For Public Benefit And Low Production Cost

Decision: research, simulations, materials, and blueprints must lead toward a solution that can be offered publicly at the lowest practical production cost while still working reliably and safely.

Reason: the purpose of the project is to help Cuban people struggling with blackouts and communication loss. A design that performs well in theory but is expensive, fragile, hard to import, or hard to repair does not satisfy the project mission.

## 2026-08-09: Treat Phone-At-RF-Location As The Baseline To Beat

Decision: until measured or simulated passive-system losses prove otherwise, the phone-at-best-RF-location architecture is the baseline comparison for all passive antenna/coupler proposals.

Reason: first desktop link-budget scenarios show that coax, connector, matching, passive-coupler, and implementation losses can erase the gain of a directional antenna. A passive antenna may still win if it improves SINR, uses low-loss short coax, and couples efficiently into an ordinary phone, but advertised antenna gain alone is not sufficient evidence.

## 2026-08-09: Do Not Trust Uniform Wavelength-Scaled Director Geometry

Decision: `calculations/preliminary_antenna_geometry.py`'s `make_yagi` director length/spacing scaling (uniform position steps, shallow uniform length taper) must not be reused for further Yagi candidates until it is replaced with an actual director design method.

Reason: the first NEC simulation pass showed both `Y900_5EL_SEED` and `Y1800_5EL_SEED` fail across their entire required bands (negative-to-marginal forward gain, VSWR above 11:1) using this director geometry, while the reflector-driven half of the same seeds behaves correctly and an independently chosen textbook-ratio Yagi built with the same solver produces expected results. See `simulations/results/first_pass_yagi_comparison.md`. Running `Y900_7EL_SEED`, `Y1800_7EL_SEED`, or other candidates that reuse the same director scaling logic would likely waste simulation effort reproducing the same failure.

## 2026-08-10: Use NEC-Optimized Director Geometry, Not Hand-Derived Dimensions

Decision: when a formula-based or memory-recalled antenna geometry fails simulation, the replacement should come from a local numerical search using the validated NEC solver as the objective function, not from a second hand-picked or recalled set of dimensions.

Reason: this project's own rule against inventing performance figures applies equally to inventing geometry -- a "known good" set of published Yagi dimensions recalled from memory risks being subtly wrong and is not independently checkable the way a solver-verified search is. `simulations/nec/optimize_yagi_directors.py` used SciPy's Nelder-Mead optimizer with `necpp` itself as the objective function and found working geometry for both `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW`. This also caught a real bug during development (an early version silently rescaled the antenna's physical size per test frequency instead of holding one fixed structure) that a hand-derived design would not have surfaced the same way, since the bug was found by the optimizer's own output disagreeing with an independent re-simulation.

## 2026-08-10: A Single-Frequency Gain Peak Is Not a Working Antenna

Decision: any future antenna optimization or design work for this project must evaluate gain (and other acceptance criteria) across the full required check-point frequencies from `simulations/nec/first_pass_queue.md`, not at a single target frequency alone.

Reason: `Y900_5EL_OPT_V1` and `Y1800_5EL_OPT_V1` (single-frequency-optimized) reached excellent gain and front-to-back ratio exactly at their target frequency, then collapsed to negative gain within 25-80 MHz -- a narrow, high-Q spike that fails the project's own required-band criteria despite looking excellent at one point. The bandwidth-aware replacement (`*_OPT_V2_BW`, optimizing worst-case gain across all required check points) produced a geometry that actually holds up across the band.
