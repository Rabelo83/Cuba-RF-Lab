# NanoVNA Test Protocol

Status: initial protocol

## Objective

Use a NanoVNA to evaluate prototype matching behavior.

NanoVNA results are useful only when they support a practical low-cost design decision, such as rejecting a badly matched prototype or comparing material substitutions.

## Required Steps

1. Warm up the NanoVNA if recommended by its documentation.
2. Calibrate over the target frequency range.
3. Use appropriate calibration standards.
4. Measure S11.
5. Record return loss and SWR.
6. Identify resonance and bandwidth.
7. Document fixture and feedline effects.

## Limits

A NanoVNA does not directly measure antenna gain. Do not claim gain from NanoVNA data alone.

Do not treat a good S11 result as approval for public fabrication unless simulation, field testing, cost, and repairability are also documented.
