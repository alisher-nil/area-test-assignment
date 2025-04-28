from math import pi, sqrt
from typing import Protocol, Union

Number = Union[int, float]


class Shape(Protocol):
    """Base class for shapes."""

    def area(self) -> float:
        """Calculate the area of the shape."""
        ...


class Circle(Shape):
    """
    Circle shape.

    Args:
        radius (int | float): The radius of the circle.
    Raises:
        ValueError: If the radius is negative.
    """

    def __init__(self, radius: Number) -> None:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of a circle given its radius.

        Returns:
            float: The area of the circle.
        """
        return pi * self.radius**2


class Triangle(Shape):
    """
    Triangle shape.

    Args:
        side_a (int | float): The length of the first side.
        side_b (int | float): The length of the second side.
        side_c (int | float): The length of the third side.
    Raises:
        ValueError: If any of the sides are non-positive.
        ValueError: If the sides do not satisfy the triangle inequality.
    """

    def __init__(self, side_a: Number, side_b: Number, side_c: Number) -> None:
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be positive")

        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("Invalid triangle sides")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """
        Calculate the area of a triangle given its three sides
        using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        semiperimeter = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(
            (
                semiperimeter
                * (semiperimeter - self.side_a)
                * (semiperimeter - self.side_b)
                * (semiperimeter - self.side_c)
            )
        )


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
    Args:
        side_a (int | float): The length of the first side.
        side_b (int | float): The length of the second side.
        side_c (int | float): The length of the third side.
    Returns:
        float: The area of the triangle.
    Raises:
        ValueError: If any of the sides are non-positive.
        ValueError: If the sides do not satisfy the triangle inequality.
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
