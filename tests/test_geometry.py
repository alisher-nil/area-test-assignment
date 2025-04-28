from math import pi, sqrt
from typing import Union

import pytest

from area_test_assignment import Circle, Shape, Triangle

Number = Union[int, float]


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),  # testing zero radius
        (1, pi),  # testing integer radius
        (2, 4 * pi),  # testing integer radius
        (3, 9 * pi),  # testing integer radius
        (pi, pi**3),  # testing float value
    ],
)
def test_circle_area(value: Union[int, float], expected: float):
    """Test the circle_area function."""
    assert Circle(value).area() == expected


def test_circle_area_negative():
    """Test the circle_area function with a negative radius."""
    with pytest.raises(ValueError):
        Circle(-1)


@pytest.mark.parametrize(
    "side_a, side_b, side_c, expected",
    [
        (3, 4, 5, 6),  # testing integer sides
        (3.0, 4.0, 5.0, 6.0),  # testing float sides
        (1, 1, 1, sqrt(3) / 4),  # testing equilateral triangle
    ],
)
def test_triangle_area(
    side_a: Number,
    side_b: Number,
    side_c: Number,
    expected: float,
):
    """Test the triangle_area function."""
    assert Triangle(side_a, side_b, side_c).area() == expected


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (-1, 2, 3),  # testing negative side a
        (1, -2, 5),  # testing negative side b
        (1, 4, -5),  # testing negative side c
        (0, 0, 0),  # testing zero sides
        (1, 1, 3),  # testing invalid triangle inequality
    ],
)
def test_triangle_area_invalid_sides(
    side_a: Number,
    side_b: Number,
    side_c: Number,
):
    """Test the triangle_area function with invalid sides."""
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "shape, expected",
    [
        (Circle(1), pi),  # testing circle
        (Triangle(3, 4, 5), 6),  # testing triangle
    ],
)
def test_shape_behaviour_compatibility(shape: Shape, expected: float):
    """Test the area of a shape."""
    assert isinstance(shape, Shape)
    assert shape.area() == expected


@pytest.mark.parametrize(
    "side_a, side_b, side_c, is_right_angle",
    [
        (3, 4, 5, True),  # testing right angle triangle
        (3, 3, 3, False),  # testing non-right angle triangle
    ],
)
def test_right_angle_triangle(
    side_a: Number, side_b: Number, side_c: Number, is_right_angle: bool
):
    """Test if the triangle is a right angle triangle."""
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.is_right_triangle() == is_right_angle
