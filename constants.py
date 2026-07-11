"""
constants.py

Shared mathematical constants and helper functions
for Quantum Algebra Calculator.
"""

from sympy import symbols, pi, sqrt


# =====================================================
# VARIABLES (a-z)
# =====================================================

(
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p, q, r, s, t,
    u, v, w, x, y, z
) = symbols(
    "a b c d e f g h i j k l m n o p q r s t u v w x y z",
    real=True
)


# All polynomial variables
VARIABLES = (
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p, q, r, s, t,
    u, v, w, x, y, z
)


# =====================================================
# CONSTANTS
# =====================================================

CONSTANTS = {
    "pi": pi
}


# =====================================================
# FUNCTIONS
# =====================================================

FUNCTIONS = {
    "sqrt": sqrt
}


# =====================================================
# SAFE NAMESPACE
# =====================================================

SAFE_NAMESPACE = {
    **CONSTANTS,
    **FUNCTIONS,

    **{
        symbol.name: symbol
        for symbol in VARIABLES
    }
}


# =====================================================
# NEWTON-RAPHSON SETTINGS
# =====================================================

NEWTON_MAX_ITERATIONS = 100

NEWTON_TOLERANCE = 1e-12

NEWTON_INITIAL_GUESS = 1.0
