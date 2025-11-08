#!/usr/bin/python3
"""
This is the "add_integer" module.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if (
        a != a or b != b
        or a in (float('inf'), float('-inf'))
        or b in (float('inf'), float('-inf'))
    ):
        raise OverflowError("cannot convert float NaN or infinity to integer")

    return (int(a) + int(b))
