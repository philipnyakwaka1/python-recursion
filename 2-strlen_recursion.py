#!/usr/bin/env python3
"""This module defines _strlen_recursion"""

def _strlen_recursion(s: str, i: int = 0):
    """return the length of a string recursively"""
    try:
        s[i]
        return _strlen_recursion(s, i + 1)
    except IndexError:
        return i

