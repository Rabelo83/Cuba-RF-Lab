# Desktop Link-Budget Scenarios

Status: desktop engineering scenarios, not measured results

Date: 2026-08-09

These scenarios compare the two project architectures before local measurements are available.

They are intentionally conservative. They are used to decide what to simulate and test next, not to approve any blueprint.

## Architectures Compared

### Architecture 1: Passive Coax/Coupler

```text
ETECSA/Cubacel tower
-> directional antenna
-> coax
-> passive phone coupler
-> ordinary ETECSA-compatible phone
```

### Architecture 2: Phone At RF Location

```text
ETECSA/Cubacel tower
-> ordinary ETECSA-compatible phone positioned at the best RF location
-> USB, Ethernet, or Wi-Fi
-> house network
```

## Core Relationship

For the passive antenna path:

```text
Passive antenna-chain delta =
directional antenna gain
- coax loss
- connector loss
- matching loss
- passive coupling loss
- miscellaneous implementation loss
```

This delta is compared against placing the phone itself at the same strong RF location.

The full improvement relative to a poor indoor phone location is:

```text
Total improvement versus indoor phone =
RF-location improvement
+ passive antenna-chain delta
```

For Architecture 2, there is no passive antenna-chain delta. The improvement is simply the benefit of putting the phone where the signal is better.

## Input Assumptions

| Input | Good-case assumption | Typical-risk assumption | Notes |
| --- | ---: | ---: | --- |
| Phone-at-RF-location gain versus poor indoor location | 6 to 18 dB | 12 dB mid case | Must later be measured at the actual house. |
| 900 MHz Yagi realized gain | 9 dBi | 9 dBi | Placeholder, now known not to match the first simulated seed (see note below). |
| 1800 MHz Yagi realized gain | 12 dBi | 12 dBi | Placeholder, now known not to match the first simulated seed (see note below). |
| High-gain 1800 MHz sensitivity case | 14 dBi | not baseline | Shows what would be needed for a strong passive win. |
| RG-58 5 m loss at 900 MHz | 2.56 dB | 2.56 dB | Based on 51.2 dB/100 m benchmark. |
| RG-58 5 m loss at 1800 MHz | 3.68 dB | 3.68 dB | Based on 73.5 dB/100 m benchmark. |
| LMR-240 5 m loss at 900 MHz | 1.24 dB | 1.24 dB | Based on 24.8 dB/100 m benchmark. |
| LMR-240 5 m loss at 1800 MHz | 1.78 dB | 1.78 dB | Based on 35.6 dB/100 m benchmark. |
| LMR-400 3 m loss at 1800 MHz | 0.56 dB | not baseline | Sensitivity case only. |
| Connector loss | 0.4 to 0.6 dB | 0.6 dB | Placeholder for two connectors. |
| Matching loss | 0.5 to 1.5 dB | 1.5 dB | Depends on antenna, balun, feed, and coupler match. |
| Passive-coupler loss | 3 to 6 dB | 12 dB | 3 dB is optimistic; 6 dB is good-case; 12 dB covers homemade-placement risk. |
| Miscellaneous implementation loss | 1 dB | 1 dB | Mounting, nearby metal, weatherproofing, bends, and construction error. |

## Scenario Results

See the machine-readable table at:

`data/processed/desktop_link_budget_scenarios.csv`

| Scenario | Architecture | Passive chain delta | Total improvement vs poor indoor phone | Advantage vs phone at same RF location | Interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| A_PHONE_LOW | Phone at RF location | 0.00 dB | 6.00 dB | 0.00 dB | Weak outdoor placement improvement still may beat lossy passive chains. |
| A_PHONE_MID | Phone at RF location | 0.00 dB | 12.00 dB | 0.00 dB | Current baseline comparison case. |
| A_PHONE_HIGH | Phone at RF location | 0.00 dB | 18.00 dB | 0.00 dB | Strong placement improvement is difficult for passive coax/coupler to beat cheaply. |
| B900_GOOD | Passive 900 MHz Yagi, LMR-240, 5 m, 6 dB coupler | -0.84 dB | 11.16 dB | -0.84 dB | Slightly worse than phone at same RF location unless it improves SINR enough to matter. |
| B900_TYPICAL | Passive 900 MHz Yagi, RG-58, 5 m, 12 dB coupler | -8.66 dB | 3.34 dB | -8.66 dB | Not promising unless assumptions improve greatly. |
| B1800_GOOD | Passive 1800 MHz Yagi, LMR-240, 5 m, 6 dB coupler | 1.62 dB | 13.62 dB | 1.62 dB | Small RF-power win; may be useful if directivity improves SINR. |
| B1800_TYPICAL | Passive 1800 MHz Yagi, RG-58, 5 m, 12 dB coupler | -6.78 dB | 5.22 dB | -6.78 dB | Not promising for public build without better coax and coupler. |
| B1800_SENSITIVITY | Passive 1800 MHz high-gain Yagi, LMR-400, 3 m, 3 dB coupler | 8.54 dB | 20.54 dB | 8.54 dB | Shows a possible passive win, but requires low coupler loss, low-loss coax, tight construction, and cost proof. |

## Engineering Takeaways

1. The passive path is dominated by passive-coupler loss and coax loss.
2. Architecture 2 remains the baseline to beat because it avoids cellular-frequency feedline loss.
3. A passive antenna may still win if it provides useful directivity and stable SINR, not only higher RSRP.
4. The first simulations should compare 900 MHz Yagi, 1800 MHz Yagi, broadband LPDA, and dual-band concepts with realistic feed and tolerance assumptions.
5. No passive antenna blueprint should be approved until coupler loss is measured or bounded tightly enough to support the decision.

## Simulation Update (2026-08-10): Working Candidates Found

The 9 dBi / 12 dBi realized-gain assumptions above were placeholders pending simulation. The first NEC pass (2026-08-09) on the original uniform wavelength-scaled seeds (`Y900_5EL_SEED`, `Y1800_5EL_SEED`) failed across their required bands. A follow-up NEC-driven local search (`simulations/nec/optimize_yagi_directors.py`) then found working replacement geometries, `Y900_5EL_OPT_V2_BW` and `Y1800_5EL_OPT_V2_BW`, with flat 11.1-11.5 dBi simulated gain across both required bands -- meeting or nearly meeting the original placeholder. See `simulations/results/y900_5el_opt_v2_bw_first_pass.md` and `simulations/results/y1800_5el_opt_v2_bw_first_pass.md` for full characterization.

The remaining gap is native impedance match, not gain: these candidates have not been fitted with a matching network yet, so feeding them directly from 50 ohm coax loses real power to reflection (2.6-13.5 dB depending on frequency and band). Two scenario rows are added below for each band: as simulated today with no matching network, and with an assumed future matching network achieving the same 1.0 dB matching-loss assumption used in the original placeholder scenarios (not yet designed or simulated -- an assumption, flagged as such).

| Scenario | Antenna basis | Passive chain delta (good case, LMR-240/5m/6dB coupler) | Interpretation |
| --- | --- | ---: | --- |
| B900_SIM_UNMATCHED_WORST | Simulated, worst required check point (960 MHz), no match | -11.14 dB | The 960 MHz edge is unusable without a matching network. |
| B900_SIM_UNMATCHED_BEST3 | Simulated, best of the other three check points (925 MHz), no match | +1.54 dB | Even fully unmatched, most of the required band already beats Track A in the good-case loss stack. |
| B900_SIM_WITH_FUTURE_MATCH | Simulated raw gain (worst required check point, 11.11 dBi) + assumed 1.0 dB matching loss | +1.37 dB | Assumes a matching network not yet designed. |
| B1800_SIM_UNMATCHED_WORST | Simulated, worst required check point (1880 MHz), no match | -7.56 dB | Weakest point, but still better than the 900 MHz worst case. |
| B1800_SIM_UNMATCHED_BEST | Simulated, best required check point (1840 MHz), no match | -0.80 dB | Close to breakeven even fully unmatched. |
| B1800_SIM_WITH_FUTURE_MATCH | Simulated raw gain (worst required check point, 11.08 dBi) + assumed 1.0 dB matching loss | +0.80 dB | Assumes a matching network not yet designed. |

These deltas use the same good-case loss stack as `B900_GOOD`/`B1800_GOOD` above (LMR-240, 5 m, connector 0.5 dB, coupler 6 dB, misc 1 dB). The typical-risk loss stack (RG-58, 12 dB coupler) would push all of these solidly negative, same as the original placeholder scenarios -- coupler loss is still the dominant risk, simulated gain or not.

## Sources

Network band baseline and coax/coupler values are recorded in `research/sources.md`.
