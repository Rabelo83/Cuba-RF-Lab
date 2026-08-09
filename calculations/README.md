# Calculations

Status: starter tools

This directory contains small Python 3 utilities for early engineering estimates.

Current scripts:

- `wavelength_calculations.py`: wavelength, half wavelength, and quarter wavelength for target frequencies.
- `coax_loss.py`: feedline loss calculator with editable cable attenuation values.
- `link_budget.py`: simple received-signal delta calculator.

These scripts do not replace RF simulation or field measurement.

Calculation notes must include system-level losses and production-cost implications where relevant. A design with good element dimensions is still not practical if coax, connector, matching, passive-coupler, or material costs erase the benefit.
