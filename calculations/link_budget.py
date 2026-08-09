"""Simple received-signal delta calculator for the Cuba RF Lab project."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LinkBudget:
    """Inputs for a simple receive-side improvement estimate."""

    baseline_phone_signal_dbm: float
    antenna_gain_dbi: float
    coax_loss_db: float
    connector_loss_db: float
    coupler_loss_db: float
    miscellaneous_loss_db: float = 0.0

    @property
    def total_loss_db(self) -> float:
        return (
            self.coax_loss_db
            + self.connector_loss_db
            + self.coupler_loss_db
            + self.miscellaneous_loss_db
        )

    @property
    def net_improvement_db(self) -> float:
        return self.antenna_gain_dbi - self.total_loss_db

    @property
    def expected_signal_dbm(self) -> float:
        return self.baseline_phone_signal_dbm + self.net_improvement_db


def calculate_budget(
    baseline_phone_signal_dbm: float,
    antenna_gain_dbi: float,
    coax_loss_db: float,
    connector_loss_db: float,
    coupler_loss_db: float,
    miscellaneous_loss_db: float = 0.0,
) -> LinkBudget:
    """Create a link budget after validating non-negative loss values."""

    losses = {
        "coax_loss_db": coax_loss_db,
        "connector_loss_db": connector_loss_db,
        "coupler_loss_db": coupler_loss_db,
        "miscellaneous_loss_db": miscellaneous_loss_db,
    }
    for name, value in losses.items():
        if value < 0:
            raise ValueError(f"{name} must not be negative")

    return LinkBudget(
        baseline_phone_signal_dbm=baseline_phone_signal_dbm,
        antenna_gain_dbi=antenna_gain_dbi,
        coax_loss_db=coax_loss_db,
        connector_loss_db=connector_loss_db,
        coupler_loss_db=coupler_loss_db,
        miscellaneous_loss_db=miscellaneous_loss_db,
    )


def main() -> None:
    """Run an example with clearly labeled placeholder values."""

    budget = calculate_budget(
        baseline_phone_signal_dbm=-110,
        antenna_gain_dbi=0,
        coax_loss_db=0,
        connector_loss_db=0,
        coupler_loss_db=0,
    )
    print("Example only. Replace all values with sourced or measured data.")
    print(f"Baseline phone signal: {budget.baseline_phone_signal_dbm:.1f} dBm")
    print(f"Antenna gain: {budget.antenna_gain_dbi:.1f} dBi")
    print(f"Total loss: {budget.total_loss_db:.1f} dB")
    print(f"Net improvement: {budget.net_improvement_db:.1f} dB")
    print(f"Expected signal: {budget.expected_signal_dbm:.1f} dBm")


if __name__ == "__main__":
    main()
