# Cuba Local Materials

Status: plausible categories, availability unknown

The following material categories may be locally plausible, but nothing is confirmed until documented with source, observation, or purchase.

For each material, future notes should include approximate local cost, source location, required tools, repair difficulty, and whether the material can be substituted without breaking the design.

## Cuba Availability Input Ledger

User-provided availability information from Cuba should be saved in:

```text
data/raw/material_availability_cuba.csv
```

Use the template:

```text
data/templates/material_availability_cuba.csv
```

Record one row per material observation. Do not overwrite old observations when availability or price changes; add a dated row so the project can see how stable the supply is.

## Fields To Capture

- date
- province and municipality
- source type: store, workshop, scrapyard, marketplace, personal observation, or other
- material and specification
- quantity or unit size
- price and currency
- availability status: available, scarce, uncertain, not available, or seasonal
- whether it appears local or imported
- compatible project use
- substitute material if relevant
- required tools
- quality and repair notes
- confidence level
- privacy notes before publishing seller or contact details

| Material | Possible Use | Availability |
| --- | --- | --- |
| Aluminum rod or tube | antenna elements, booms | Unknown |
| Copper wire | antenna elements, couplers, grounding | Unknown |
| PVC | supports, weather-resistant nonmetal parts | Unknown |
| Wood | temporary fixtures, nonmetal phone holder | Unknown |
| Plastic sheet or box | coupler fixture, enclosure | Unknown |
| Screws and fasteners | mechanical assembly | Unknown |
| Coax cable | feedline | Unknown type and loss |
| RF connectors | antenna and feedline joins | Unknown |
| Ferrites | noise suppression, cable management | Unknown |
| Silicone or tape | weatherproofing | Unknown |

Public designs should prefer materials that can be bought, salvaged, repaired, or replaced locally without specialized RF suppliers.

This summary table should be updated only after the raw availability ledger has enough dated observations to justify changing `Unknown` to a more confident status.
