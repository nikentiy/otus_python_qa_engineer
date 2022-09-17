import math

import pytest


@pytest.mark.parametrize("figure", ['triangle', 'rectangle', 'square', 'circle'])
def test_name_exists(figure, request):
    obj = request.getfixturevalue(figure)
    assert hasattr(obj, 'name') and obj.name is not None


def test_circle_perimeter(circle):
    assert circle.perimeter == (2 * math.pi * circle.r)


def test_circle_area(circle):
    assert circle.area == (math.pi * (circle.r**2))


def test_triangle_area(triangle):
    half = triangle.perimeter/2
    assert triangle.area == math.sqrt(half*(half-triangle.a)*(half-triangle.b)*(
            half-triangle.c))


def test_triangle_perimeter(triangle):
    assert triangle.perimeter == triangle.a + triangle.b + triangle.c


def test_rectangle_perimeter(rectangle):
    assert rectangle.perimeter == 2*(rectangle.a + rectangle.b)


def test_rectangle_area(rectangle):
    assert rectangle.area == rectangle.a * rectangle.b


def test_square_perimeter(square):
    assert square.perimeter == 4*square.a


def test_square_area(square):
    assert square.area == square.a * square.a


@pytest.mark.parametrize("figure", ['triangle', 'rectangle', 'square', 'circle'])
def test_add_area(figure, request, triangle):
    obj = request.getfixturevalue(figure)
    assert obj.add_area(triangle) == triangle.area + obj.area
