# Open Questions

## Highest Priority

1. Which current public sources best document ETECSA/Cubacel bands and service behavior in Matanzas or nearby Cuban regions?
2. Which low-cost Android phones are realistic reference devices for Cuba, and which 2G, 3G, and 4G bands do they support?
3. What conservative signal scenarios should be simulated for indoor, high window, outdoor, roof, and street-corner placements while local measurements are temporarily unavailable?
4. What exact coax type is used in the observed Cuban passive antenna kit?
5. What is the passive coupler loss and how sensitive is it to phone position?
6. What is the lowest production cost for a system that still works well enough to help families?
7. Which parts can be sourced, fabricated, repaired, or substituted inside Cuba?
8. What assumptions must remain blocked until the owner or a collaborator can provide field measurements later?

## Network

- What EARFCN, UARFCN, or channel values are visible from the target location?
- Does the phone report LTE Band 3, UMTS Band 8, GSM 900, or another band?
- Does SINR improve or worsen when moving to higher signal locations?
- Are there seasonal, weather, or outage-duration effects?
- Which public or third-party reports can be used as weak proxies while local measurements are temporarily unavailable?

## Antenna

- Which topology is best for 800 to 2200 MHz broadband coverage under local material constraints?
- Is a narrow 1800 MHz antenna worthwhile if LTE is often unavailable during blackout?
- Is a dedicated 900 MHz antenna required for blackout resilience?
- Does any passive antenna/coupler system beat simply placing the phone at the best RF location after all losses are counted?
- Which candidate ranks highest after simulation: LPDA, 900 MHz Yagi, 1800 MHz Yagi, dual-band/nested antenna, biquad, panel/patch, or another passive design? Partial answer as of 2026-08-09: the seeded `Y900_5EL_SEED` and `Y1800_5EL_SEED` Yagis both fail as given (see `simulations/results/first_pass_yagi_comparison.md`); neither can be ranked against the others until re-simulated with a redesigned director geometry.
- What director length taper and spacing pattern actually produces a working 900 MHz and 1800 MHz Yagi, given that the first-pass uniform wavelength-scaled seed did not? (New question raised by the first NEC pass, 2026-08-09.)
- What polarization is used by the reachable serving sites?
- What antenna height is safe and useful?

## Coupler

- Where is the internal antenna on the actual phone model?
- Which passive coupler geometry gives the best repeatable improvement?
- What phone-to-coupler gap works best?
- Is one broadband coupler better than switchable 900 MHz and 1800 MHz couplers?

## Import and Materials

- Which components can be fabricated locally?
- Which parts can be imported without technical authorization?
- Which parts may require UPTCER authorization?
- What substitutes are available for low-loss coax, connectors, waterproof enclosures, and routers?
- What is the realistic cost range for each path?
- Which components are required for a minimum working system, and which are optional improvements?
- Which design is cheapest to repair after weather damage or normal wear?
- Which online marketplace or public-source prices are reasonable proxies for Cuban availability, and which are too unreliable?
