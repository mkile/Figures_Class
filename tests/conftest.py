import pytest
from source.classes import Triangle, Circle, Square, Rectangle

default_name = 'test_figure_name'


@pytest.fixture
def generic_triangle():
    figure = Triangle(default_name, [2, 4, 5])
    yield figure
    del figure


@pytest.fixture
def generic_circle():
    figure = Circle(default_name, [3])
    yield figure
    del figure


@pytest.fixture
def generic_square():
    figure = Square(default_name, [3])
    yield figure
    del figure


@pytest.fixture
def generic_rectangle():
    figure = Rectangle(default_name, [3, 5])
    yield figure
    del figure
