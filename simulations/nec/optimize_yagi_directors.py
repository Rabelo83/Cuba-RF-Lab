"""NEC-driven local search for a working Yagi director geometry.

`simulations/results/first_pass_yagi_comparison.md` showed that the
uniform wavelength-scaled director geometry in
`calculations/preliminary_antenna_geometry.py` does not form a working
Yagi at either 900 MHz or 1800 MHz. Rather than substitute a second guess
at director dimensions from memory (the same failure mode as the first
seed), this script uses the already-validated NEC solver itself as the
objective function for a local optimizer (SciPy Nelder-Mead) and lets it
search for a geometry that the solver confirms works.

This is a local search from a reasonable starting point, not a global
optimum and not a claim of the best possible Yagi. Its output still goes
through the same full sweep/tolerance/pattern characterization as the
first-pass seeds before it can be called anything beyond a first working
candidate.

Reflector length and position are held fixed at the first-pass seed's
values (0.500 wavelength, position 0), since the first-pass isolation
test showed the reflector half of that geometry already behaves
correctly (see `simulations/results/y900_5el_seed_first_pass.md`,
"Solver Validation"). Only the driven element and three directors are
optimized, each parameterized as (length, gap-from-previous-element) so
every candidate geometry is automatically ordered and non-overlapping.
"""

from __future__ import annotations

import sys
from pathlib import Path

from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "calculations"))

from preliminary_antenna_geometry import WireElement, wavelength_mm  # noqa: E402
from run_first_pass_yagi import solve_forward_back  # noqa: E402

REFLECTOR_LENGTH_FACTOR = 0.500

# (name, length_bounds_wavelength, gap_bounds_wavelength, initial_length_wl, initial_gap_wl)
FREE_ELEMENTS = [
    ("driven", (0.44, 0.50), (0.08, 0.30), 0.473, 0.15),
    ("director_1", (0.38, 0.46), (0.08, 0.30), 0.440, 0.15),
    ("director_2", (0.36, 0.45), (0.08, 0.30), 0.430, 0.12),
    ("director_3", (0.35, 0.44), (0.08, 0.30), 0.420, 0.10),
]


def vector_to_elements(x: list[float], wavelength_mm_: float) -> tuple[WireElement, ...]:
    elements = [WireElement("reflector", 0.0, REFLECTOR_LENGTH_FACTOR * wavelength_mm_)]
    position_wl = 0.0
    for index, (name, _len_bounds, _gap_bounds, _l0, _g0) in enumerate(FREE_ELEMENTS):
        length_wl = x[2 * index]
        gap_wl = x[2 * index + 1]
        position_wl += gap_wl
        elements.append(
            WireElement(name, position_wl * wavelength_mm_, length_wl * wavelength_mm_)
        )
    return tuple(elements)


def build_bounds() -> list[tuple[float, float]]:
    bounds: list[tuple[float, float]] = []
    for _name, len_bounds, gap_bounds, _l0, _g0 in FREE_ELEMENTS:
        bounds.append(len_bounds)
        bounds.append(gap_bounds)
    return bounds


def build_x0() -> list[float]:
    x0: list[float] = []
    for _name, _len_bounds, _gap_bounds, l0, g0 in FREE_ELEMENTS:
        x0.append(l0)
        x0.append(g0)
    return x0


def objective(x: list[float], target_mhz: float, conductor_diameter_mm: float) -> float:
    wl = wavelength_mm(target_mhz)
    elements = vector_to_elements(x, wl)
    try:
        result = solve_forward_back(elements, conductor_diameter_mm, target_mhz)
    except RuntimeError:
        return 100.0  # NEC failed to solve this geometry (e.g. degenerate wire); penalize heavily
    score = result.forward_gain_dbi + 0.25 * result.front_to_back_db
    return -score


def objective_bandwidth(
    x: list[float], design_wavelength_mm: float, checkpoints_mhz: list[float], conductor_diameter_mm: float
) -> float:
    """Maximize worst-case (minimum) forward gain across all required check points.

    A single-frequency objective can find a narrow, high-Q spike that peaks
    at the target frequency and collapses a short distance away (this is
    exactly what the first optimization pass produced). Using the minimum
    gain across the required check points as the score pushes the search
    toward a geometry that holds up across the whole required band, not
    just at one point in it.

    Physical (mm) dimensions are fixed once, from `design_wavelength_mm`
    (a single reference wavelength) -- they must NOT be re-derived per
    checkpoint frequency. A real antenna has one fixed physical size; only
    the test frequency varies across the sweep. An earlier version of this
    function incorrectly rebuilt the geometry at each checkpoint's own
    wavelength, which silently evaluated a different rescaled antenna per
    frequency instead of one fixed structure's real frequency response.
    """

    elements = vector_to_elements(x, design_wavelength_mm)
    gains = []
    for freq_mhz in checkpoints_mhz:
        try:
            result = solve_forward_back(elements, conductor_diameter_mm, freq_mhz)
        except RuntimeError:
            return 100.0
        gains.append(result.forward_gain_dbi)
    return -min(gains)


def optimize(target_mhz: float, conductor_diameter_mm: float, label: str) -> list[float]:
    bounds = build_bounds()
    x0 = build_x0()

    result = minimize(
        objective,
        x0,
        args=(target_mhz, conductor_diameter_mm),
        method="Nelder-Mead",
        bounds=bounds,
        options={"maxiter": 2000, "xatol": 1e-4, "fatol": 1e-3, "adaptive": True},
    )

    wl = wavelength_mm(target_mhz)
    elements = vector_to_elements(result.x, wl)
    final = solve_forward_back(elements, conductor_diameter_mm, target_mhz)

    print(f"=== {label}: single-frequency optimization result ===")
    print(f"Converged: {result.success}, iterations: {result.nit}, evaluations: {result.nfev}")
    print(f"Forward gain: {final.forward_gain_dbi:.2f} dBi, F/B: {final.front_to_back_db:.2f} dB")
    print(f"Impedance: {final.resistance_ohm:+.2f} {final.reactance_ohm:+.2f}j ohm, VSWR: {final.vswr_50:.2f}")
    for element in elements:
        print(f"  {element.name:12s} position={element.position_mm:7.2f} mm  length={element.length_mm:7.2f} mm")
    print()

    return list(result.x)


def optimize_bandwidth(
    design_mhz: float,
    checkpoints_mhz: list[float],
    conductor_diameter_mm: float,
    label: str,
    x0: list[float],
) -> list[float]:
    bounds = build_bounds()
    design_wavelength_mm = wavelength_mm(design_mhz)

    result = minimize(
        objective_bandwidth,
        x0,
        args=(design_wavelength_mm, checkpoints_mhz, conductor_diameter_mm),
        method="Nelder-Mead",
        bounds=bounds,
        options={"maxiter": 3000, "xatol": 1e-4, "fatol": 1e-3, "adaptive": True},
    )

    print(f"=== {label}: bandwidth-aware optimization result ===")
    print(f"Converged: {result.success}, iterations: {result.nit}, evaluations: {result.nfev}")
    elements = vector_to_elements(result.x, design_wavelength_mm)
    for element in elements:
        print(f"  {element.name:12s} position={element.position_mm:7.2f} mm  length={element.length_mm:7.2f} mm")
    for freq_mhz in checkpoints_mhz:
        r = solve_forward_back(elements, conductor_diameter_mm, freq_mhz)
        print(
            f"  {freq_mhz:>7.1f} MHz  Z={r.resistance_ohm:+7.2f}{r.reactance_ohm:+7.2f}j ohm  "
            f"VSWR={r.vswr_50:6.2f}  gain={r.forward_gain_dbi:6.2f} dBi"
        )
    print()

    return list(result.x)


def main() -> None:
    x0_900 = optimize(900.0, conductor_diameter_mm=6.0, label="Y900_5EL_OPT")
    x0_1800 = optimize(1800.0, conductor_diameter_mm=4.0, label="Y1800_5EL_OPT")

    optimize_bandwidth(
        900.0, [900.0, 925.0, 945.0, 960.0], conductor_diameter_mm=6.0,
        label="Y900_5EL_OPT_BW", x0=x0_900,
    )
    optimize_bandwidth(
        1800.0, [1710.0, 1800.0, 1840.0, 1880.0], conductor_diameter_mm=4.0,
        label="Y1800_5EL_OPT_BW", x0=x0_1800,
    )


if __name__ == "__main__":
    main()
