"""
parser.py

Parses user input and dispatches commands.
"""

from sympy import sympify

from constants import SAFE_NAMESPACE
from algebra import (
    simplify_expr,
    expand_expr,
    factor_expr,
    collect_expr,
    solve_equation,
    evaluate,
    numeric,
    find_rationals,
)

from classifier import classify


def preprocess(expr):
    """
    Makes user-friendly syntax compatible with SymPy.
    """

    expr = expr.replace("^", "**")
    expr = expr.replace(" ", "")

    # Implicit multiplication:
    # 2x -> 2*x
    expr = expr.replace(")(", ")*(")

    import re

    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)
    expr = re.sub(r"(\d)\(", r"\1*(", expr)
    expr = re.sub(r"\)([a-zA-Z])", r")*\1", expr)

    return expr


def parse(command):

    command = command.strip()

    # -----------------------------
    # fr(a,b) n
    # -----------------------------

    if command.startswith("fr("):

        import re

        m = re.match(r"fr\((.*?),(.*?)\)\s+(\d+)", command)

        if not m:
            raise ValueError("Invalid fr() syntax.")

        left = float(m.group(1))
        right = float(m.group(2))
        amount = int(m.group(3))

        return find_rationals(left, right, amount)

    # -----------------------------
    # Commands
    # -----------------------------

    if command.startswith("expand("):

        expr = preprocess(command[7:-1])
        return expand_expr(sympify(expr, locals=SAFE_NAMESPACE))

    if command.startswith("factor("):

        expr = preprocess(command[7:-1])
        return factor_expr(sympify(expr, locals=SAFE_NAMESPACE))

    if command.startswith("simplify("):

        expr = preprocess(command[9:-1])
        return simplify_expr(sympify(expr, locals=SAFE_NAMESPACE))

    if command.startswith("collect("):

        expr = preprocess(command[8:-1])
        return collect_expr(sympify(expr, locals=SAFE_NAMESPACE))

    if command.startswith("type("):

        expr = preprocess(command[5:-1])
        return classify(sympify(expr, locals=SAFE_NAMESPACE))

    # -----------------------------
    # Equation
    # -----------------------------

    if "=" in command:

        left, right = command.split("=")

        left = sympify(preprocess(left), locals=SAFE_NAMESPACE)
        right = sympify(preprocess(right), locals=SAFE_NAMESPACE)

        return solve_equation(left, right)

    # -----------------------------
    # Basic arithmetic / expressions
    # -----------------------------

    expr = sympify(preprocess(command), locals=SAFE_NAMESPACE)

    return numeric(expr)
