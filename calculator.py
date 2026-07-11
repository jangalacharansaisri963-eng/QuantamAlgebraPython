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


def handle_output(output):
    """
    Handles different types of parser results.
    """

    # Polynomial classification
    if (
        isinstance(output, tuple)
        and len(output) == 2
        and isinstance(output[0], str)
        and isinstance(output[1], (int, type(None)))
    ):
        polynomial_info(output[0], output[1])
        return

    # Rational numbers list
    if (
        isinstance(output, list)
        and output
        and isinstance(output[0], Fraction)
    ):
        rationals(output)
        return

    # Equation solutions
    if isinstance(output, list):
        equation_solution(None, output)
        return

    # Normal calculation result
    result(output)


def main():

    banner()

    while True:

        try:
            command = input("\ncalc:~$ ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

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
            handle_output(output)

        except Exception as ex:
            error(ex)


if __name__ == "__main__":
    main()
