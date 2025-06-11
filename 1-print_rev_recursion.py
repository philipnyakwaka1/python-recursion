#!/usr/bin/env python3
"""This module defines print_rev_recursion function"""

def _print_rev_recursion(s: str, i: int = 0):
    """
    print a string in reverse, followed by a new line
    """
    if len(s) == i:
        return
    _print_rev_recursion(s, i + 1)
    print(s[i], end='')

_print_rev_recursion("\nColton Walker")