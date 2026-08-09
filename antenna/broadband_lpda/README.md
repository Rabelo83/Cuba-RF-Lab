# Broadband LPDA

Status: CONCEPT

## Goal

Investigate a log-periodic directional antenna that can cover roughly 800 to 2200 MHz for resilience across possible ETECSA bands.

The LPDA is not the selected or preferred antenna by default. It must compete against the other candidates in `antenna/candidate_comparison.md`.

## Current Notes

An early conceptual LPDA discussion used approximate values around:

- tau = 0.86
- sigma about 0.16
- element lengths roughly 17.8 cm down to 5.3 cm

These numbers are not approved blueprints. They are not build data and must not be fabricated without proper calculation, simulation, and review.

The current pre-simulation seed is `LPDA_800_2200_SEED` in `../../calculations/preliminary_antenna_geometry.md`. It deliberately keeps the earlier tau/sigma idea as a test candidate, not as a preferred antenna.

## Evaluation Questions

- Can local materials support the required element spacing and tolerances?
- Is the feed arrangement practical?
- Is broadband gain sufficient compared with narrower antennas?
- What coax length is unavoidable?
- Does the phone or passive coupler limit the antenna benefit?
- Does broadband coverage justify higher fabrication complexity and cost compared with simpler narrowband antennas?
