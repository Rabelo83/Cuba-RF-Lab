"""First-pass NEC2 simulation of the Y900_5EL_SEED and Y1800_5EL_SEED Yagi
candidates queued in `simulations/nec/first_pass_queue.md`.

This script builds free-space NEC2 wire models from the geometry seeds in
`calculations/preliminary_antenna_geometry.py`, sweeps conductor diameter,
frequency, and dimensional tolerance, and writes raw sweep data to
`data/processed/` plus summarized results to `simulations/results/`.

All Yagi elements are modeled as separate, unconnected horizontal wires
(radius = conductor_diameter / 2) stacked along the boom axis, fed with a
voltage source at the center segment of the driven element. The model is
free space (no ground plane), consistent with `scripts/nec_smoke_test.py`.

Orientation convention used throughout this script:

- Element (dipole) axis: X.
- Boom axis (reflector at 0, directors increasing): Y.
- "Forward" (toward the directors) is phi = 90 degrees.
- "Back" (toward the reflector) is phi = 270 degrees.
- "Horizontal pattern" = theta = 90 degrees, phi swept (the plane containing
  both the element axis and the boom axis).
- "Vertical pattern" = phi fixed at the forward direction, theta swept from
  0 to 180 degrees.

These are geometric simulation conventions, not a statement about real-world
mounting orientation, which is up to the installer.
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import necpp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "calculations"))
from preliminary_antenna_geometry import (  # noqa: E402
    CandidateGeometry,
    WireElement,
    build_candidates,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PROCESSED = REPO_ROOT / "data" / "processed"
RESULTS_DIR = REPO_ROOT / "simulations" / "results"
SEGMENTS_PER_ELEMENT = 21  # odd, matches scripts/nec_smoke_test.py sizing logic


@dataclass(frozen=True)
class SolvePoint:
    freq_mhz: float
    conductor_diameter_mm: float
    length_offset_mm: float
    spacing_offset_mm: float
    resistance_ohm: float
    reactance_ohm: float
    vswr_50: float
    forward_gain_dbi: float
    back_gain_dbi: float
    front_to_back_db: float


def offset_elements(
    elements: tuple[WireElement, ...], length_offset_mm: float, spacing_offset_mm: float
) -> tuple[WireElement, ...]:
    """Apply a uniform per-element length and per-position spacing offset.

    This models a first-order fabrication/measurement tolerance stress test:
    every element is uniformly too long/short, and every gap along the boom
    is uniformly too wide/narrow. It is not a per-element random error model.
    """

    return tuple(
        WireElement(
            name=element.name,
            position_mm=element.position_mm + (spacing_offset_mm if element.position_mm > 0 else 0.0),
            length_mm=element.length_mm + length_offset_mm,
        )
        for element in elements
    )


def build_nec(
    elements: tuple[WireElement, ...],
    conductor_diameter_mm: float,
    freq_mhz: float,
):
    """Build a free-space NEC2 model. Caller must nec_delete() the handle."""

    radius_m = (conductor_diameter_mm / 2.0) / 1000.0
    nec = necpp.nec_create()

    driven_tag = None
    for tag, element in enumerate(elements, start=1):
        half_length_m = (element.length_mm / 1000.0) / 2.0
        y_m = element.position_mm / 1000.0
        result = necpp.nec_wire(
            nec,
            tag,
            SEGMENTS_PER_ELEMENT,
            -half_length_m, y_m, 0.0,
            half_length_m, y_m, 0.0,
            radius_m,
            1.0,
            1.0,
        )
        if result != 0:
            raise RuntimeError(necpp.nec_error_message())
        if element.name == "driven":
            driven_tag = tag

    if driven_tag is None:
        raise ValueError("geometry has no element named 'driven'")

    if necpp.nec_geometry_complete(nec, 0) != 0:
        raise RuntimeError(necpp.nec_error_message())
    if necpp.nec_gn_card(nec, -1, 0, 0, 0, 0, 0, 0, 0) != 0:
        raise RuntimeError(necpp.nec_error_message())
    if necpp.nec_fr_card(nec, 0, 1, freq_mhz, 0) != 0:
        raise RuntimeError(necpp.nec_error_message())

    center_segment = (SEGMENTS_PER_ELEMENT + 1) // 2
    if necpp.nec_ex_card(nec, 0, driven_tag, center_segment, 0, 1.0, 0, 0, 0, 0, 0) != 0:
        raise RuntimeError(necpp.nec_error_message())

    return nec


def vswr(resistance_ohm: float, reactance_ohm: float, z0_ohm: float = 50.0) -> float:
    z = complex(resistance_ohm, reactance_ohm)
    gamma = abs((z - z0_ohm) / (z + z0_ohm))
    if gamma >= 1.0:
        return float("inf")
    return (1.0 + gamma) / (1.0 - gamma)


def solve_forward_back(
    elements: tuple[WireElement, ...],
    conductor_diameter_mm: float,
    freq_mhz: float,
    length_offset_mm: float = 0.0,
    spacing_offset_mm: float = 0.0,
) -> SolvePoint:
    working_elements = offset_elements(elements, length_offset_mm, spacing_offset_mm)
    nec = build_nec(working_elements, conductor_diameter_mm, freq_mhz)
    try:
        # theta=90 fixed, phi = 90 (forward) then 270 (back).
        if necpp.nec_rp_card(nec, 0, 1, 2, 0, 5, 0, 0, 90, 90, 0, 180, 0, 0) != 0:
            raise RuntimeError(necpp.nec_error_message())

        resistance = necpp.nec_impedance_real(nec, 0)
        reactance = necpp.nec_impedance_imag(nec, 0)
        forward_gain = necpp.nec_gain(nec, 0, 0, 0)
        back_gain = necpp.nec_gain(nec, 0, 0, 1)

        return SolvePoint(
            freq_mhz=freq_mhz,
            conductor_diameter_mm=conductor_diameter_mm,
            length_offset_mm=length_offset_mm,
            spacing_offset_mm=spacing_offset_mm,
            resistance_ohm=resistance,
            reactance_ohm=reactance,
            vswr_50=vswr(resistance, reactance),
            forward_gain_dbi=forward_gain,
            back_gain_dbi=back_gain,
            front_to_back_db=forward_gain - back_gain,
        )
    finally:
        necpp.nec_delete(nec)


def horizontal_cut(
    elements: tuple[WireElement, ...], conductor_diameter_mm: float, freq_mhz: float
) -> list[tuple[float, float]]:
    """Gain in dBi vs. azimuth (phi, degrees) at theta = 90 degrees."""

    nec = build_nec(elements, conductor_diameter_mm, freq_mhz)
    try:
        if necpp.nec_rp_card(nec, 0, 1, 360, 0, 5, 0, 0, 90, 0, 0, 1, 0, 0) != 0:
            raise RuntimeError(necpp.nec_error_message())
        return [(float(phi), necpp.nec_gain(nec, 0, 0, phi)) for phi in range(360)]
    finally:
        necpp.nec_delete(nec)


def vertical_cut(
    elements: tuple[WireElement, ...], conductor_diameter_mm: float, freq_mhz: float
) -> list[tuple[float, float]]:
    """Gain in dBi vs. elevation (theta, degrees) at phi = 90 degrees (forward)."""

    nec = build_nec(elements, conductor_diameter_mm, freq_mhz)
    try:
        if necpp.nec_rp_card(nec, 0, 181, 1, 0, 5, 0, 0, 0, 90, 1, 0, 0, 0) != 0:
            raise RuntimeError(necpp.nec_error_message())
        return [(float(theta), necpp.nec_gain(nec, 0, theta, 0)) for theta in range(181)]
    finally:
        necpp.nec_delete(nec)


def half_power_beamwidth_deg(cut: list[tuple[float, float]], peak_angle_hint: float) -> float | None:
    """Estimate HPBW (degrees) around the peak nearest peak_angle_hint.

    Walks outward from the peak sample in both directions and linearly
    interpolates the angle where gain first drops 3 dB below the peak.
    Returns None if the pattern never drops 3 dB within the sampled cut.
    """

    peak_index = min(range(len(cut)), key=lambda i: abs(cut[i][0] - peak_angle_hint))
    peak_angle, peak_gain = cut[peak_index]
    threshold = peak_gain - 3.0

    def find_crossing(step: int) -> float | None:
        i = peak_index
        while 0 <= i + step < len(cut):
            angle_a, gain_a = cut[i]
            angle_b, gain_b = cut[i + step]
            if gain_b <= threshold < gain_a:
                if gain_a == gain_b:
                    return angle_b
                fraction = (gain_a - threshold) / (gain_a - gain_b)
                return angle_a + fraction * (angle_b - angle_a)
            i += step
        return None

    lower = find_crossing(-1)
    upper = find_crossing(1)
    if lower is None or upper is None:
        return None
    return abs(upper - lower)


def frequency_grid(low_mhz: float, high_mhz: float, step_mhz: float) -> list[float]:
    points = []
    freq = low_mhz
    while freq <= high_mhz + 1e-9:
        points.append(round(freq, 3))
        freq += step_mhz
    return points


def write_sweep_csv(path: Path, rows: list[SolvePoint]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "freq_mhz",
                "conductor_diameter_mm",
                "length_offset_mm",
                "spacing_offset_mm",
                "resistance_ohm",
                "reactance_ohm",
                "vswr_50",
                "forward_gain_dbi",
                "back_gain_dbi",
                "front_to_back_db",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.freq_mhz,
                    row.conductor_diameter_mm,
                    row.length_offset_mm,
                    row.spacing_offset_mm,
                    f"{row.resistance_ohm:.3f}",
                    f"{row.reactance_ohm:.3f}",
                    f"{row.vswr_50:.3f}" if row.vswr_50 != float("inf") else "inf",
                    f"{row.forward_gain_dbi:.3f}",
                    f"{row.back_gain_dbi:.3f}",
                    f"{row.front_to_back_db:.3f}",
                ]
            )


def run_candidate(
    candidate: CandidateGeometry,
    freq_range: tuple[float, float, float],
    diameters_mm: list[float],
    checkpoints_mhz: list[float],
    length_offsets_mm: list[float],
    spacing_offsets_mm: list[float],
) -> dict:
    freqs = frequency_grid(*freq_range)
    nominal_diameter = diameters_mm[len(diameters_mm) // 2]

    diameter_sweep_rows: list[SolvePoint] = []
    for diameter in diameters_mm:
        for freq in freqs:
            diameter_sweep_rows.append(solve_forward_back(candidate.elements, diameter, freq))

    tolerance_rows: list[SolvePoint] = []
    for offset in length_offsets_mm:
        for freq in checkpoints_mhz:
            tolerance_rows.append(
                solve_forward_back(candidate.elements, nominal_diameter, freq, length_offset_mm=offset)
            )
    for offset in spacing_offsets_mm:
        if offset == 0.0:
            continue  # nominal already captured by the length_offsets_mm pass
        for freq in checkpoints_mhz:
            tolerance_rows.append(
                solve_forward_back(candidate.elements, nominal_diameter, freq, spacing_offset_mm=offset)
            )

    center_freq = candidate.target_mhz
    h_cut = horizontal_cut(candidate.elements, nominal_diameter, center_freq)
    v_cut = vertical_cut(candidate.elements, nominal_diameter, center_freq)
    h_hpbw = half_power_beamwidth_deg(h_cut, peak_angle_hint=90.0)
    v_hpbw = half_power_beamwidth_deg(v_cut, peak_angle_hint=90.0)

    checkpoint_rows = [
        row for row in diameter_sweep_rows
        if row.conductor_diameter_mm == nominal_diameter and row.freq_mhz in checkpoints_mhz
    ]

    return {
        "candidate": candidate,
        "nominal_diameter_mm": nominal_diameter,
        "diameter_sweep_rows": diameter_sweep_rows,
        "tolerance_rows": tolerance_rows,
        "checkpoint_rows": checkpoint_rows,
        "horizontal_hpbw_deg": h_hpbw,
        "vertical_hpbw_deg": v_hpbw,
    }


def main() -> None:
    candidates = {c.candidate_id: c for c in build_candidates()}

    plans = {
        "Y900_5EL_SEED": dict(
            freq_range=(880.0, 960.0, 5.0),
            diameters_mm=[4.0, 6.0, 8.0],
            checkpoints_mhz=[900.0, 925.0, 945.0, 960.0],
        ),
        "Y1800_5EL_SEED": dict(
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

        print(f"=== {candidate_id} ===")
        print(f"Nominal conductor diameter: {result['nominal_diameter_mm']} mm")
        print("Checkpoint results (nominal diameter):")
        for row in result["checkpoint_rows"]:
            print(
                f"  {row.freq_mhz:>7.1f} MHz  Z={row.resistance_ohm:+7.2f}{row.reactance_ohm:+7.2f}j ohm  "
                f"VSWR={row.vswr_50:5.2f}  gain={row.forward_gain_dbi:6.2f} dBi  "
                f"F/B={row.front_to_back_db:5.2f} dB"
            )
        print(f"Horizontal HPBW at {candidate.target_mhz:.0f} MHz: {result['horizontal_hpbw_deg']}")
        print(f"Vertical HPBW at {candidate.target_mhz:.0f} MHz: {result['vertical_hpbw_deg']}")
        print()


if __name__ == "__main__":
    main()
