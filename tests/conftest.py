import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture(scope='class')
def triangle():
    return Triangle(14, 13.5, 5)


@pytest.fixture(scope='class')
def rectangle():
    return Rectangle(14, 5)


@pytest.fixture(scope='class')
def square():
    return Square(5.3)


@pytest.fixture(scope='class')
def circle():
    return Circle(9.1)
