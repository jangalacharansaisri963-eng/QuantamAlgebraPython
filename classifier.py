"""
classifier.py

Determines the type of polynomial based on
the number of terms and supports variables a-z.
"""

from sympy import Poly
from constants import VARIABLES


# Polynomial names
POLY_NAMES = {
    0: "Zero Polynomial",
    1: "Monomial",
    2: "Binomial",
    3: "Trinomial",
    4: "Quadrinomial",
    5: "Pentanomial",
    6: "Hexanomial",
    7: "Heptanomial",
    8: "Octanomial",
    9: "Nonanomial",
    10: "Decanomial",
}


def make_poly(expr):
    """
    Creates a polynomial using variables a-z.
    """
    return Poly(expr, *VARIABLES)


def classify(expr):
    """
    Returns:
        (polynomial type, degree)
    """

    try:
        poly = make_poly(expr)

        terms = len(poly.terms())
        degree = poly.total_degree()

        if terms in POLY_NAMES:
            poly_type = POLY_NAMES[terms]
        else:
            poly_type = f"Polynomial ({terms} terms)"

        return poly_type, degree

    except Exception:
        return "Not a Polynomial", None


def term_count(expr):
    """
    Returns number of terms.
    """
    try:
        return len(make_poly(expr).terms())
    except Exception:
        return 0


def degree(expr):
    """
    Returns polynomial degree.
    """
    try:
        return make_poly(expr).total_degree()
    except Exception:
        return None


def leading_coefficient(expr):
    """
    Returns leading coefficient.
    """
    try:
        return make_poly(expr).LC()
    except Exception:
        return None


def constant_term(expr):
    """
    Returns constant term.
    """
    try:
        return make_poly(expr).TC()
    except Exception:
        return None
