# Area Test Assignment

A Python library for calculating the area of geometric shapes. This library currently supports calculating the area of circles and triangles, with the ability to easily extend support for additional shapes.

## Features

- Calculate the area of a circle given its radius.
- Calculate the area of a triangle given its three sides using Heron's formula.
- Check if a triangle is a right triangle.
- Designed for extensibility to add new shapes easily.
- Abstract base class (`Shape`) ensures a consistent interface for all shapes.

## Installation

To use this library, clone the repository and navigate to the project directory:
```bash
git clone https://github.com/alisher-nil/area-test-assignment.git
cd area-test-assignment
```
### install dependencies using pip
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
### or install using uv
```bash
uv sync
```

## Usage
### `Circle`
To calculate the area of a circle:
```python
from area_test_assignment import Circle

circle = Circle(radius=5)
print(f"Area of the circle: {circle.area()}")
```

### `Triangle`
To calculate the area of a triangle and check if it is a right triangle:
```python
from area_test_assignment import Triangle

triangle = Triangle(side_a=3, side_b=4, side_c=5)
print(f"Area of the triangle: {triangle.area()}")
print(f"Is the triangle a right triangle? {triangle.is_right_triangle()}")
```
## Extensibility
To add a new shape, simply create a new class that inherits from the `Shape` abstract base class and implement the area method. For example:
```python
from area_test_assignment import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
```
## Testing
This project uses pytest for unit testing. To run the tests, execute from the projects directory:
```bash
pytest
```
## Project Structure
```
area-test-assignment/
├── src/
│   └── area_test_assignment/
│       ├── __init__.py
│       ├── geometry.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   └── test_geometry.py
├── README.md
├── pyproject.toml
├── ruff.toml
└── .gitignore
```
## Requirements
- Python 3.13 or higher
- pytest for testing
## Author
Created by Alisher Nildibayev. For any questions, feel free to reach out at alisher.nil@gmail.com