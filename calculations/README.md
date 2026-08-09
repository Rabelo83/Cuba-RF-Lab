# Calculations

Status: starter tools

This directory contains small Python 3 utilities for early engineering estimates.

Engineering dependencies are pinned in `../requirements-engineering.txt`.

Current scripts:

- `wavelength_calculations.py`: wavelength, half wavelength, and quarter wavelength for target frequencies.
- `coax_loss.py`: feedline loss calculator with editable cable attenuation values.
- `link_budget.py`: simple received-signal delta calculator that separates coax, connector, matching, passive-coupler, and miscellaneous losses.
- `preliminary_antenna_geometry.py`: pre-simulation geometry seed generator for first-pass antenna candidates.

These scripts do not replace RF simulation or field measurement.

Calculation notes must include system-level losses and production-cost implications where relevant. A design with good element dimensions is still not practical if coax, connector, matching, passive-coupler, or material costs erase the benefit.

## Current Scenario Notes

- `desktop_link_budget_scenarios.md`: first desktop comparison of phone-at-RF-location versus passive antenna/coax/coupler architectures.
- `preliminary_antenna_geometry.md`: first antenna geometry seeds for NEC/openEMS modeling.
- `../data/processed/desktop_link_budget_scenarios.csv`: machine-readable scenario table.
- `../data/processed/antenna_candidate_first_pass.csv`: machine-readable first-pass candidate worksheet.

The current desktop scenarios show that passive antenna gain can be erased by coax and passive-coupler losses. Architecture 2, where the phone is placed at the strongest practical RF location and data is moved by USB, Ethernet, or Wi-Fi, remains the baseline to beat.

## Local Toolchain Check

Run from the repository root:

```bash
.venv/bin/pip install -r requirements-engineering.txt
.venv/bin/python scripts/nec_smoke_test.py
```

If a script imports Matplotlib, set:

```bash
MPLCONFIGDIR=.cache/matplotlib
```
