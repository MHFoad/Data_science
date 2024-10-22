# Enter you module contents here
"""
Module: triangle

This module provides functions for calculating properties of right-angled triangles.
"""
import math

__version__ = "1.0"
__author__ = "Mohammad Foad"

def hypotenuse(side1, side2):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.

    Parameters:
    side1 (float): Length of one of the other sides.
    side2 (float): Length of the other side.

    Returns:
    float: Length of the hypotenuse.
    """
    return math.sqrt(side1**2 + side2**2)

def area(base, height):
    """
    Calculate the area of a right-angled triangle.

    Parameters:
    base (float): Length of the base (perpendicular to the height).
    height (float): Length of the height (perpendicular to the base).

    Returns:
    float: Area of the right-angled triangle.
    """
    return 0.5 * base * height