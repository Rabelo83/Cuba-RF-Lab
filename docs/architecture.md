# System Architecture

Status: CONCEPT

## Goal

Bring usable ETECSA/Cubacel connectivity into the house during blackouts while avoiding unauthorized active cellular RF systems.

The public goal is broader than one house: develop a solution that can be offered to Cuban families at the lowest practical production cost while still being safe, legal, repairable, and useful.

## Preferred Architecture

```text
ETECSA surviving tower
-> best available RF location
-> ordinary phone with ETECSA SIM
-> USB tethering, Wi-Fi hotspot, or Ethernet adapter
-> router, access point, bridge, or travel router
-> house Wi-Fi
```

## Architecture Principles

- Put the cellular device where the signal is best.
- Convert cellular RF to data as early as practical.
- Transport data instead of weak RF when possible.
- Keep the system modular and repairable.
- Prefer parts that can be replaced independently.
- Avoid designs that require specialized carrier service unless all low-cost paths fail.
- Compare total working-system cost, including phone, router, coax, coupler, weatherproofing, tools, and replacement parts.
- Prefer the cheapest architecture that works reliably enough for real communication.

## Passive RF Alternative

The passive antenna and phone-coupler track may be useful when the phone cannot be placed at the best RF location or when a local-style passive kit can be improved.

This alternative is still research-stage and requires measured coupler performance.

It must also prove that antenna gain can overcome coax, connector, mismatch, and passive-coupler losses at a production cost lower than other practical options.
