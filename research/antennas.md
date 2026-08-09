# Antenna Research

Status: topic map

## Candidate Topologies

- LPDA for broadband 800 to 2200 MHz investigation
- 1800 MHz Yagi for LTE Band 3 performance
- 900 MHz Yagi for lower-band blackout resilience
- dual-band Yagi concepts
- nested Yagi concepts
- biquad and double biquad
- panel or patch arrays
- corner reflector
- passive reflector designs
- low-cost MIMO concepts
- dual-polarized directional systems

## Evaluation Criteria

- target frequency or bandwidth
- expected gain from simulation only
- impedance
- SWR and return loss
- radiation pattern
- polarization
- material diameter
- boom geometry
- feed arrangement
- local manufacturability
- weatherproofing
- safety
- import considerations
- production cost
- repairability and local substitution options

## Current Status

No antenna topology is selected for final build. LPDA, 900 MHz Yagi, and 1800 MHz Yagi are the first structured research paths.

The LPDA is not preferred by default. Use `antenna/candidate_comparison.md` before selecting any antenna topology for fabrication-ready blueprints.

First pre-simulation geometry seeds now exist for:

- 900 MHz 5-element Yagi
- 900 MHz 7-element Yagi
- 1800 MHz 5-element Yagi
- 1800 MHz 7-element Yagi
- 800-2200 MHz LPDA seed
- 1800 MHz biquad seed
- 2100 MHz biquad seed

The first simulation priority is to compare the simplest 900 MHz and 1800 MHz Yagi seeds against the complete passive-chain loss budget, then test whether extra elements, LPDA bandwidth, or biquad simplicity justify their tradeoffs.

Detailed comparison framework:

- `antenna/candidate_comparison.md`
- `data/templates/antenna_candidate_comparison.csv`
- `calculations/preliminary_antenna_geometry.md`
- `data/processed/antenna_candidate_first_pass.csv`
- `simulations/nec/first_pass_queue.md`
