# Engineering Requirements

## RF Requirements

- Use metric dimensions as primary.
- Account for element diameter.
- Account for boom geometry.
- Account for support material.
- Account for feed impedance.
- Account for coax loss.
- Account for connector loss.
- Account for passive coupler loss.
- Distinguish RSRP, RSRQ, SINR, and RSSI.
- Keep raw measurement data.
- Evaluate RF performance as a full system, including coax, connectors, matching, passive coupler, and phone placement.
- Prefer useful real-world connectivity over theoretical peak gain.

## Production Requirements

- Estimate production cost before recommending a public build.
- Separate required parts from optional improvements.
- Prefer locally available, repairable, and substitutable materials.
- Track required tools and construction difficulty.
- Penalize designs that need fragile precision work unless they deliver a necessary benefit.
- Include import and legal uncertainty in design comparisons.

## Validation Requirements

- Calculations before fabrication.
- Simulation before buildable blueprint status.
- NanoVNA or equivalent S11 checks for prototypes where practical.
- Field measurements before final approval.
- Separate normal-power and blackout measurements.

## Documentation Requirements

Every design document should include:

- title
- version
- status
- author or AI
- date
- objective
- assumptions
- target bands
- materials
- dimensions
- RF calculations
- simulation method and results
- feed arrangement
- mechanical notes
- construction tolerance
- weatherproofing
- limitations
- import considerations
- production cost estimate
- local substitutes
- required tools
- repair notes
- testing procedure
- revision history
