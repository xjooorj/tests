import pytest


def test_area(the_rectangle):
    assert the_rectangle.area() == 10 * 20

def test_perimeter(the_rectangle):
    assert the_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_non_equal(the_rectangle, non_rectangle):
    assert the_rectangle != non_rectangle
