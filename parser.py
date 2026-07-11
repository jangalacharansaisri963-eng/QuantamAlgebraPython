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

    # )x
    expr = re.sub(r"\)([a-z])", r")*\1", expr)

    # x(
    expr = re.sub(r"([a-z])\(", r"\1*(", expr)

    # xy -> x*y
    expr = re.sub(r"([a-z])([a-z])", r"\1*\2", expr)

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
    # expand(...)
    # ------------------------------------------

    if command.startswith("expand("):

        expr = preprocess(command[7:-1])

        return expand_expr(
            sympify(expr, locals=SAFE_NAMESPACE)
        )

    # ------------------------------------------

    if command.startswith("factor("):

        expr = preprocess(command[7:-1])

        return factor_expr(
            sympify(expr, locals=SAFE_NAMESPACE)
        )

    # ------------------------------------------

    if command.startswith("simplify("):

        expr = preprocess(command[9:-1])

        return simplify_expr(
            sympify(expr, locals=SAFE_NAMESPACE)
        )

    # ------------------------------------------

    if command.startswith("collect("):

        expr = preprocess(command[8:-1])

        return collect_expr(
            sympify(expr, locals=SAFE_NAMESPACE)
        )

    # ------------------------------------------

    if command.startswith("type("):

        expr = preprocess(command[5:-1])

        return classify(
            sympify(expr, locals=SAFE_NAMESPACE)
        )

    # ------------------------------------------
    # EQUATION
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

        return solve_equation(left, right)

    # ------------------------------------------
    # NORMAL EXPRESSION
    # ------------------------------------------

    expr = sympify(
        preprocess(command),
        locals=SAFE_NAMESPACE
    )

    return numeric(expr)
