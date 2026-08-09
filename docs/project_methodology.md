# Project Methodology

Status: active roadmap

## Guiding Objective

The project is not trying to produce the most impressive laboratory antenna. It is trying to produce the lowest-cost practical communication solution that can help Cuban families during blackouts.

Research and simulations should therefore lead toward:

- useful connectivity
- low production cost
- simple fabrication
- repairability
- legal passive operation
- ordinary consumer phones
- parts that can be sourced, substituted, or fabricated in Cuba

## Current Data Mode

The project owner cannot currently collect local RF measurements or local material availability observations from Cuba. The active engineering mode is therefore desktop research and simulation first.

That means:

- use dated public sources
- use manufacturer specifications where possible
- model conservative low, medium, and high loss scenarios
- run sensitivity analysis instead of claiming certainty
- keep all designs marked as not field validated
- treat local field data as an external validation gate

## Phase 0: Repository and Research Baseline

- Create repository structure.
- Record known facts, assumptions, questions, and safety limits.
- Gather dated ETECSA band and blackout behavior sources.

## Phase 1: Verify ETECSA RF Environment

- Gather current dated sources for ETECSA/Cubacel bands and blackout behavior.
- Build conservative RF scenarios for indoor, outdoor, window, roof, and street-corner placements.
- Record which questions still require external local measurements.
- Do not claim field performance until collaborator measurements exist.

## Phase 2: Model Antennas

- Compare LPDA, 900 MHz Yagi, 1800 MHz Yagi, biquad, panel, reflector, and dual-polarized options.
- Account for material diameter, spacing, feed impedance, supports, and coax loss.

## Phase 3: Design Passive Phone Coupler

- Build an adjustable test fixture.
- Sweep phone position, gap, rotation, and coupler geometry.
- Record repeatability and sensitivity.

## Phase 4: Build Prototypes

- Build only designs that have calculations and simulation notes.
- Document tolerances, materials, and assembly steps.

## Phase 5: NanoVNA Validation

- Calibrate NanoVNA.
- Measure S11, return loss, SWR, resonance, and bandwidth.
- Do not claim antenna gain from NanoVNA data alone.

## Phase 6: Blackout Field Testing

- Hold this as a validation phase for future local collaborators.
- Test real communication performance during outages only when safe local data becomes available.
- Record app-level success, not just signal strength.

## Phase 7: Optimize

- Compare measured results to simulation when measurements exist.
- Before measurements exist, optimize only across conservative scenarios and clearly documented assumptions.
- Revise antenna, coupler, feedline, and placement.

## Phase 8: Create Final Blueprints

- Move only reviewed, calculated, simulated, and tested designs toward approval.
- Clearly label anything that is not field validated.
- Include production-cost notes and substitution options.

## Phase 9: Public Production Package

- Create plain-language bilingual build instructions.
- Create final bill of materials with cost ranges.
- Identify local substitutes.
- Separate required parts from optional performance improvements.
- Document repair steps and replacement parts.
- Keep the solution as simple and inexpensive as possible while still working.
