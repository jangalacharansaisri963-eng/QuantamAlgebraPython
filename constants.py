"""
constants.py

Shared mathematical constants and helper functions
for Quantum Algebra Calculator.
"""

from sympy import Symbol, pi, sqrt

# =====================================================
# PRIMARY VARIABLE
# =====================================================

# Default variable used for solving equations.
x = Symbol("x", real=True)

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
# NAMESPACES
# =====================================================

# Everything that the parser is allowed to evaluate.
SAFE_NAMESPACE = {
    **CONSTANTS,
    **FUNCTIONS,
    "x": x
}

# =====================================================
# NEWTON-RAPHSON SETTINGS
# =====================================================

NEWTON_MAX_ITERATIONS = 100

NEWTON_TOLERANCE = 1e-12

NEWTON_INITIAL_GUESS = 1.0
