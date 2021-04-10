import pytest
from source.classes import Triangle


def test_creation():
    assert Triangle('triangle', [2, 4, 5])


def test_wrong_triangle_creation_error():
    with pytest.raises(Exception):
        Triangle('triangle', [2, 9, 5])


def test_check_name(generic_triangle):
    assert generic_triangle.name == 'test_figure_name'


def test_check_area(generic_triangle):
    assert int(round(generic_triangle.area(), 0)) == 4


def test_check_perimeter(generic_triangle):
    assert generic_triangle.perimeter() == 11


def test_add_area(generic_triangle):
    assert int(round(generic_triangle.add_area(generic_triangle), 0)) == 8
