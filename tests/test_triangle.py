import pytest
from source.classes import Triangle


def test_creation():
    assert Triangle('triangle', [2, 3, 5])


def test_check_name():
    test_figure = Triangle('test_figure_name', [2, 3, 5])
    assert test_figure == 'test_figure_name'


def test_check_area():
    test_figure = Triangle('test_figure_name', [2, 3, 5])
    assert int(round(test_figure.area(), 0)) == 4