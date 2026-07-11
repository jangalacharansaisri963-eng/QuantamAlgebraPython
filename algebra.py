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
    sqrt,
    pi,
    sympify,
    N,
)

from constants import (
    x,
    NEWTON_MAX_ITERATIONS,
    NEWTON_TOLERANCE,
    NEWTON_INITIAL_GUESS,
)


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
    return collect(expr, x)


def derivative(expr):
    return diff(expr, x)


def integral(expr):
    return integrate(expr, x)


# ==========================================================
# EQUATION SOLVER
# ==========================================================

def solve_equation(left, right=0):

    equation = Eq(left, right)

    try:
        ans = solve(equation, x)

        if ans:
            return ans

    except Exception:
        pass

    return [newton_raphson(left - right)]


# ==========================================================
# NEWTON-RAPHSON
# ==========================================================

def newton_raphson(expr):

    f = sympify(expr)
    fp = diff(f, x)

    guess = float(NEWTON_INITIAL_GUESS)

    for _ in range(NEWTON_MAX_ITERATIONS):

        fx = float(f.subs(x, guess))
        dfx = float(fp.subs(x, guess))

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
    return Poly(expr, x).degree()


def leading_coefficient(expr):
    return Poly(expr, x).LC()


def constant_term(expr):
    return Poly(expr, x).TC()


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

            if frac > a and frac < b:

                if frac not in found:

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

    return expr.subs(x, value)


# ==========================================================
# NUMERIC VALUE
# ==========================================================

def numeric(expr):

    return N(expr)
