"""Preliminary antenna geometry seeds for Cuba RF Lab.

These values are starting points for simulation only. They are not optimized,
not matched, not field validated, and not fabrication-ready blueprints.
"""

from __future__ import annotations

from dataclasses import dataclass


SPEED_OF_LIGHT_M_PER_S = 299_792_458


@dataclass(frozen=True)
class WireElement:
    name: str
    position_mm: float
    length_mm: float


@dataclass(frozen=True)
class CandidateGeometry:
    candidate_id: str
    target_mhz: float
    notes: str
    elements: tuple[WireElement, ...]

    @property
    def longest_element_mm(self) -> float:
        return max(element.length_mm for element in self.elements)

    @property
    def boom_length_mm(self) -> float:
        return max(element.position_mm for element in self.elements)


def wavelength_mm(frequency_mhz: float) -> float:
    """Return free-space wavelength in millimeters."""

    return SPEED_OF_LIGHT_M_PER_S / (frequency_mhz * 1_000_000) * 1_000


def make_yagi(
    candidate_id: str,
    target_mhz: float,
    length_factors: tuple[float, ...],
    position_factors: tuple[float, ...],
    notes: str,
) -> CandidateGeometry:
    """Create a simple Yagi seed from wavelength-scaled factors."""

    if len(length_factors) != len(position_factors):
        raise ValueError("length and position factors must have the same length")

    names = ["reflector", "driven"] + [
        f"director_{index}" for index in range(1, len(length_factors) - 1)
    ]
    wavelength = wavelength_mm(target_mhz)
    elements = tuple(
        WireElement(name=name, position_mm=pos * wavelength, length_mm=length * wavelength)
        for name, length, pos in zip(names, length_factors, position_factors)
    )
    return CandidateGeometry(candidate_id, target_mhz, notes, elements)


def make_lpda(
    candidate_id: str,
    low_mhz: float,
    tau: float,
    sigma: float,
    element_count: int,
) -> CandidateGeometry:
    """Create an LPDA seed using tau-scaled resonant element frequencies."""

    position_mm = 0.0
    elements: list[WireElement] = []

    for index in range(element_count):
        element_mhz = low_mhz / (tau**index)
        full_length_mm = 0.475 * wavelength_mm(element_mhz)
        elements.append(
            WireElement(
                name=f"element_{index + 1}_{element_mhz:.0f}mhz",
                position_mm=position_mm,
                length_mm=full_length_mm,
            )
        )
        position_mm += sigma * full_length_mm

    return CandidateGeometry(
        candidate_id=candidate_id,
        target_mhz=low_mhz,
        notes=f"LPDA seed, tau={tau}, sigma={sigma}, {element_count} elements",
        elements=tuple(elements),
    )


def make_biquad(candidate_id: str, target_mhz: float) -> CandidateGeometry:
    """Create a simple biquad seed represented by its key dimensions."""

    wavelength = wavelength_mm(target_mhz)
    side_mm = wavelength / 4
    return CandidateGeometry(
        candidate_id=candidate_id,
        target_mhz=target_mhz,
        notes="Biquad seed dimensions; use full wire geometry in EM model",
        elements=(
            WireElement("square_side", 0.0, side_mm),
            WireElement("reflector_spacing", 0.0, wavelength / 8),
            WireElement("minimum_reflector_width", 0.0, wavelength / 2),
        ),
    )


def build_candidates() -> tuple[CandidateGeometry, ...]:
    yagi_5_lengths = (0.52, 0.49, 0.465, 0.455, 0.445)
    yagi_5_positions = (0.0, 0.20, 0.40, 0.60, 0.80)
    yagi_7_lengths = (0.52, 0.49, 0.465, 0.455, 0.445, 0.435, 0.425)
    yagi_7_positions = (0.0, 0.18, 0.34, 0.50, 0.67, 0.86, 1.05)

    return (
        make_yagi(
            "Y900_5EL_SEED",
            900,
            yagi_5_lengths,
            yagi_5_positions,
            "Compact 900 MHz class Yagi seed",
        ),
        make_yagi(
            "Y900_7EL_SEED",
            900,
            yagi_7_lengths,
            yagi_7_positions,
            "Higher-gain 900 MHz class Yagi seed",
        ),
        make_yagi(
            "Y1800_5EL_SEED",
            1800,
            yagi_5_lengths,
            yagi_5_positions,
            "Compact 1800 MHz class Yagi seed",
        ),
        make_yagi(
            "Y1800_7EL_SEED",
            1800,
            yagi_7_lengths,
            yagi_7_positions,
            "Higher-gain 1800 MHz class Yagi seed",
        ),
        make_lpda("LPDA_800_2200_SEED", 800, tau=0.86, sigma=0.16, element_count=9),
        make_biquad("BIQUAD_1800_SEED", 1800),
        make_biquad("BIQUAD_2100_SEED", 2100),
    )


def build_optimized_candidates() -> tuple[CandidateGeometry, ...]:
    """Yagi geometries found by `simulations/nec/optimize_yagi_directors.py`.

    Unlike `build_candidates()`, these dimensions were not derived from a
    formula. They are the output of a local NEC-driven numerical search
    (SciPy Nelder-Mead, `necpp` as the objective function) that started
    from a reasonable textbook-ratio guess and searched for a geometry
    the solver confirms actually works, after the uniform wavelength-scaled
    `*_5EL_SEED`/`*_7EL_SEED` candidates above failed NEC simulation. See
    `simulations/results/y900_5el_opt_v1_first_pass.md` and
    `simulations/results/y1800_5el_opt_v1_first_pass.md` for full
    characterization. Reflector length/position matches the original seed
    (0.500 wavelength, position 0); only the driven element and three
    directors were searched.
    """

    return (
        CandidateGeometry(
            candidate_id="Y900_5EL_OPT_V1",
            target_mhz=900,
            notes="NEC-optimized (local search) 900 MHz class 5-element Yagi",
            elements=(
                WireElement("reflector", 0.00, 166.55),
                WireElement("driven", 51.24, 163.39),
                WireElement("director_1", 104.15, 146.20),
                WireElement("director_2", 143.78, 135.88),
                WireElement("director_3", 177.66, 136.43),
            ),
        ),
        CandidateGeometry(
            candidate_id="Y1800_5EL_OPT_V1",
            target_mhz=1800,
            notes="NEC-optimized (local search) 1800 MHz class 5-element Yagi",
            elements=(
                WireElement("reflector", 0.00, 83.28),
                WireElement("driven", 25.88, 83.05),
                WireElement("director_1", 50.60, 72.41),
                WireElement("director_2", 70.26, 69.86),
                WireElement("director_3", 88.01, 66.08),
            ),
        ),
        CandidateGeometry(
            candidate_id="Y900_5EL_OPT_V2_BW",
            target_mhz=900,
            notes=(
                "NEC-optimized (bandwidth-aware local search, worst-case gain across "
                "900/925/945/960 MHz) 900 MHz class 5-element Yagi. Supersedes "
                "Y900_5EL_OPT_V1 for band coverage; needs a matching network (native "
                "VSWR 20-33 against 50 ohm)."
            ),
            elements=(
                WireElement("reflector", 0.00, 166.55),
                WireElement("driven", 38.17, 166.55),
                WireElement("director_1", 93.20, 133.98),
                WireElement("director_2", 177.70, 131.20),
                WireElement("director_3", 277.63, 132.31),
            ),
        ),
        CandidateGeometry(
            candidate_id="Y1800_5EL_OPT_V2_BW",
            target_mhz=1800,
            notes=(
                "NEC-optimized (bandwidth-aware local search, worst-case gain across "
                "1710/1800/1840/1880 MHz) 1800 MHz class 5-element Yagi. Supersedes "
                "Y1800_5EL_OPT_V1 for band coverage; native VSWR 2.8-5.9 against 50 "
                "ohm, close enough that a simple matching network should suffice."
            ),
            elements=(
                WireElement("reflector", 0.00, 83.28),
                WireElement("driven", 14.22, 82.41),
                WireElement("director_1", 63.68, 65.26),
                WireElement("director_2", 108.64, 63.60),
                WireElement("director_3", 157.30, 64.62),
            ),
        ),
    )


def print_summary(candidates: tuple[CandidateGeometry, ...]) -> None:
    print("| Candidate | Target MHz | Elements | Longest element mm | Boom / width mm | Notes |")
    print("| --- | ---: | ---: | ---: | ---: | --- |")
    for candidate in candidates:
        print(
            "| "
            f"{candidate.candidate_id} | "
            f"{candidate.target_mhz:.0f} | "
            f"{len(candidate.elements)} | "
            f"{candidate.longest_element_mm:.1f} | "
            f"{candidate.boom_length_mm:.1f} | "
            f"{candidate.notes} |"
        )


def print_elements(candidates: tuple[CandidateGeometry, ...]) -> None:
    for candidate in candidates:
        print()
        print(f"## {candidate.candidate_id}")
        print()
        print("| Element | Position mm | Length or key dimension mm |")
        print("| --- | ---: | ---: |")
        for element in candidate.elements:
            print(f"| {element.name} | {element.position_mm:.1f} | {element.length_mm:.1f} |")


def main() -> None:
    candidates = build_candidates()
    print_summary(candidates)
    print_elements(candidates)


if __name__ == "__main__":
    main()
