# Blueprints

Blueprint status values:

- CONCEPT
- CALCULATED
- SIMULATED
- PROTOTYPE
- FIELD_TESTED
- APPROVED

No blueprint is approved at repository initialization.

Rules:

- `blueprints/draft/` may contain concepts, calculations, and prototype notes.
- `blueprints/approved/` may contain only reviewed designs with calculations, simulation, and review notes.
- If a design has not been field tested, it must clearly state `NOT FIELD VALIDATED`.
- Antenna blueprints also require documented topology comparison in `antenna/candidate_comparison.md` and a selection reason in `DECISIONS.md`.
- Public-ready blueprints must include production cost, required tools, local substitutes, and repair notes.
- Prefer the lowest-cost design that reliably solves the communication problem.
