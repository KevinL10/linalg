from .vector import Vector


class Matrix:
    # initialize with 2d list of values
    def __init__(self, data):
        self.__data = data

    # note: override equality check for matrices/vectors with floats
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__data == other.__data
        return False

    def __str__(self):
        return "\n".join([str(row) for row in self.__data])

    # data is safe to change
    def __getitem__(self, idx):
        return self.__data[idx][:]

    # either multiply by scalar, vector or matrix
    def __mul__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return self.__mul_scalar(x)

        if isinstance(x, Vector):
            return self.__mul_vector(x)

        return self.__mul_matrix(x)

    # multiply all elements by a scalar (self * c)
    def __mul_scalar(self, c):
        rows, cols = self.size()
        return Matrix(
            [[self.__data[i][a] * c for a in range(cols)] for i in range(rows)]
        )

    # multiply by a vector (self * x)
    def __mul_vector(self, v):
        assert len(self.__data[0]) == len(v)
        return Vector([Vector(self.__data[i]).dot(v) for i in range(len(self.__data))])

    # matrix addition (self + A)
    def __add__(self, A):
        assert self.size() == A.size()
        rows, cols = self.size()

        return Matrix(
            [[self.__data[i][a] + A[i][a] for a in range(cols)] for i in range(rows)]
        )

    # multiply by a matrix (self * A)
    def __mul_matrix(self, A):
        assert len(self.__data[0]) == A.size()[0]

        # (m x n) and (n x p) matrices
        m, n = self.size()
        p = len(A[0])

        return Matrix(
            [
                [Vector(self.__data[a]).dot(Vector(A.column(b))) for b in range(p)]
                for a in range(m)
            ]
        )

    # returns the column at idx
    def column(self, idx):
        return [self.__data[i][idx] for i in range(len(self.__data))]

    # returns (rows, columns)
    def size(self):
        return len(self.__data), len(self.__data[0])

    # returns an identity matrix of the specified size
    @staticmethod
    def identity(size):
        return Matrix([[0] * i + [1] + [0] * (size - i - 1) for i in range(size)])

    # appends vector v as an additional column
    def augment(self, v):
        assert len(self.__data) == len(v)
        return Matrix([self.__data[i] + [v[i]] for i in range(len(self.__data))])

    # returns the solution to Ax = b
    def solve_vector(self, b):
        data = [row[:] for row in self.__data]
        b = b.list()
        sz = len(b)
        idx = 0

        # convert matrix to upper triangular form
        while idx < len(data):
            if data[idx][idx] == 0:
                # rearrange rows to find a non-zero pivot
                for i in range(idx + 1, len(data)):
                    if data[i][idx] != 0:
                        data[idx], data[i] = data[i], data[idx]
                        b[idx], b[i] = b[i], b[idx]
                        break

                # if there isn't a pivot, then the matrix is singular
                if data[idx][idx] == 0:
                    raise Exception("Singular Matrix")

            pivot = data[idx][idx]
            for i in range(idx + 1, len(data)):
                multiplier = data[i][idx] / pivot
                data[i] = [
                    data[i][a] - data[idx][a] * multiplier for a in range(len(data[i]))
                ]
                b[i] -= multiplier * b[idx]

            idx += 1

        # back substitution
        x = b
        x[sz - 1] = b[sz - 1] / data[sz - 1][sz - 1]

        for i in range(sz - 2, -1, -1):
            for a in range(i + 1, sz):
                x[i] -= data[i][a] * x[a]
            x[i] /= data[i][i]

        return Vector(x)
