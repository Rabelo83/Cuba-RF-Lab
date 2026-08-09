# Standard Operating Procedures

<span class="status-badge status-concept">Initial SOPs</span>
<span class="status-badge status-warning">Field validation required</span>

These SOPs are intended to keep measurements repeatable and safe. They are not a substitute for local safety judgment.

Because the final goal is a public low-cost solution, SOPs should record not only what works, but also what tools, materials, time, and replacement parts were needed.

## Available SOPs

| SOP | Purpose | Repository Source |
| --- | --- | --- |
| Blackout test protocol | Measure what communication options survive during outages. | [tests/blackout_test_protocol.md](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/tests/blackout_test_protocol.md) |
| Antenna test protocol | Compare placements and prototypes without inventing gain. | [tests/antenna_test_protocol.md](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/tests/antenna_test_protocol.md) |
| Phone coupler test protocol | Sweep passive coupler positions and record repeatability. | [tests/phone_coupler_test_protocol.md](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/tests/phone_coupler_test_protocol.md) |
| NanoVNA test protocol | Measure matching, S11, SWR, and return loss. | [tests/nanovna_test_protocol.md](https://github.com/Rabelo83/ETECSA-RF-Lab/blob/main/tests/nanovna_test_protocol.md) |

## Minimum Field Safety Rules

- Do not climb or work near outdoor wiring during unsafe weather.
- Keep masts, antennas, ladders, and tools away from power lines.
- Do not test on roofs alone.
- Do not handle outdoor antenna systems during lightning risk.
- Stop the test if the setup becomes unsafe.

## Blackout Measurement Sequence

1. Power the existing Nauta Hogar modem/router from solar if possible.
2. Check DSL synchronization.
3. Test Internet over DSL.
4. Measure phone service indoors.
5. Measure service at high window, outside wall, roof or highest safe point, and street corner.
6. Record network type, band, RSRP, RSRQ, SINR, ping, upload, download, and app success.
7. Record blackout duration and notes.

## RF Reporting Rule

Phone signal improvement is a system result. Do not call it antenna gain unless gain was measured with a method appropriate for antenna gain.
