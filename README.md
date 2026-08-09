# Cuba RF Lab

Repository name: `Cuba-RF-Lab`

Public documentation site:

```text
https://rabelo83.github.io/Cuba-RF-Lab/
```

The site source lives in `docs/` and is built with MkDocs. Because this repository is currently using branch-based GitHub Pages from `main`, the generated static site is also committed at the repository root so the public site matches the local MkDocs preview.

Plain-language public build paths:

```text
https://rabelo83.github.io/Cuba-RF-Lab/keep-it-simple/
```

## Mission

Cuba RF Lab is an engineering project for low-cost, blackout-resilient communication at a house in Matanzas, Cuba. The goal is to bring usable ETECSA/Cubacel connectivity into the home during long power outages using practical, repairable, legal, and locally adaptable systems.

The broader goal is public benefit: turn the research, simulations, measurements, and blueprints into a solution that can help Cuban people who are struggling with communication during blackouts. Engineering choices must prioritize the lowest practical production cost while still delivering useful, safe, reliable connectivity.

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

Current public-source desktop baseline:

- Priority bands: 900 MHz and 1800 MHz
- Likely 900 MHz use: GSM and UMTS Band 8
- Likely 1800 MHz use: LTE Band 3
- Possible additional bands: 700 MHz and 2100 MHz in some areas

These are not final field facts. The repository keeps source URLs, source dates, source classes, and confidence levels in `research/`, and local blackout measurements remain required before any final public blueprint.

## Current Status

Version: 0.1.0 research baseline

Status:

- Repository structure initialized.
- Public GitHub Pages documentation site configured.
- Branch-based Pages output generated from MkDocs and committed at repository root.
- Bilingual Keep It Simple section created for plain-language public build paths.
- Public-benefit and low-production-cost objective documented.
- Engineering rules documented.
- First public-source network/coax/passive-coupler evidence added.
- First desktop link-budget scenarios added for phone-first and passive antenna/coupler paths.
- Measurement templates created.
- Starter calculation scripts created.
- Local owner-side field measurement and material collection are temporarily unavailable, but expected later.
- No antenna blueprint is approved.
- No gain, VSWR, impedance, or field performance is claimed.

## Next Milestones

1. Improve direct official ETECSA/regulatory source coverage for current bands and import constraints.
2. Identify realistic low-cost reference phones, supported bands, and practical tethering options from public sources and manufacturer specs.
3. Build desktop material and component availability notes from public sources while local observations are unavailable.
4. Simulate candidate antennas using realistic materials, feed assumptions, and tolerances.
5. Compare every passive antenna path against the phone-at-best-RF-location baseline before any fabrication dimensions are promoted to buildable status.
