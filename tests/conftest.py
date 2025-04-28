import pytest

from area_test_assignment.geometry import Circle, Shape, Triangle


@pytest.fixture
def shapes() -> list[Shape]:
    """Fixture to create a list of shapes."""
    return (Circle(1), Triangle(7, 24, 25))
