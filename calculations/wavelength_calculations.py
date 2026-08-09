"""Calculate free-space wavelengths for project target frequencies."""

from __future__ import annotations

from dataclasses import dataclass

SPEED_OF_LIGHT_M_PER_S = 299_792_458
TARGET_FREQUENCIES_MHZ = (700, 800, 850, 900, 1800, 2100, 2200)


@dataclass(frozen=True)
class WavelengthResult:
    """Wavelength values for one frequency."""

    frequency_mhz: float
    wavelength_m: float
    half_wavelength_m: float
    quarter_wavelength_m: float

    @property
    def wavelength_cm(self) -> float:
        return self.wavelength_m * 100

    @property
    def half_wavelength_cm(self) -> float:
        return self.half_wavelength_m * 100

    @property
    def quarter_wavelength_cm(self) -> float:
        return self.quarter_wavelength_m * 100

    @property
    def wavelength_mm(self) -> float:
        return self.wavelength_m * 1000

    @property
    def half_wavelength_mm(self) -> float:
        return self.half_wavelength_m * 1000

    @property
    def quarter_wavelength_mm(self) -> float:
        return self.quarter_wavelength_m * 1000


def calculate_wavelength(frequency_mhz: float) -> WavelengthResult:
    """Return free-space wavelength values for a frequency in MHz."""

    if frequency_mhz <= 0:
        raise ValueError("frequency_mhz must be positive")

    frequency_hz = frequency_mhz * 1_000_000
    wavelength_m = SPEED_OF_LIGHT_M_PER_S / frequency_hz
    return WavelengthResult(
        frequency_mhz=frequency_mhz,
        wavelength_m=wavelength_m,
        half_wavelength_m=wavelength_m / 2,
        quarter_wavelength_m=wavelength_m / 4,
    )


def format_row(result: WavelengthResult) -> str:
    """Format one result row for terminal output."""

    return (
        f"{result.frequency_mhz:>8.0f} | "
        f"{result.wavelength_m:>9.4f} m | "
        f"{result.wavelength_cm:>8.2f} cm | "
        f"{result.wavelength_mm:>8.1f} mm | "
        f"{result.half_wavelength_cm:>8.2f} cm | "
        f"{result.quarter_wavelength_cm:>8.2f} cm"
    )


def main() -> None:
    """Print wavelength table for project target frequencies."""

    print("Freq MHz | Wavelength |      cm |       mm |  half cm | quarter cm")
    print("-" * 75)
    for frequency_mhz in TARGET_FREQUENCIES_MHZ:
        print(format_row(calculate_wavelength(frequency_mhz)))


if __name__ == "__main__":
    main()

