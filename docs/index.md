# Cuba RF Lab

<span class="status-badge status-concept">Research baseline</span>
<span class="status-badge status-warning">No approved antenna blueprint yet</span>
<span class="status-badge status-stop">No active cellular repeater designs</span>

Cuba RF Lab is a practical engineering project for low-cost, blackout-resilient communication on ETECSA/Cubacel service in Cuba, especially for a target installation in Matanzas.

The project exists to help Cuban people who are struggling with communication during blackouts. It focuses on ordinary phones, passive antennas, passive phone couplers, safe field testing, and data transport by USB, Ethernet, or Wi-Fi after cellular reception.

![Preferred communication architecture](assets/diagrams/system-architecture.svg){ .site-diagram }

## What This Project Is

This project is a public engineering notebook and manual for:

- documenting the communication problem during long blackouts
- testing which ETECSA bands and locations actually work
- comparing passive antenna and coupler ideas
- reducing production cost without sacrificing useful connectivity
- building standard operating procedures for safe field work
- creating public blueprints only after calculation, simulation, and review
- helping collaborators continue without relying on chat memory

## What This Project Is Not

This project does not design or recommend:

- active cellular RF repeaters
- cellular power amplifiers
- jammers
- IMSI catchers
- base station emulators
- unauthorized transmitters
- systems intended to bypass ETECSA controls

## The Two Engineering Tracks

### Track A: Phone First

Put an ordinary ETECSA-compatible phone where the signal is best, then move data into the house.

```text
ETECSA network
-> phone at best RF location
-> USB, Wi-Fi, or Ethernet
-> router or access point
-> house Wi-Fi
```

### Track B: Improved Passive System

Study and improve a local passive concept:

```text
directional antenna
-> coax
-> passive phone coupler
-> ordinary phone
```

This track is useful only if measurement proves the passive coupler and antenna system gives repeatable benefit.

## Start Here

<div class="grid cards" markdown>

-   **Keep It Simple**

    Plain-language bilingual build paths: what to use, how to assemble it, and what is not approved yet.

    [Open Keep It Simple](keep-it-simple.md)

-   **Field SOPs**

    Use the blackout, antenna, phone coupler, and NanoVNA test procedures before collecting results.

    [Open SOPs](sops.md)

-   **Blueprint Status**

    Understand the difference between concepts, prototypes, field-tested designs, and approved blueprints.

    [Open Blueprints](blueprints.md)

-   **Research Baseline**

    Track ETECSA bands, blackout behavior, coax loss, passive coupling, and import rules.

    [Open Research](research.md)

-   **Collaborate**

    Learn how contributors and AI agents should update the repository without losing context.

    [Open Collaboration](collaboration.md)

</div>

## Current Public Status

- Version: 0.1.0 research baseline
- No field-validated antenna design exists yet.
- No approved blueprint exists yet.
- Local owner-side field measurement is temporarily unavailable, but expected later.
- First public-source network, coax, and passive-coupler evidence has been added.
- First desktop link-budget scenarios have been added.
- First antenna pre-simulation geometry seeds and NEC queue have been added.
- Python `necpp` NEC2 solver is installed and smoke-tested.
- The first priority now is first antenna simulations, official/regulatory source improvement, and component/material desktop research.

The recommended next engineering task is to run the 900 MHz 5-element Yagi versus 1800 MHz 5-element Yagi simulation comparison and compare each passive path against the phone-at-best-RF-location baseline. Field validation remains required before any final public blueprint.
