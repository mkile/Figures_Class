import pytest
from source.classes import Rectangle


def test_creation():
    assert Rectangle('rectangle', [2, 4])


def test_check_name(generic_rectangle):
    assert generic_rectangle.name == 'test_figure_name'


def test_check_area(generic_rectangle):
    assert generic_rectangle.area() == 15


def test_check_perimeter(generic_rectangle):
    assert generic_rectangle.perimeter() == 16


def test_add_area(generic_rectangle):
    assert generic_rectangle.add_area(generic_rectangle) == 30
