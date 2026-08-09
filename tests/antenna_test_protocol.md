# Antenna Test Protocol

Status: initial protocol

## Objective

Compare candidate antenna placements and prototypes without inventing performance claims.

Each antenna test must also compare the passive antenna/coupler path against the simpler phone-at-RF-location baseline.

## Before Testing

- Confirm antenna status.
- Confirm target band.
- Inspect mechanical safety.
- Record coax type and length.
- Record connector types.
- Record antenna height and azimuth.

## Measurements

- phone signal without antenna or coupler
- phone signal with antenna/coupler
- RSRP, RSRQ, SINR, RSSI if available
- ping, upload, download
- app-level success
- weather and blackout state
- parts used and estimated cost
- coax length, connector count, and coupler type
- whether cheaper substitute materials were used

## Rule

Do not report gain unless measured with an appropriate method. Phone signal improvement is a system result, not antenna gain.

Do not recommend a public antenna build unless the net improvement is large enough to justify its cost, coax loss, coupling loss, roof work, and repair complexity.
