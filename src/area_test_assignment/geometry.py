from abc import ABC, abstractmethod
from math import pi, sqrt
from typing import Union

Number = Union[int, float]


class Shape(ABC):
    """Base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass


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

    def is_right_triangle(self) -> bool:
        """
        Check if the triangle is a right triangle.

        Returns:
            bool: True if the triangle is a right triangle, False otherwise.
        """
        cathetes_a, cathetes_b, hypotenuse = sorted(
            [
                self.side_a,
                self.side_b,
                self.side_c,
            ]
        )
        return hypotenuse**2 == cathetes_a**2 + cathetes_b**2
