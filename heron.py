# heron.py

import math

def heron_formula(a, b, c):
    """ (number, number, number) -> float

    Precondition: a > 0 and b > 0 and c > 0

    Return the area of a triangle with sides of length a, b, c.

    >>> heron_formula(3, 4, 5)
    6.0
    >>> heron_formula(5, 5.5, 4.5)
    10.606601717798213
    """

    if a <=0 or b <= 0 or c <= 0:
        raise ValueError("The lengths must be positive numbers.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))
