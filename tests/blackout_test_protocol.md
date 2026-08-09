# Blackout Test Protocol

Status: initial protocol

## Objective

Measure what communication options actually survive during outages at the target Matanzas location.

## Safety

Do not climb, work on roofs, or handle outdoor wiring during unsafe weather or darkness. Do not test near power lines.

## Test Locations

- inside house
- high indoor window
- outside wall
- roof or highest safe point
- nearby street corner

## Data to Record

Use `data/templates/blackout_measurement.csv`.

Required fields include:

- date
- time
- location
- phone model
- network type
- band
- EARFCN if available
- RSRP
- RSRQ
- SINR
- RSSI if available
- ping
- download
- upload
- WhatsApp text success
- WhatsApp call success
- IMO call success
- antenna orientation and height if used
- blackout duration
- notes

## First Test Sequence

1. Power the Nauta Hogar modem/router from solar.
2. Check DSL sync.
3. Test Internet.
4. Record phone signal indoors.
5. Record phone signal outdoors.
6. Record phone signal at the best safe elevated point.
7. Test WhatsApp and IMO.

