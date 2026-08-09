# Sources / Fuentes

<span class="status-badge status-concept">Desktop research</span>
<span class="status-badge status-warning">Not field validation</span>

This page lists the public links currently used by Cuba RF Lab.

Esta pagina muestra los enlaces publicos que usa Cuba RF Lab.

## Important Note / Nota Importante

English: These links support desktop research, assumptions, and scenario modeling. They do not prove what works at one specific house in Cuba during a blackout. Field measurements are still required before any final blueprint is approved.

Español: Estos enlaces apoyan la investigacion de escritorio, las suposiciones y los escenarios. No prueban lo que funciona en una casa especifica en Cuba durante un apagon. Todavia hacen falta mediciones reales antes de aprobar un plano final.

Access date for the first source pass: 2026-08-09.

## Network And Bands / Red Y Bandas

| Source | What it supports | Class | Confidence |
| --- | --- | --- | --- |
| [Cuba.Travel communications page](https://www.cuba.travel/en/useful-information/communications) | Public compatibility baseline for 3G Band 8 at 900 MHz and 4G Band 3 at 1800 MHz. | B | High for national compatibility baseline; not blackout-specific. |
| [Granma/ETECSA mobile technology forum, 2018-06-14](https://www.granma.cu/cuba/2018-06-14/forodebate-tecnologia-movil-digital-en-cuba-14-06-2018-15-06-01?page=25) | Historical ETECSA-context discussion of 900 MHz 2G/3G use, 1800 MHz LTE Band 3 plan, and 2100 MHz indoor-use context. | B | High for historical baseline; medium for current 2026 local conditions. |
| [Powertec ETECSA technical profile](https://portal.powertec.com.au/industry-resources/companies/etecsa) | Third-party technical listing for 3G B8 900 MHz, LTE B3 1800 MHz, and later LTE B1/B28/B8 entries. | E | Medium; useful but still needs official or local confirmation. |

## Coax And Feedline / Cable Coaxial

| Source | What it supports | Class | Confidence |
| --- | --- | --- | --- |
| [McGill Microwave RG58 page](https://www.mcgillmicrowave.com/rg58/) | RG-58-class loss benchmark at 900 MHz and 1800 MHz. | C | Medium; product-specific benchmark. |
| [Belden 8240 RG-58 product page](https://www.belden.com/products/cable/coax-triax-cable/50-ohm-coax-cable/8240) | Manufacturer attenuation benchmark for RG-58 at 900 MHz and nominal impedance information. | C | High for that cable product. |
| [DigiKey mirror of Times Microwave LMR-240 datasheet](https://www.digikey.com/en/htmldatasheets/production/3391245/0/0/1/lmr-240) | LMR-240 attenuation benchmarks at 900 MHz and 1800 MHz. | C | High for datasheet values; Cuba availability unknown. |
| [Cross RF Times Microwave LMR-400 cable assembly page](https://www.crossrf.com/flexible-cables-c-433_322/times-microwave-lmr400-cable-assembly-p-844.html) | LMR-400-class attenuation guide at 900 MHz and 1800 MHz. | E | Medium; useful reseller technical data. |
| [Times Microwave attenuation engineering note](https://timesmicrowave.com/attenuation/) | General principle that larger-diameter coax usually reduces attenuation but increases weight and bend-radius constraints. | C | High for the engineering principle. |

## Passive Coupling / Acoplamiento Pasivo

| Source | What it supports | Class | Confidence |
| --- | --- | --- | --- |
| [OnWireless patch cable and cradle guide](https://remoteone.com.au/support/patch-cable-cradle-guide/) | Order-of-magnitude passive cradle and passive patch loss assumptions; placement sensitivity warning. | E | Medium; vendor guidance, not project measurement. |
| [OnWireless passive antenna coupler product page](https://remoteone.com.au/product/universal-passive-antenna-coupler-for-mobile-phones/) | Practical warning that inductive patches are less effective than direct connections and depend on placement near the phone antenna. | E | Medium; product/vendor claim. |

## Project Decisions / Decisiones Del Proyecto

| Source | What it supports | Class | Confidence |
| --- | --- | --- | --- |
| [Project decisions ledger](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/DECISIONS.md) | Mission, low-cost priority, passive RF boundary, and phone-at-RF-location baseline decision. | Internal | High as a project constraint. |
| [Research source ledger](https://github.com/Rabelo83/Cuba-RF-Lab/blob/main/research/sources.md) | Full repository source table with claim, source date, access date, class, confidence, and notes. | Internal | High as the current project ledger. |

## Source Classes / Clases De Fuentes

| Class | Meaning |
| --- | --- |
| A | Official ETECSA. |
| B | Cuban government or official publication. |
| C | Equipment manufacturer. |
| D | Peer-reviewed or engineering reference. |
| E | Reputable technical third party. |
| F | Forum, marketplace, anecdotal, or field observation. |
