import pytest
from source.classes import Figure


def test_baseclass_create():
    with pytest.raises(Exception):
        Figure('name', [1], 1)
