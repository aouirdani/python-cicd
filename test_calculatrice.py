import pytest

from calculatrice import addition, division, multiplication


def test_addition():
    assert addition(2, 3) == 5


def test_multiplication():
    assert multiplication(4, 3) == 12

def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10, 0)
