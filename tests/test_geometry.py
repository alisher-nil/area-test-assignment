from math import pi

import pytest

from area_test_assignment import circle_area


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (1, pi),
        (2, 4 * pi),
        (3, 9 * pi),
        (4, 16 * pi),
    ],
)
def test_circle_area(value, expected):
    """Test the circle_area function."""
    assert circle_area(value) == expected


def test_circle_area_negative():
    """Test the circle_area function with a negative radius."""
    with pytest.raises(ValueError):
        circle_area(-1)
