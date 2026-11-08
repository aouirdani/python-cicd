from calculatrice import addition, multiplication


def test_addition():
    assert addition(2, 3) == 5


def test_multiplication():
    assert multiplication(4, 3) == 12
