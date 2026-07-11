"""
formatter.py

Handles all terminal output formatting.
"""


LINE = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"


def title(text):
    """
    Prints a section title.
    """
    print()
    print(LINE)
    print(text)
    print(LINE)


def result(value):
    """
    Prints a normal result.
    """
    title("Result")
    print(value)
    print(LINE)


def success(message):
    """
    Prints a success message.
    """
    print(f">> {message}")


def error(message):
    """
    Prints an error message.
    """
    print(f"Error: {message}")


def equation_solution(variable, solutions):
    """
    Prints one or more equation solutions.
    """

    title("Solution")

    if isinstance(solutions, (list, tuple, set)):
        if len(solutions) == 0:
            print("No solution.")
        else:
            for s in solutions:
                print(f"{variable} = {s}")
    else:
        print(f"{variable} = {solutions}")

    print(LINE)


def polynomial_info(poly_type, degree):
    """
    Prints polynomial information.
    """

    title("Polynomial Information")

    print(f"Type   : {poly_type}")
    print(f"Degree : {degree}")

    print(LINE)


def rationals(fractions):
    """
    Prints rational numbers.
    """

    title("Rational Numbers")

    for f in fractions:
        print(f"{f} = {float(f)}")

    print(LINE)


def banner():
    """
    Startup banner.
    """

    print(LINE)
    print(" Quantum Algebra Calculator")
    print(" Version 1.0")
    print(LINE)
    print("Type 'help' for commands.")
    print("Type 'exit' to quit.")
    print(LINE)


def help_menu():

    title("Commands")

    print("expand(expression)")
    print("factor(expression)")
    print("simplify(expression)")
    print("collect(expression)")
    print("degree(expression)")
    print("type(expression)")
    print("sqrt(number)")
    print("Equation solving:")
    print("    x^2+5x+6=0")
    print("Find rationals:")
    print("    fr(3,4) 12")

    print(LINE)
