# Materials

<span class="status-badge status-concept">Initial categories only</span>

Materials are tracked as categories until exact models, availability, and import status are verified.

Availability in Cuba must be saved as project data, not only remembered from chat. When local information is provided, add it to the raw material availability ledger first, then update summary docs only when the evidence supports it.

## Candidate Local Materials

| Material | Possible Use | Current Availability Status |
| --- | --- | --- |
| Aluminum rod or tube | antenna elements, booms | Unknown |
| Copper wire | antenna elements, couplers, grounding | Unknown |
| PVC | supports, nonmetal fixtures | Unknown |
| Wood | temporary fixtures, phone holder | Unknown |
| Plastic sheet or box | enclosure, coupler fixture | Unknown |
| Screws and fasteners | mechanical assembly | Unknown |
| Coax cable | antenna feedline | Unknown type and loss |
| RF connectors | feedline joins | Unknown |
| Ferrites | noise suppression | Unknown |

## Design Philosophy

- Prefer local fabrication where performance and safety allow.
- Prefer ordinary parts over specialized carrier equipment.
- Prefer the lowest production cost that still gives useful, safe connectivity.
- Document substitutions and their expected tradeoffs.
- Do not invent component availability or import legality.
- Track cost ranges and required tools before recommending public build paths.

## Cuba Availability Ledger

Use this raw data file for local availability inputs:

[data/raw/material_availability_cuba.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/raw/material_availability_cuba.csv)

Use this template for the required columns:

[data/templates/material_availability_cuba.csv](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/data/templates/material_availability_cuba.csv)

Record one dated row per observation. Keep old rows when price or availability changes, because supply stability matters for public production.

## Repository Sources

- [Bill of materials](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/materials/bill_of_materials.md)
- [Cost model](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/materials/cost_model.md)
- [Cuba local materials](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/materials/cuba_local_materials.md)
- [Importable components](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/materials/importable_components.md)
- [Substitutes](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/materials/substitutes.md)
