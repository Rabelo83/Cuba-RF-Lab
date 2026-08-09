# Calculations

Status: starter tools

This directory contains small Python 3 utilities for early engineering estimates.

Current scripts:

- `wavelength_calculations.py`: wavelength, half wavelength, and quarter wavelength for target frequencies.
- `coax_loss.py`: feedline loss calculator with editable cable attenuation values.
- `link_budget.py`: simple received-signal delta calculator that separates coax, connector, matching, passive-coupler, and miscellaneous losses.

These scripts do not replace RF simulation or field measurement.

Calculation notes must include system-level losses and production-cost implications where relevant. A design with good element dimensions is still not practical if coax, connector, matching, passive-coupler, or material costs erase the benefit.

## Current Scenario Notes

- `desktop_link_budget_scenarios.md`: first desktop comparison of phone-at-RF-location versus passive antenna/coax/coupler architectures.
- `../data/processed/desktop_link_budget_scenarios.csv`: machine-readable scenario table.

The current desktop scenarios show that passive antenna gain can be erased by coax and passive-coupler losses. Architecture 2, where the phone is placed at the strongest practical RF location and data is moved by USB, Ethernet, or Wi-Fi, remains the baseline to beat.
