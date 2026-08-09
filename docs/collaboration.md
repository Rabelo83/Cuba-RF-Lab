# Collaboration

<span class="status-badge status-concept">Repository is source of truth</span>

The repository is designed so humans and AI agents can continue the project without relying on chat memory.

The shared mission is public benefit for Cuban families during blackouts. Contributors should optimize toward the lowest practical production cost that still gives useful, safe, legal, and repeatable communication.

## Required Reading for Contributors

Before meaningful work, read:

1. [README.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/README.md)
2. [AGENTS.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/AGENTS.md)
3. [PROJECT_STATE.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/PROJECT_STATE.md)
4. [DECISIONS.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/DECISIONS.md)
5. [ASSUMPTIONS.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/ASSUMPTIONS.md)
6. [OPEN_QUESTIONS.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/OPEN_QUESTIONS.md)
7. [HANDOFF.md](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/HANDOFF.md)

## Contribution Rules

- Update `HANDOFF.md` before ending meaningful work.
- Put engineering decisions in `DECISIONS.md`.
- Put uncertain claims in `ASSUMPTIONS.md`.
- Put unresolved items in `OPEN_QUESTIONS.md`.
- Put new raw measurements in `data/raw/`.
- Put source-backed research in `research/sources.md`.
- Keep public pages clear about design status.
- Record cost, local material availability, tool requirements, and repairability when comparing solutions.

## Website Contribution Rules

The public website source lives in `docs/` and is built with MkDocs.

If you edit website source files or `mkdocs.yml`:

1. Run `mkdocs build --strict`.
2. Copy the generated output to the repository root with `cp -R site/. .`.
3. Commit both the source files and generated root output.

GitHub Pages currently serves the repository root from `main`. Do not assume the ignored `site/` folder is published.

## Keep It Simple Rules

The `Keep It Simple` section is for public, plain-language instructions. Keep it bilingual and focused on:

- simple blueprints
- materials
- building instructions
- simple test steps
- clear status labels

Do not add RF math, unresolved engineering debate, or unapproved final dimensions there.

## Good First Contributions

- Add official or reputable sources for current ETECSA band information.
- Add exact Cuban import rule citations.
- Add first field measurements from the target locations when the owner or a safe local collaborator can collect them.
- Identify the available Android phone model and supported bands.
- Add manufacturer attenuation data for realistic coax options.
