# Handoff

Date: 2026-08-09

The project is ETECSA-RF-Lab, also called Project ETECSA Phoenix. It aims to improve blackout-resilient communications for a house in Matanzas, Cuba, using legal, low-cost, modular, repairable systems centered on ordinary phones, passive antennas, passive couplers, and data transport by USB, Ethernet, or Wi-Fi.

Critical boundary: do not design active cellular repeaters, RF amplifiers, jammers, IMSI catchers, base station emulators, or anything intended to bypass ETECSA controls.

Current strategy has two tracks:

1. Track A: place an ETECSA-compatible Android phone at the best RF location and bring data into the house.
2. Track B: improve a local passive directional antenna plus phone-coupler concept through measurement, calculation, and simulation.

Priority bands are currently assumed to be 900 MHz and 1800 MHz, with optional research from roughly 800 to 2200 MHz. This still needs current source verification and local measurements during blackouts.

No buildable antenna blueprint exists yet. Do not create final fabrication dimensions until research, calculations, and simulation are ready.

Current repository state:

- Local git repository initialized on branch `main`.
- GitHub remote: `https://github.com/Rabelo83/ETECSA-RF-Lab.git`.
- Initial project baseline committed and pushed.
- GitHub Pages site configured with MkDocs in `mkdocs.yml`.
- Pages deployment workflow added at `.github/workflows/pages.yml`.
- Expected public site URL: `https://rabelo83.github.io/ETECSA-RF-Lab/`.
- First Pages workflow run `31320108396` triggered but failed at `Configure GitHub Pages`; repository admin likely needs to set Pages source to GitHub Actions, then rerun the workflow.
- Starter scripts were run successfully.
- Python compile check passed with `PYTHONPYCACHEPREFIX` set to `/private/tmp/etecsa_rf_lab_pycache` because the default macOS bytecode cache path was outside the writable workspace.

Recommended next task: fill `research/sources.md` and `research/etecsa_network.md` with dated source citations for current ETECSA bands, then perform first local signal measurements using `data/templates/blackout_measurement.csv`.
