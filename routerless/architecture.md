# Routerless Architecture

Status: CONCEPT

## Preferred Path

```text
ETECSA/Cubacel network
-> ordinary Android phone at best RF location
-> USB tethering, Wi-Fi hotspot, or Ethernet adapter
-> travel router, access point, bridge, or house router
-> house Wi-Fi
```

## Why This Comes First

This path avoids transporting weak cellular RF through long coax. It also avoids specialized LTE router service and keeps the cellular device easy to replace.

For the public mission, this is the cost baseline. Any passive antenna/coupler design must be compared against the total cost and reliability of simply placing an ordinary phone at the best RF location and moving data by USB, Ethernet, or Wi-Fi.

## Candidate Placements

- high indoor window
- protected roof-edge enclosure
- protected outdoor enclosure
- rooftop area if safe
- nearby best-RF point with Wi-Fi bridge back to the house

## Risks

- phone overheating
- unstable tethering
- battery swelling if continuously charged
- weatherproofing failure
- USB cable voltage drop
- Wi-Fi path blocked by walls or metal roof
- phone band support mismatch

## Public Release Criteria

- Use ordinary phones and consumer networking parts where possible.
- Record total working-system cost, not only router cost.
- Separate minimum required parts from optional improvements.
- Prefer setups that can be repaired with common cables, chargers, and enclosures.
- Document whether this path works during real blackouts before recommending it publicly.
