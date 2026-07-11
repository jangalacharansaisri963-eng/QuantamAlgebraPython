"""
parser.py

Parses user input and dispatches commands.
"""

import re
from sympy import sympify

from constants import SAFE_NAMESPACE

from algebra import (
    simplify_expr,
    expand_expr,
    factor_expr,
    collect_expr,
    solve_equation,
    numeric,
    find_rationals,
)

from classifier import classify


# ==========================================================
# PREPROCESS
# ==========================================================

def preprocess(expr):

    expr = expr.replace("^", "**")
    expr = expr.replace(" ", "")

    # (x+1)(x-1)
    expr = expr.replace(")(", ")*(")

    # 2x -> 2*x
    expr = re.sub(r"(\d)([a-z])", r"\1*\2", expr)

    # 2(x+1)
    expr = re.sub(r"(\d)\(", r"\1*(", expr)

    # )x -> )*x
    expr = re.sub(r"\)([a-z])", r")*\1", expr)

    # x( -> x*(
    expr = re.sub(r"([a-z])\(", r"\1*(", expr)

    # xy -> x*y (only single variables)
    expr = re.sub(
        r"([a-z])([a-z])",
        r"\1*\2",
        expr
    )

    return expr


# ==========================================================
# PARSER
# ==========================================================

def parse(command):

    command = command.strip()

    # ------------------------------------------
    # fr(a,b) n
    # ------------------------------------------

    fr_match = re.fullmatch(
        r"fr\((.*?),(.*?)\)\s+(\d+)",
        command
    )

    if fr_match:

        left = float(fr_match.group(1))
        right = float(fr_match.group(2))
        amount = int(fr_match.group(3))

        return find_rationals(left, right, amount)


    # ------------------------------------------
    # Functions
    # ------------------------------------------

    functions = {
        "expand(": expand_expr,
        "factor(": factor_expr,
        "simplify(": simplify_expr,
        "collect(": collect_expr,
    }


    for name, func in functions.items():

        if command.startswith(name):

            expr = preprocess(
                command[len(name):-1]
            )

            return func(
                sympify(
                    expr,
                    locals=SAFE_NAMESPACE
                )
            )


    # ------------------------------------------
    # Polynomial type
    # ------------------------------------------

    if command.startswith("type("):

        expr = preprocess(
            command[5:-1]
        )

        return classify(
            sympify(
                expr,
                locals=SAFE_NAMESPACE
            )
        )


    # ------------------------------------------
    # Equation
    # ------------------------------------------

    if "=" in command:

        left, right = command.split("=", 1)

        left = sympify(
            preprocess(left),
            locals=SAFE_NAMESPACE
        )

        right = sympify(
            preprocess(right),
            locals=SAFE_NAMESPACE
        )

        variable, solutions = solve_equation(
            left,
            right
        )

        return variable, solutions


    # ------------------------------------------
    # Normal expression
    # ------------------------------------------

    expr = sympify(
        preprocess(command),
        locals=SAFE_NAMESPACE
    )

    return numeric(expr)
