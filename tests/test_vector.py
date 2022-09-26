import pytest
from linalg.vector import Vector
from linalg.applications import cauchy_schwarz, triangle_inequality


@pytest.fixture
def v1():
    return Vector([5, -2, 17, 4])


@pytest.fixture
def v2():
    return Vector([6, -12, 3, -4])


def test_str(v1):
    assert "[5, -2, 17, 4]" == str(v1)


def test_len(v1):
    assert 4 == len(v1)


def test_get_item(v1, v2):
    assert 17 == v1[2]
    assert 6 == v2[0]


def test_add(v1, v2):
    assert Vector([11, -14, 20, 0]) == v1 + v2
    assert Vector([11, -14, 20, 0]) == v2 + v1


def test_sub(v1, v2):
    assert Vector([-1, 10, 14, 8]) == v1 - v2
    assert Vector([1, -10, -14, -8]) == v2 - v1


def test_mul(v1, v2):
    assert Vector([15, -6, 51, 12]) == v1 * 3
    assert Vector([-12, 24, -6, 8]) == -2 * v2


def test_dot(v1, v2):
    assert 5 * 6 + -2 * -12 + 17 * 3 + 4 * -4 == v1.dot(v2)


def test_length(v1):
    assert abs(v1.length() - 18.2756668825) < 1e6


def test_inequalities(v1, v2):
    assert cauchy_schwarz(v1, v2)
    assert triangle_inequality(v1, v2)
