from fractions import Fraction

class FractionMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
        self._validate_matrix()
    def _validate_matrix(self):
        for row in self.matrix:
            if len(row) != self.cols:
                raise ValueError("Все строки должны быть одной длины.")
    @classmethod
    def zero_matrix(cls, rows, cols):
        return cls([[Fraction(0) for _ in range(cols)] for _ in range(rows)])
    @property
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц.")
        return self._determinant(self.matrix)
    def _determinant(self, mat):
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            det = Fraction(0)
            for c in range(len(mat)):
                minor = [row[:c] + row[c+1:] for row in mat[1:]]
                det += ((-1) ** c) * mat[0][c] * self._determinant(minor)
            return det
    def __add__(self, other):
        self._validate_same_dimension(other)
        return FractionMatrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])
    def __sub__(self, other):
        self._validate_same_dimension(other)
        return FractionMatrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Невозможно умножить матрицы: количество столбцов первой должно равняться количеству строк второй.")
        result = FractionMatrix.zero_matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols))
        return result
    def transpose(self):
        return FractionMatrix([[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)])
    def _validate_same_dimension(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размерности матриц не совпадают.")
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
print(m1 + m2)  # Матрица из дробей
print(m1 * m2)  # Умножение матриц
print(m1.determinant)  # Вычисление определителя