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

## Public Website Rules

The public website is built with MkDocs from `docs/`.

Current GitHub Pages deployment is branch-based from `main` using generated static output committed at the repository root. After changing any file under `docs/` or `mkdocs.yml`, run:

```bash
mkdocs build --strict
cp -R site/. .
```

Then commit both the source documentation and the generated root output. The generated `site/` directory remains ignored; the root `index.html`, section folders, `assets/`, `search/`, `sitemap.xml`, and `.nojekyll` are the files GitHub Pages serves.

## Keep It Simple Rules

`docs/keep-it-simple.md`, `docs/simple-path-a-phone.md`, and `docs/simple-path-b-passive.md` are the public plain-language layer.

For those pages:

- keep text bilingual: English and Spanish
- use plain language
- show only simple blueprints, materials, build steps, and test steps
- avoid RF math and deep engineering discussion
- clearly mark concept or not-field-validated work
- do not publish final dimensions unless the matching engineering files support them

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
