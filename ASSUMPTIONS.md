# Assumptions

Confidence levels:

- High: likely correct but still useful to verify
- Medium: plausible and needs confirmation
- Low: speculative or anecdotal

## Network

| Assumption | Confidence | Notes |
| --- | --- | --- |
| ETECSA/Cubacel service in Cuba includes 900 MHz operation. | High | Supported by Cuba.Travel, Granma/ETECSA 2018 forum, and Powertec. Still requires local phone measurements before site-specific claims. |
| ETECSA/Cubacel service in Cuba includes LTE Band 3 around 1800 MHz. | High | Supported by Cuba.Travel and third-party technical band records. Still requires local blackout measurements before design approval. |
| 700 MHz or 2100 MHz may exist in some network areas. | Medium | Supported by public/third-party sources, but not yet enough to drive the first low-cost blueprint. Include in broadband awareness. |
| During long blackouts, 4G may be less available than 2G or 3G. | Low | Plausible but not source-backed for the target site. Must be measured during actual outages before using as a design fact. |

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
| A passive phone coupler can improve reception for some phone positions. | Low | Public guidance suggests several dB of coupling loss and strong placement sensitivity. Homemade coupler loss and repeatability are unknown. |
| Locally available coax may not be low-loss 50-ohm cable. | Medium | Source-backed benchmarks show RG-58 class losses are high at cellular frequencies. Actual Cuban availability remains unknown. |
| A phone placed at the best RF location may outperform a passive antenna/coupler chain. | Medium | Desktop link-budget scenarios show passive coupler and coax losses can erase antenna gain. Needs later field validation. |

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
