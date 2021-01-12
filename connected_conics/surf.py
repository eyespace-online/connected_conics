"""
These functions are used for converting the output of find_val, 
which is a 2D representation of a single meridian of the lens, 
into a surface.
"""

import numpy as np
import math
from scipy.interpolate import CubicSpline


def interp_sag(z1, z2, theta):
    """
    Used for toric lenses.
    """
    return z1 * np.square(np.cos(theta)) + z2 * np.square(np.sin(theta))


def interp_quad(z1, z2, z3, z4, theta):
    """
    Used for quadrant specific lenses.
    """
    X = np.linspace(0, math.pi * 2, 5)
    Y = [z1, z2, z3, z4, z1]
    f = CubicSpline(X, Y, bc_type="periodic")
    return f(theta)
