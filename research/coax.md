# Coax and Feedline Research

Status: public-source desktop baseline, local availability unknown

Access date for the current source pass: 2026-08-09.

## Principle

Shorten cellular-frequency coax whenever possible. At 900 to 2100 MHz, feedline loss can erase much of the benefit from an antenna.

For public production, coax is both an RF loss and a cost risk. A cheaper phone-at-RF-location setup may outperform a high-gain antenna if the antenna requires long or poor-quality coax.

## Desktop Attenuation Benchmarks

These are source-backed benchmarks for scenario modeling. They are not proof that the same cable is available in Cuba.

| Cable type | Source example | Impedance | 900 MHz loss | 1800 MHz loss | 5 m loss at 900 | 5 m loss at 1800 | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| RG-58 class | McGill RG58 | 50 ohm | 51.2 dB/100 m | 73.5 dB/100 m | 2.56 dB | 3.68 dB | Cheap and common-looking, but high loss for rooftop cellular runs. |
| RG-58 class | Belden 8240 | 52 ohm nominal | 13.7 dB/100 ft, about 44.9 dB/100 m | Not listed at 1800 MHz | 2.25 dB | Unknown | Manufacturer data confirms RG-58 loss is already large at 900 MHz. |
| LMR-240 class | Times/Fairview/DigiKey-style datasheet values | 50 ohm | 24.8 dB/100 m | 35.6 dB/100 m | 1.24 dB | 1.78 dB | Better compromise if importable; still costly in long runs. |
| LMR-400 class | Cross RF / Times assembly data | 50 ohm | 12.8 dB/100 m | 18.6 dB/100 m | 0.64 dB | 0.93 dB | Much lower loss, but thicker, heavier, harder to route, and likely more expensive. |
| Unknown local 75-ohm TV coax | No project source yet | Usually 75 ohm | Unknown | Unknown | Unknown | Unknown | Treat as unapproved for feedline until measured or identified. Mismatch and shield quality may be major risks. |

Length examples:

| Cable type | 10 m loss at 900 | 10 m loss at 1800 |
| --- | ---: | ---: |
| RG-58 class, McGill benchmark | 5.12 dB | 7.35 dB |
| LMR-240 class | 2.48 dB | 3.56 dB |
| LMR-400 class | 1.28 dB | 1.86 dB |

## Practical Interpretation

- Use the shortest possible cellular-frequency coax.
- A phone-at-RF-location architecture avoids most feedline loss and may beat a passive antenna/coupler path even when the antenna has higher advertised gain.
- If passive antenna/coupler architecture is used, keep coax as short as physically practical and document the cable type.
- Unknown cable should be modeled as RG-58-or-worse until identified, measured, or replaced with a known low-loss type.
- 75-ohm TV coax may be available locally, but it is not automatically acceptable for a 50-ohm phone-coupler antenna system.
- Coax cost must be included in antenna ranking. A design that requires expensive coax may lose against a simpler phone-at-roof-location path.

## Cable Types to Research

- RG-58
- RG-174
- RG-316
- CFD-200
- LMR-200
- LMR-240
- LMR-400
- equivalent Chinese low-loss cables
- unknown local 75-ohm TV coax

## Required Attenuation Data

Record attenuation at:

- 900 MHz
- 1800 MHz
- 2100 MHz

For each cable, document:

- impedance
- diameter
- loss per meter or per 100 meters
- source
- connector compatibility
- availability
- import status if known
- estimated cost
- practical minimum usable length
- local substitutes and their expected loss

## Source Notes

See `research/sources.md` for the full source ledger. Current benchmark sources include manufacturer or technical reseller data for Belden RG-58, McGill RG58, LMR-240 class cable, and LMR-400 class cable, plus Times Microwave engineering guidance that larger cable diameter generally lowers attenuation while increasing mass and bend-radius requirements.
