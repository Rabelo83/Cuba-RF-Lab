# Assumptions

Confidence levels:

- High: likely correct but still useful to verify
- Medium: plausible and needs confirmation
- Low: speculative or anecdotal

## Network

| Assumption | Confidence | Notes |
| --- | --- | --- |
| ETECSA/Cubacel service in the area includes 900 MHz operation. | Medium | Requires current source and local phone measurements. |
| ETECSA/Cubacel service in the area includes LTE Band 3 around 1800 MHz. | Medium | Requires current source and local phone measurements. |
| 700 MHz or 2100 MHz may exist in some network areas. | Low | Do not design around these until verified locally. |
| During long blackouts, 4G may be less available than 2G or 3G. | Medium | Must be measured during actual outages. |

## Site

| Assumption | Confidence | Notes |
| --- | --- | --- |
| The house has solar power available during outages. | Medium | User provided context; capacity and wiring remain unknown. |
| Indoor cellular service can be poor while a nearby outdoor point works. | Medium | Needs location-by-location measurements. |
| Nauta Hogar DSL may fail if upstream ETECSA cabinets lose power. | Medium | Test modem sync and Internet during outage. |
| Local field measurements are temporarily unavailable from the project owner. | High | Desktop research, simulation, and conservative assumptions must carry the current phase until the owner or a collaborator can contribute measurements later. |

## Hardware

| Assumption | Confidence | Notes |
| --- | --- | --- |
| An ordinary Android phone can serve as the primary cellular endpoint. | Medium | Depends on phone bands, battery behavior, tethering support, and thermal limits. |
| A passive phone coupler can improve reception for some phone positions. | Low | Coupler loss and repeatability are unknown. |
| Locally available coax may not be low-loss 50-ohm cable. | Medium | Must identify actual cable type and attenuation. |

## Regulatory

| Assumption | Confidence | Notes |
| --- | --- | --- |
| Passive antennas and ordinary phones are safer regulatory choices than active repeaters. | Medium | Exact Cuban rules need official citation. |
| Some routers or telecommunications equipment may require UPTCER authorization under Cuban rules. | Medium | Needs exact official text and practical interpretation. |

## Public Production

| Assumption | Confidence | Notes |
| --- | --- | --- |
| A useful public solution must be cheaper and easier to repair than specialized telecom equipment. | High | This is a project constraint, not a measured RF fact. |
| Designs using ordinary phones and locally substitutable materials are more likely to help Cuban families at scale. | Medium | Must be checked against real availability, cost, and performance. |
| The best final design may be the lowest-cost design that works reliably, not the highest-gain design. | High | This should guide antenna and architecture selection. |
| Public-source material and network information may not reflect real local availability during outages. | High | Treat source-backed conclusions as pre-field-validation guidance until later local checks are possible. |
