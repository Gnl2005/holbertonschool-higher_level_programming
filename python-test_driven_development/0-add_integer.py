#!/usr/bin/python3
"""
This is the "add_integer" module.
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN yoxlaması
    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")
    
    # Infinity yoxlaması
    if a in (float('inf'), float('-inf')) or b in (float('inf'), float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
