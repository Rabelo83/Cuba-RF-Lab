"""Full characterization pass for the NEC-optimized Yagi candidates.

Runs the same frequency/diameter/tolerance sweeps used for the original
`*_5EL_SEED` candidates (see `run_first_pass_yagi.py`) against the
NEC-optimized geometries from `optimize_yagi_directors.py`, now recorded
in `calculations/preliminary_antenna_geometry.build_optimized_candidates`.

Also computes a more robust front-to-back figure than the single-point
phi=270 sample used in the first pass: a point sample can land exactly on
a very narrow, construction-tolerance-fragile pattern null (see the
"1009 dB" artifact discussed in the results file), so this script reports
front-to-rear-hemisphere as (forward peak) - (highest gain anywhere in the
180-360 degree half), which is far less sensitive to exactly where a
single deep null happens to fall.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "calculations"))

from preliminary_antenna_geometry import build_optimized_candidates  # noqa: E402
from run_first_pass_yagi import (  # noqa: E402
    DATA_PROCESSED,
    half_power_beamwidth_deg,
    horizontal_cut,
    run_candidate,
    vertical_cut,
    write_sweep_csv,
)


def robust_front_to_rear_db(cut: list[tuple[float, float]]) -> tuple[float, float, float]:
    forward_peak = max(gain for phi, gain in cut if phi <= 90 or phi >= 270 or phi == 0)
    forward_peak = max(gain for _phi, gain in cut)  # true peak, wherever it falls
    rear_candidates = [gain for phi, gain in cut if 180.0 < phi < 360.0]
    rear_peak = max(rear_candidates)
    return forward_peak, rear_peak, forward_peak - rear_peak


def mismatch_loss_db(vswr: float) -> float:
    if vswr <= 1.0:
        return 0.0
    gamma = (vswr - 1.0) / (vswr + 1.0)
    return -10.0 * __import__("math").log10(1.0 - gamma * gamma)


def main() -> None:
    candidates = {c.candidate_id: c for c in build_optimized_candidates()}

    plans = {
        "Y900_5EL_OPT_V1": dict(
            freq_range=(880.0, 960.0, 5.0),
            diameters_mm=[4.0, 6.0, 8.0],
            checkpoints_mhz=[900.0, 925.0, 945.0, 960.0],
        ),
        "Y1800_5EL_OPT_V1": dict(
            freq_range=(1710.0, 1880.0, 10.0),
            diameters_mm=[3.0, 4.0, 6.0],
            checkpoints_mhz=[1710.0, 1800.0, 1840.0, 1880.0],
        ),
        "Y900_5EL_OPT_V2_BW": dict(
            freq_range=(880.0, 960.0, 5.0),
            diameters_mm=[4.0, 6.0, 8.0],
            checkpoints_mhz=[900.0, 925.0, 945.0, 960.0],
        ),
        "Y1800_5EL_OPT_V2_BW": dict(
            freq_range=(1710.0, 1880.0, 10.0),
            diameters_mm=[3.0, 4.0, 6.0],
            checkpoints_mhz=[1710.0, 1800.0, 1840.0, 1880.0],
        ),
    }
    length_offsets_mm = [0.0, 1.0, -1.0, 3.0, -3.0]
    spacing_offsets_mm = [0.0, 1.0, -1.0, 3.0, -3.0]

    for candidate_id, plan in plans.items():
        candidate = candidates[candidate_id]
        result = run_candidate(
            candidate,
            length_offsets_mm=length_offsets_mm,
            spacing_offsets_mm=spacing_offsets_mm,
            **plan,
        )
        slug = candidate_id.lower()
        write_sweep_csv(DATA_PROCESSED / f"{slug}_diameter_freq_sweep.csv", result["diameter_sweep_rows"])
        write_sweep_csv(DATA_PROCESSED / f"{slug}_tolerance_sweep.csv", result["tolerance_rows"])

        h_cut = horizontal_cut(candidate.elements, result["nominal_diameter_mm"], candidate.target_mhz)
        forward_peak, rear_peak, robust_fb = robust_front_to_rear_db(h_cut)

        print(f"=== {candidate_id} ===")
        print(f"Nominal conductor diameter: {result['nominal_diameter_mm']} mm")
        print("Checkpoint results (nominal diameter):")
        for row in result["checkpoint_rows"]:
            mismatch = mismatch_loss_db(row.vswr_50)
            print(
                f"  {row.freq_mhz:>7.1f} MHz  Z={row.resistance_ohm:+7.2f}{row.reactance_ohm:+7.2f}j ohm  "
                f"VSWR={row.vswr_50:5.2f}  gain={row.forward_gain_dbi:6.2f} dBi  "
                f"mismatch_loss={mismatch:5.2f} dB  net={row.forward_gain_dbi - mismatch:6.2f} dBi"
            )
        print(f"Forward peak: {forward_peak:.2f} dBi, rear-hemisphere peak: {rear_peak:.2f} dBi, "
              f"robust front-to-rear: {robust_fb:.2f} dB")
        print(f"Horizontal HPBW at {candidate.target_mhz:.0f} MHz: {result['horizontal_hpbw_deg']}")
        print(f"Vertical HPBW at {candidate.target_mhz:.0f} MHz: {result['vertical_hpbw_deg']}")
        print()


if __name__ == "__main__":
    main()
