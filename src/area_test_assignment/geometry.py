from math import pi
from typing import Union


def circle_area(radius: Union[int, float]) -> float:
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * radius**2
