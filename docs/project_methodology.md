# Project Methodology

Status: active roadmap

## Phase 0: Repository and Research Baseline

- Create repository structure.
- Record known facts, assumptions, questions, and safety limits.
- Gather dated ETECSA band and blackout behavior sources.

## Phase 1: Verify ETECSA RF Environment

- Measure indoor, outdoor, window, roof, and street-corner signal.
- Record network type, band, RSRP, RSRQ, SINR, ping, upload, download, and app success.
- Repeat during normal power and blackout.

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

- Test real communication performance during outages.
- Record app-level success, not just signal strength.

## Phase 7: Optimize

- Compare measured results to simulation.
- Revise antenna, coupler, feedline, and placement.

## Phase 8: Create Final Blueprints

- Move only reviewed, calculated, simulated, and tested designs toward approval.
- Clearly label anything that is not field validated.

