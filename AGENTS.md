# AGENTS.md

This repository is the source of truth for ETECSA-RF-Lab. Do not rely on chat memory when continuing the project.

## Required Reading

Before meaningful work, every AI or human collaborator must read:

1. `README.md`
2. `PROJECT_STATE.md`
3. `DECISIONS.md`
4. `ASSUMPTIONS.md`
5. `OPEN_QUESTIONS.md`
6. `HANDOFF.md`
7. Any files directly relevant to the task

## Safety Boundaries

Do not design:

- active cellular RF repeaters
- cellular power amplifiers
- jammers
- IMSI catchers
- base station emulators
- unauthorized transmitters
- systems intended to bypass carrier controls

Prefer:

- passive RF structures
- ordinary consumer phones
- passive directional antennas
- passive phone couplers
- legal consumer networking equipment
- USB, Ethernet, or Wi-Fi data transport after cellular reception
- modular and repairable parts

## Documentation Rules

- Every engineering decision belongs in `DECISIONS.md`.
- Every uncertain technical assumption belongs in `ASSUMPTIONS.md`.
- Every unresolved research or measurement gap belongs in `OPEN_QUESTIONS.md`.
- Every meaningful work session must update `HANDOFF.md`.
- Every user-provided measurement must be stored under `data/raw/`.
- Never label a design as optimized without calculations or simulation.
- Never invent gain, VSWR, impedance, pattern, or measured performance.
- Separate facts, assumptions, calculations, simulations, and field measurements.

## Blueprint Status

Allowed status values:

- CONCEPT
- CALCULATED
- SIMULATED
- PROTOTYPE
- FIELD_TESTED
- APPROVED

Nothing may enter `blueprints/approved/` unless it has calculations, simulation, and review notes. If it has not been field tested, it must clearly say `NOT FIELD VALIDATED`.

## Preferred Workflow

```text
research
-> requirements
-> calculation
-> simulation
-> prototype drawing
-> test
-> revision
-> approved blueprint
```

## Python Style

- Python 3
- standard library first
- clear functions
- docstrings
- type hints where practical
- no unnecessary dependencies

