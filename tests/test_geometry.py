from math import pi
from typing import Union

import pytest

from area_test_assignment import circle_area


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
    assert circle_area(value) == expected


def test_circle_area_negative():
    """Test the circle_area function with a negative radius."""
    with pytest.raises(ValueError):
        circle_area(-1)
