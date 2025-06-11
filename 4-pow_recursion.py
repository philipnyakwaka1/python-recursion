#!/usr/bin/env python3
"""This module defines _pow_recursion function"""

def _pow_recursion(x: int, y: int) -> int:
    """
    Compute x raised to the power of y recursively.

    Args:
        x (int): The base.
        y (int): The exponent.

    Returns:
        int: x ** y if y >= 0, otherwise -1.
    """

    if y < 0:
        return -1
    if y == 0:
        return 1
    return x * _pow_recursion(x, y - 1)
