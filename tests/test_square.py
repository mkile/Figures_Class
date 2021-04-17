import pytest
from source.classes import Square


def test_creation():
    assert Square('square', [2])


def test_null_side_creation():
    with pytest.raises(Exception):
        assert Square('square', [0])


def test_check_name(generic_square):
    assert generic_square.name == 'test_figure_name'


def test_check_area(generic_square):
    assert int(round(generic_square.area(), 0)) == 9


def test_check_perimeter(generic_square):
    assert generic_square.perimeter() == 12


def test_add_area(generic_square):
    assert generic_square.add_area(generic_square) == 18
