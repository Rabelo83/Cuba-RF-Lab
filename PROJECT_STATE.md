# Project State

Date: 2026-08-09

Version: 0.1.0 research baseline

## Known Context

Project owner: Alfredo

Target installation: Matanzas, Cuba

Primary need: resilient basic communication during blackouts, especially when the house has solar power but ETECSA/Cubacel cellular and Nauta Hogar infrastructure may be impaired.

## Current Engineering Direction

The project is proceeding on two parallel tracks:

1. Track A: place an ordinary ETECSA-compatible phone at the best RF location, then bring data into the house over USB, Ethernet, Wi-Fi, or a bridge.
2. Track B: improve a local passive antenna-plus-phone-coupler concept using calculations, simulation, and measurements.

## Existing Local Passive Concept

A locally sold passive kit in Matanzas has been observed. It appears to include:

- directional rooftop antenna
- coax cable
- passive phone coupling structure
- wood or nonmetal phone fixture
- ordinary phone placed near the coupler

The listing was described as a 4G antenna and had an approximate observed price of 6000 CUP. This is local feasibility evidence only. It is not technical proof and its dimensions must not be copied as a design.

## Frequency Baseline

Current priority assumptions:

- 900 MHz first priority for lower-band resilience
- 1800 MHz second priority for LTE Band 3 performance
- Optional broadband research from about 800 MHz to 2200 MHz

Possible ETECSA behavior during outages includes shutting down 4G or 3G while lower-power or legacy service survives longer. This must be measured locally.

## Current Repository Status

- Documentation baseline created.
- Public GitHub Pages site configured with MkDocs.
- Current live deployment path is branch-based Pages from `main`, using committed static MkDocs output at the repository root.
- Public `Keep It Simple` section added for bilingual plain-language build paths.
- Calculation scripts created for wavelength, coax loss, and simple received-signal delta.
- Measurement CSV template created.
- No simulation results yet.
- No CAD files yet.
- No final dimensions yet.
- No approved blueprints yet.

## Immediate Next Work

1. Verify current ETECSA band information with dated sources.
2. Measure phone signal in the target locations.
3. Confirm the phone model and supported bands.
4. Research realistic coax and connector availability.
5. Prepare first antenna models for simulation.
