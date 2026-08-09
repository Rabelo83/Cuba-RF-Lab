# Passive Coupling Research

Status: research plan with public-source loss assumptions

Access date for the current source pass: 2026-08-09.

## Goal

Design a repeatable passive coupler test fixture that can improve signal transfer to an ordinary phone without using an active cellular repeater.

The coupler should remain in the project only if measured improvement is repeatable, low-cost, repairable, and better than simply placing the phone at the stronger RF location.

## Current Loss Assumption

Public vendor guidance for passive phone cradles and patch leads commonly describes several dB of loss, with performance depending strongly on phone model, antenna location, and placement accuracy. OnWireless guidance gives these order-of-magnitude values:

| Passive coupling type | Public guidance | Project assumption use |
| --- | ---: | --- |
| Model-specific passive cradle | about 3 dB loss | Optimistic only; requires a known phone model and repeatable fixture. |
| Universal passive cradle | about 4-6 dB loss | Good-case design target if a strong mechanical fixture is built. |
| Universal passive patch lead | about 4-6 dB loss | Good-case assumption only when the phone antenna location is known. |
| Unknown homemade coupler | unknown | Model as 6-12 dB until measured. |

For current desktop link budgets, use 6 dB as a good-case passive coupling assumption and 12 dB as a conservative typical-risk assumption unless a specific coupler design has measured data.

This loss is separate from coax loss, connector loss, and matching loss.

## Candidate Coupler Geometries

- small loop
- rectangular loop
- folded element
- patch
- microstrip-like plate
- capacitive plate
- inductive loop
- resonant parasitic element
- broadband coupler
- switchable 900 MHz and 1800 MHz couplers

## Mechanical Variables

- phone height
- phone horizontal offset
- phone-to-coupler gap
- phone rotation
- coupler orientation
- phone case installed or removed
- nonmetal support material

Initial gap sweep target: about 2 mm to 30 mm.

## Measurement Rule

Do not assume the best position. Measure it and record repeatability.

Also record whether the result is sensitive to small placement errors, because a public build must work outside a lab.

## Desktop Conclusion

The passive coupler is currently the highest-uncertainty part of Architecture 1. Before any passive antenna design is approved, the project needs either:

- a repeatable coupler measurement fixture, or
- a simulation and measurement plan that shows the selected antenna has enough margin to survive realistic coupler loss.

Until then, the phone-at-RF-location architecture remains the baseline to beat.
