# Data Templates

<span class="status-badge status-concept">Measurement template ready</span>

The project needs real measurements more than guesses. Store raw measurements in `data/raw/` and keep processed summaries in `data/processed/`.

## Blackout Measurement Template

Use this CSV template:

[data/templates/blackout_measurement.csv](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/data/templates/blackout_measurement.csv)

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

[data/templates/antenna_candidate_comparison.csv](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/data/templates/antenna_candidate_comparison.csv)

Do not fill it with advertised antenna gain. Use calculated, simulated, measured, or clearly labeled assumption values.

## Production Cost Estimate Template

Use this CSV template when a design starts becoming a public build package:

[data/templates/production_cost_estimate.csv](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/data/templates/production_cost_estimate.csv)

Cost estimates should separate required parts from optional improvements and identify local substitutes whenever possible.
