# Data Templates

<span class="status-badge status-concept">Measurement template ready</span>

The project needs real measurements more than guesses. Store raw measurements in `data/raw/` and keep processed summaries in `data/processed/`.

Local owner-side data collection is temporarily unavailable, so the current phase also stores clearly labeled desktop scenario data. Desktop data must never be described as measured field performance.

## Blackout Measurement Template

Use this CSV template:

[data/templates/blackout_measurement.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/templates/blackout_measurement.csv)

Required columns:

```csv
date,time,location,phone_model,network_type,band,earfcn,rsrp_dbm,rsrq_db,sinr_db,rssi_dbm,ping_ms,download_mbps,upload_mbps,whatsapp_text,whatsapp_call,imo_call,antenna_type,antenna_azimuth,antenna_height_m,blackout_duration,notes
```

## Measurement Priorities

1. Indoor baseline.
2. High window.
3. Outside wall.
4. Roof or highest safe point.
5. Street corner.
6. Same locations during blackout.

## Reporting Quality

- Keep raw readings.
- Record phone model.
- Record whether the phone is handheld, fixed, in a case, or near a coupler.
- Record app-level success, not just signal strength.
- Do not optimize only for strongest RSRP if SINR becomes worse.

## Antenna Candidate Comparison Template

Use this CSV template when simulation or calculation results become available:

[data/templates/antenna_candidate_comparison.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/templates/antenna_candidate_comparison.csv)

Do not fill it with advertised antenna gain. Use calculated, simulated, measured, or clearly labeled assumption values.

## Desktop Link-Budget Scenario Data

Current processed scenario table:

[data/processed/desktop_link_budget_scenarios.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/desktop_link_budget_scenarios.csv)

This table compares the phone-at-RF-location architecture against passive antenna/coax/coupler paths using public-source coax benchmarks and conservative passive-coupler assumptions.

## Antenna Candidate First-Pass Data

Current processed candidate worksheet:

[data/processed/antenna_candidate_first_pass.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/processed/antenna_candidate_first_pass.csv)

This table lists pre-simulation geometry scale, rough gain targets, construction risk, passive-chain notes, and simulation priority. It is not measured performance and not build approval.

## Production Cost Estimate Template

Use this CSV template when a design starts becoming a public build package:

[data/templates/production_cost_estimate.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/templates/production_cost_estimate.csv)

Cost estimates should separate required parts from optional improvements and identify local substitutes whenever possible.

## Cuba Material Availability Template

Use this CSV template when local availability information is provided from Cuba:

[data/templates/material_availability_cuba.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/templates/material_availability_cuba.csv)

Append raw observations here:

[data/raw/material_availability_cuba.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/raw/material_availability_cuba.csv)

Record one dated row per material, seller/source type, location, price, availability status, and quality note. Do not publish private contact details unless the project owner explicitly approves it.
