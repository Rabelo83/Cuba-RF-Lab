# Decisions

## 2026-08-09: Use Two Parallel Tracks

Decision: pursue both a routerless phone-at-best-RF-location architecture and an improved passive antenna/coupler architecture.

Reason: the routerless path may be simpler and more robust, while the passive coupler path may match local Cuban materials and avoid dedicated LTE router service.

## 2026-08-09: Do Not Make Dedicated ETECSA Router Service Primary

Decision: do not make an expensive dedicated ETECSA modem/router/uSIM service the primary solution.

Reason: project economics favor ordinary phones and modular consumer networking.

## 2026-08-09: Prefer Ordinary Phones

Decision: use an ETECSA-compatible Android phone or similar consumer cellular device as the preferred cellular endpoint.

Reason: ordinary phones are easier to obtain, replace, test, and power than specialized cellular routers.

## 2026-08-09: Prefer Passive RF Systems

Decision: prioritize passive antennas, passive couplers, and legal consumer data transport.

Reason: this avoids unauthorized active cellular repeaters and keeps the project aligned with legal and safety boundaries.

## 2026-08-09: Prioritize 900 MHz and 1800 MHz

Decision: use 900 MHz and 1800 MHz as the initial engineering priorities.

Reason: public information suggests these are important ETECSA/Cubacel bands, but they still require current local verification.

## 2026-08-09: Require Real Blackout Measurements

Decision: no final design can rely only on normal-power signal readings.

Reason: ETECSA site behavior may change during blackouts.

## 2026-08-09: Minimize Long Cellular-Frequency Coax

Decision: avoid transporting weak cellular RF over long coax where practical.

Reason: coax loss at 900 to 2100 MHz can erase antenna benefit, especially with thin or unknown cable.

## 2026-08-09: Repository Is Source of Truth

Decision: all important project knowledge must live in repository files.

Reason: future AI and human collaborators need continuity without relying on chat history.

