"""
classifier.py

Determines the type of polynomial based on
the number of terms.
"""

from sympy import Poly
from constants import x

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
    10: "Decanomial"
}


def classify(expr):
    """
    Returns:
        (type_name, degree)
    """

    try:
        poly = Poly(expr, x)

        terms = len(poly.terms())
        degree = poly.degree()

        if terms in POLY_NAMES:
            poly_type = POLY_NAMES[terms]
        elif terms > 10:
            poly_type = f"Polynomial ({terms} terms)"
        else:
            poly_type = "Unknown"

        return poly_type, degree

    except Exception:
        return "Not a Polynomial", None


def term_count(expr):
    """
    Returns the number of terms.
    """

    try:
        poly = Poly(expr, x)
        return len(poly.terms())
    except Exception:
        return 0


def degree(expr):
    """
    Returns the polynomial degree.
    """

    try:
        poly = Poly(expr, x)
        return poly.degree()
    except Exception:
        return None


def leading_coefficient(expr):
    """
    Returns the leading coefficient.
    """

    try:
        poly = Poly(expr, x)
        return poly.LC()
    except Exception:
        return None


def constant_term(expr):
    """
    Returns the constant term.
    """

    try:
        poly = Poly(expr, x)
        return poly.TC()
    except Exception:
        return None
