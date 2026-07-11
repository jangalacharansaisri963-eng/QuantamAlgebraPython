"""
constants.py

Shared mathematical constants and helper functions
for Quantum Algebra Calculator.
"""

from sympy import symbols, pi, sqrt

# =====================================================
# VARIABLES
# =====================================================

(
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p, q, r, s, t,
    u, v, w, x, y, z
) = symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z", real=True)

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

    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z
}

# =====================================================
# NEWTON-RAPHSON SETTINGS
# =====================================================

NEWTON_MAX_ITERATIONS = 100

NEWTON_TOLERANCE = 1e-12

NEWTON_INITIAL_GUESS = 1.0
