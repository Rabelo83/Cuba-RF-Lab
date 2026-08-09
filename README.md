# ETECSA-RF-Lab

Alternate name: Project ETECSA Phoenix

Public documentation site:

```text
https://rabelo83.github.io/ETECSA-RF-Lab/
```

The site is built from `docs/` with MkDocs and deployed by GitHub Actions.

## Mission

ETECSA-RF-Lab is an engineering project for low-cost, blackout-resilient communication at a house in Matanzas, Cuba. The goal is to bring usable ETECSA/Cubacel connectivity into the home during long power outages using practical, repairable, legal, and locally adaptable systems.

This project is receive-focused and consumer-equipment-focused. It must not design or encourage unauthorized cellular repeaters, power amplifiers, jammers, IMSI catchers, base station emulators, or systems intended to bypass ETECSA network controls.

## Problem

During frequent blackouts, nearby ETECSA infrastructure may lose power. The house can remain powered by solar, but indoor cellular signal may be weak or absent. A usable signal may exist at a nearby outdoor location, roof point, window, or street corner.

The communication need is basic but important:

- WhatsApp
- IMO
- messaging
- voice over Internet
- basic Internet access

## Two-Track Strategy

### Track A: Rebuild From Scratch

Preferred architecture:

```text
ETECSA surviving tower
-> best available RF location
-> ordinary Android phone with ETECSA SIM
-> USB tethering, Wi-Fi hotspot, or Ethernet adapter
-> ordinary router, access point, bridge, or travel router
-> house Wi-Fi
```

Primary rule: do not transport weak cellular RF farther than necessary. Put the phone or receiver where RF is best, convert to data immediately, then transport data over USB, Ethernet, or Wi-Fi.

### Track B: Improve Existing Passive Cuban System

Observed local concept:

```text
directional rooftop antenna
-> coax
-> passive phone coupling element
-> ordinary cellular phone near the coupler
```

This path is valuable because it avoids an active repeater and can use ordinary phones. It must be improved through calculation, simulation, controlled measurements, and repeatable mechanical fixtures rather than copied from photos.

## ETECSA-Specific Baseline

Current public baseline assumptions to verify:

- Priority bands: 900 MHz and 1800 MHz
- Likely 900 MHz use: GSM and UMTS Band 8
- Likely 1800 MHz use: LTE Band 3
- Possible additional bands: 700 MHz and 2100 MHz in some areas

These are not final facts. The repository must keep source URLs, source dates, source classes, and confidence levels in `research/`.

## Current Status

Version: 0.1.0 research baseline

Status:

- Repository structure initialized.
- Public GitHub Pages documentation site configured.
- Engineering rules documented.
- Measurement templates created.
- Starter calculation scripts created.
- No antenna blueprint is approved.
- No gain, VSWR, impedance, or field performance is claimed.

## Next Milestones

1. Verify which ETECSA bands are active in the target Matanzas area during normal power and during blackouts.
2. Identify available phone model, supported bands, and practical tethering options.
3. Measure signal at indoor, outdoor, roof, window, and street-corner locations.
4. Build research baseline for coax, antennas, passive phone coupling, and Cuban import constraints.
5. Model candidate antennas before any fabrication dimensions are promoted to buildable status.
