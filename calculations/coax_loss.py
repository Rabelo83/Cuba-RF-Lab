"""Estimate coax feedline loss for project frequencies.

The starter attenuation table intentionally contains placeholders. Replace
values with sourced manufacturer data or measured data before making design
decisions.
"""

from __future__ import annotations

from dataclasses import dataclass

TARGET_FREQUENCIES_MHZ = (900, 1800, 2100)


@dataclass(frozen=True)
class CableType:
    """Cable attenuation data in dB per 100 meters."""

    name: str
    attenuation_db_per_100m: dict[int, float | None]
    source: str


STARTER_CABLES = (
    CableType(
        name="UNKNOWN_LOCAL_COAX",
        attenuation_db_per_100m={900: None, 1800: None, 2100: None},
        source="Measure or replace with sourced data.",
    ),
    CableType(
        name="RG-58_PLACEHOLDER",
        attenuation_db_per_100m={900: None, 1800: None, 2100: None},
        source="TODO: add manufacturer data.",
    ),
    CableType(
        name="LMR-240_PLACEHOLDER",
        attenuation_db_per_100m={900: None, 1800: None, 2100: None},
        source="TODO: add manufacturer data.",
    ),
)


def calculate_loss_db(length_m: float, attenuation_db_per_100m: float) -> float:
    """Calculate coax loss for a length in meters."""

    if length_m < 0:
        raise ValueError("length_m must not be negative")
    if attenuation_db_per_100m < 0:
        raise ValueError("attenuation_db_per_100m must not be negative")
    return length_m * attenuation_db_per_100m / 100


def print_loss_table(length_m: float) -> None:
    """Print loss table for all starter cables with known values."""

    print(f"Coax loss estimate for {length_m:.2f} m")
    print("Cable | Frequency MHz | Loss dB | Source")
    print("-" * 72)
    for cable in STARTER_CABLES:
        for frequency_mhz in TARGET_FREQUENCIES_MHZ:
            attenuation = cable.attenuation_db_per_100m.get(frequency_mhz)
            if attenuation is None:
                loss = "TODO"
            else:
                loss = f"{calculate_loss_db(length_m, attenuation):.2f}"
            print(f"{cable.name} | {frequency_mhz} | {loss} | {cable.source}")


def main() -> None:
    """Run the default starter table."""

    print_loss_table(length_m=10)


if __name__ == "__main__":
    main()

