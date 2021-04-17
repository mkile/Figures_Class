import pytest
from source.classes import Circle


def test_creation():
    assert Circle('circle', [5])


def test_check_name(generic_circle):
    assert generic_circle.name == 'test_figure_name'


def test_check_area(generic_circle):
    assert int(round(generic_circle.area(), 0)) == 28


def test_check_perimeter(generic_circle):
    assert int(round(generic_circle.perimeter(), 0)) == 19


def test_add_area(generic_circle):
    assert int(round(generic_circle.add_area(generic_circle), 0)) == 57
