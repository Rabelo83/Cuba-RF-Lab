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

