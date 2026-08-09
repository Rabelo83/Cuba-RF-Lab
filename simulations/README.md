# Simulations

Status: planned

Simulation files and results belong here. Do not treat a design as buildable until its modeling assumptions, geometry, and results are documented.

Simulation exists to choose the lowest-cost practical design that can work in Cuba, not to chase maximum theoretical gain. Include material choices, tolerances, and likely fabrication limits in the model notes whenever they affect the result.

Current first-pass queue:

- `nec/first_pass_queue.md`
- `../calculations/preliminary_antenna_geometry.md`
- `../data/processed/antenna_candidate_first_pass.csv`

Local solver status on 2026-08-09: `xnec2c`, `nec2c`, and `openEMS` were not found in the local environment. The next simulation step is to install or choose a solver, then generate model files from the pre-simulation geometry seeds.

Candidate tools:

- NEC2 or NEC4-compatible modeling
- xnec2c
- 4NEC2 file generation
- OpenEMS
- Python geometry generation

Record:

- tool and version
- geometry
- material assumptions
- feed location
- frequency sweep
- impedance
- SWR or return loss
- radiation pattern
- limitations
- construction tolerance assumptions
- material diameter sensitivity
- expected coax and matching losses
- cost or fabrication implications
- comparison against simpler phone-at-RF-location architecture
