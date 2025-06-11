#!/usr/bin/env python3
"""This module defines _puts_recursion(s)"""

def _puts_recursion(s: str, i: int = 0) -> None:
    """
    Print a string recursively, followed by a new line:
    Args:
        s: string to be printed
    """
    if i == len(s):
        print()
        return
    print(s[i], end='')
    i += 1
    _puts_recursion(s, i)

