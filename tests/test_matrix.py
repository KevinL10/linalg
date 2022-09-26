import pytest
from linalg.vector import Vector
from linalg.matrix import Matrix


@pytest.fixture
def m1():
    return Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])


@pytest.fixture
def m2():
    return Matrix([[2, -2], [1, 5], [0, 4], [1, 3]])


def test_constructor(m1, m2):
    assert [1, 0, 0] == m1[0]
    assert [0, -1, 1] == m1[2]
    assert 1 == m1[1][1]
    assert 3 == m2[3][1]
    assert (3, 3) == m1.size()
    assert (4, 2) == m2.size()


def test_multiply_scalar(m1, m2):
    assert Matrix([[-4, 4], [-2, -10], [0, -8], [-2, -6]]) == m2 * -2
    assert Matrix([[4, 0, 0], [-4, 4, 0], [0, -4, 4]]) == m1 * 4


def test_multiply_vector(m1, m2):
    assert Vector([1, 3, 5]) == m1 * Vector([1, 4, 9])
    assert Vector([4, 8, 4, 6]) == m2 * Vector([3, 1])


def test_multiply_matrix_square():
    assert Matrix([[5, 6], [1, 0]]) == Matrix([[1, 1], [2, -1]]) * Matrix(
        [[2, 2], [3, 4]]
    )
    assert Matrix([[0, 0, 0], [1, 2, 3], [2, 4, 6]]) == Matrix(
        [[0], [1], [2]]
    ) * Matrix([[1, 2, 3]])


def test_multiply_matrix_nonsquare(m2):
    assert Matrix([[4, -2, -10], [20, -1, 1], [12, 0, 4], [14, -1, -1]]) == m2 * Matrix(
        [[5, -1, -4], [3, 0, 1]]
    )


def test_add(m2):
    assert Matrix([[2, 1], [-1, 6], [4, 9], [-7, 4]]) == m2 + Matrix(
        [[0, 3], [-2, 1], [4, 5], [-8, 1]]
    )


def test_get_column(m1, m2):
    assert [1, -1, 0] == m1.column(0)
    assert [-2, 5, 4, 3] == m2.column(1)


def test_get_column_unchanged(m1):
    col = m1.column(1)
    col.append(-1)
    assert m1 == Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])


def test_get_row_unchanged(m1):
    row = m1[0]
    row.append(-1)
    assert m1 == Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])


def test_identity():
    sz = 5
    identity = Matrix.identity(sz)
    for i in range(sz):
        for a in range(sz):
            assert (i == a) == identity[i][a]


def test_augment(m1, m2):
    assert Matrix([[2, -2, 2], [1, 5, 3], [0, 4, 4], [1, 3, 5]]) == m2.augment(
        Vector([2, 3, 4, 5])
    )
    assert Matrix([[1, 0, 0, 5], [-1, 1, 0, -2], [0, -1, 1, -9]]) == m1.augment(
        Vector([5, -2, -9])
    )


def test_solve_vector(m1, m2):
    A = Matrix([[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
    b = Vector([2, 8, 10])
    assert A.solve_vector(b) == Vector([-1, 2, 2])


def test_solve_vector2(m1, m2):
    A = Matrix([[1, 1, 1], [1, 2, 2], [1, 2, 3]])
    b = Vector([6, 9, 10])
    assert A.solve_vector(b) == Vector([3, 2, 1])


# requires rearranging rows to avoid 0 pivot
def test_solve_vector3(m1, m2):
    A = Matrix([[1, 2, 3], [2, 4, 7], [3, 5, 2]])
    b = Vector([25, 57, 23])
    assert A.solve_vector(b) == Vector([-2, 3, 7])
