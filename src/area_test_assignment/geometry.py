from math import pi, sqrt
from typing import Union

Number = Union[int, float]


def circle_area(radius: Number) -> float:
    """Calculate the area of a circle given its radius.

    Args:
        radius (int | float): The radius of the circle.
    Returns:
        float: The area of the circle.
    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * radius**2


def triangle_area(side_a: Number, side_b: Number, side_c: Number) -> float:
    """
    Calculate the area of a triangle given its three sides
    using Heron's formula.
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Sides must be positive")
    semiperimeter = (side_a + side_b + side_c) / 2
    return sqrt(
        (
            semiperimeter
            * (semiperimeter - side_a)
            * (semiperimeter - side_b)
            * (semiperimeter - side_c)
        )
    )
