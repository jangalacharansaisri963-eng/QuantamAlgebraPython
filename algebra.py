"""
algebra.py

Core algebra engine.
"""

from fractions import Fraction
from sympy import (
    Eq,
    Poly,
    expand,
    factor,
    simplify,
    collect,
    solve,
    diff,
    integrate,
    sympify,
    N,
)

from constants import (
    SAFE_NAMESPACE,
    NEWTON_MAX_ITERATIONS,
    NEWTON_TOLERANCE,
    NEWTON_INITIAL_GUESS,
)


# ==========================================================
# VARIABLE DETECTION
# ==========================================================

def get_variable(expr):
    """
    Returns the first variable found alphabetically.
    Defaults to x if no variable exists.
    """
    symbols = sorted(expr.free_symbols, key=lambda s: s.name)

    if symbols:
        return symbols[0]

    return SAFE_NAMESPACE["x"]


# ==========================================================
# BASIC OPERATIONS
# ==========================================================

def simplify_expr(expr):
    return simplify(expr)


def expand_expr(expr):
    return expand(expr)


def factor_expr(expr):
    return factor(expr)


def collect_expr(expr):
    return collect(expr, get_variable(expr))


def derivative(expr):
    return diff(expr, get_variable(expr))


def integral(expr):
    return integrate(expr, get_variable(expr))


# ==========================================================
# EQUATION SOLVER
# ==========================================================

def solve_equation(left, right=0):

    equation = Eq(left, right)

    variable = get_variable(left - right)

    try:
        ans = solve(equation, variable)

        if ans:
            return variable, ans

    except Exception:
        pass

    return variable, [newton_raphson(left - right, variable)]


# ==========================================================
# NEWTON-RAPHSON
# ==========================================================

def newton_raphson(expr, variable):

    f = sympify(expr)
    fp = diff(f, variable)

    guess = float(NEWTON_INITIAL_GUESS)

    for _ in range(NEWTON_MAX_ITERATIONS):

        fx = float(f.subs(variable, guess))
        dfx = float(fp.subs(variable, guess))

        if abs(dfx) < 1e-15:
            break

        next_guess = guess - fx / dfx

        if abs(next_guess - guess) < NEWTON_TOLERANCE:
            return N(next_guess)

        guess = next_guess

    return N(guess)


# ==========================================================
# POLYNOMIAL INFO
# ==========================================================

def degree(expr):
    return Poly(expr, get_variable(expr)).degree()


def leading_coefficient(expr):
    return Poly(expr, get_variable(expr)).LC()


def constant_term(expr):
    return Poly(expr, get_variable(expr)).TC()


# ==========================================================
# FIND RATIONALS
# ==========================================================

def find_rationals(a, b, amount):

    a = Fraction(str(a))
    b = Fraction(str(b))

    if a > b:
        a, b = b, a

    found = []

    denominator = 1

    while len(found) < amount:

        start = int(a * denominator) + 1
        end = int(b * denominator)

        for numerator in range(start, end + 1):

            frac = Fraction(numerator, denominator)

            if a < frac < b and frac not in found:
                found.append(frac)

                if len(found) >= amount:
                    break

        denominator += 1

    found.sort()

    return found


# ==========================================================
# EVALUATE
# ==========================================================

def evaluate(expr, value):

    variable = get_variable(expr)

    return expr.subs(variable, value)


# ==========================================================
# NUMERIC VALUE
# ==========================================================

def numeric(expr):
    return N(expr)
