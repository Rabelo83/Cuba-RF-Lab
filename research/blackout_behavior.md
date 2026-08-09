# Blackout Behavior

Status: research baseline

## Working Concern

ETECSA cellular site behavior may change during power outages. Some technologies or bands may be shut down, power-limited, or unstable during long blackouts.

## Engineering Impact

A design that works only on LTE Band 3 during normal power may fail during an outage if LTE is shut down or if the serving site loses power. The project must test real outage behavior.

## Required Tests

- Test Nauta Hogar modem sync from solar power.
- Test Internet through Nauta Hogar during outage.
- Test phone service indoors.
- Test phone service outdoors.
- Test high-window, roof, and street-corner locations.
- Record blackout duration at the time of each measurement.

## Do Not Assume

- Do not assume 4G remains active.
- Do not assume 3G remains active.
- Do not assume a working voice signal means data is usable.
- Do not assume a powered house means upstream telecom infrastructure is powered.

