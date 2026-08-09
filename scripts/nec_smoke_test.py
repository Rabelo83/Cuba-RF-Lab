"""Smoke test for the project NEC2 solver.

This script verifies that the local Python `necpp` install can run a basic
antenna model. It is not a project antenna design.
"""

from __future__ import annotations

import necpp


def check(result: int) -> None:
    """Raise with the NEC error message if a call fails."""

    if result != 0:
        raise RuntimeError(necpp.nec_error_message())


def run_smoke_test() -> tuple[complex, float]:
    """Run a simple 900 MHz dipole model and return impedance and gain."""

    nec = necpp.nec_create()
    try:
        # Half-wave dipole centered at the origin, oriented on the Z axis.
        radius_m = 0.0015
        half_length_m = 0.083

        check(
            necpp.nec_wire(
                nec,
                1,
                21,
                0,
                0,
                -half_length_m,
                0,
                0,
                half_length_m,
                radius_m,
                1,
                1,
            )
        )
        check(necpp.nec_geometry_complete(nec, 0))
        check(necpp.nec_gn_card(nec, -1, 0, 0, 0, 0, 0, 0, 0))
        check(necpp.nec_fr_card(nec, 0, 1, 900.0, 0))
        check(necpp.nec_ex_card(nec, 0, 1, 11, 0, 1.0, 0, 0, 0, 0, 0))
        check(necpp.nec_rp_card(nec, 0, 19, 37, 0, 5, 0, 0, 0, 0, 5, 10, 0, 0))

        impedance = complex(necpp.nec_impedance_real(nec, 0), necpp.nec_impedance_imag(nec, 0))
        broadside_gain_dbi = necpp.nec_gain(nec, 0, 18, 0)
        return impedance, broadside_gain_dbi
    finally:
        necpp.nec_delete(nec)


def main() -> None:
    impedance, gain_dbi = run_smoke_test()
    print("NEC solver smoke test passed.")
    print(f"900 MHz dipole impedance: {impedance.real:.2f} {impedance.imag:+.2f}j ohms")
    print(f"Broadside gain sample: {gain_dbi:.2f} dBi")


if __name__ == "__main__":
    main()
