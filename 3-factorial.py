#!/usr/bin/env python3
"""This module defines factorial function"""

def factorial(n: int) -> int:
    if n < 0:
        return -1
    if n == 1:
        return 1
    return n * factorial(n - 1)
