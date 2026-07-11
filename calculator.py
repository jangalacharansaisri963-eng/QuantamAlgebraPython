"""
Quantum Algebra Calculator
Main terminal application.
"""

from parser import parse
from formatter import (
    banner,
    result,
    error,
    equation_solution,
    polynomial_info,
    rationals,
    help_menu,
)

from fractions import Fraction


def main():

    banner()

    while True:

        command = input("\ncalc:~$ ").strip()

        if not command:
            continue

        lower = command.lower()

        if lower in ("exit", "quit"):
            print("Goodbye!")
            break

        if lower == "help":
            help_menu()
            continue

        if lower in ("clear", "cls"):
            import os
            os.system("cls" if os.name == "nt" else "clear")
            banner()
            continue

        try:

            output = parse(command)

            # -------------------------
            # Polynomial classification
            # -------------------------

            if (
                isinstance(output, tuple)
                and len(output) == 2
                and isinstance(output[0], str)
            ):

                polynomial_info(output[0], output[1])
                continue

            # -------------------------
            # Rational list
            # -------------------------

            if (
                isinstance(output, list)
                and len(output) > 0
                and isinstance(output[0], Fraction)
            ):

                rationals(output)
                continue

            # -------------------------
            # Equation solutions
            # -------------------------

            if isinstance(output, list):

                equation_solution("x", output)
                continue

            # -------------------------
            # Normal result
            # -------------------------

            result(output)

        except Exception as ex:
            error(ex)


if __name__ == "__main__":
    main()
