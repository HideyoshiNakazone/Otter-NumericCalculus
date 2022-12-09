from yoshi_seals import process as sl
from typing import Callable, Any
import numpy as np


class Interpolation:
    """
    Data should be organized in a dataframe of two columns: X and Y
    """

    def __init__(self, data) -> None:

        self.data = data
        self.polynomial = self.__Polynomial(self.data)

    def minimums(self) -> Callable[[Any], float]:

        theta = 0
        # somatorio de x
        for i in range(self.data.shape[0]):
            theta += self.data.X[i]

        eta = 0
        # somatorio de y
        for i in range(self.data.shape[0]):
            eta += self.data.Y[i]

        sigma = 0
        # somatorio de xy
        for i in range(self.data.shape[0]):
            sigma += self.data.X[i] * self.data.Y[i]

        omega = 0
        # somatorio de x^2self.dself.dself.d
        for i in range(self.data.shape[0]):
            omega += self.data.X[i] ** 2

        a = (self.data.shape[0] * sigma - theta * eta) / (self.data.shape[0] * omega - (theta ** 2))

        b = (theta * sigma - eta * omega) / ((theta ** 2) - self.data.shape[0] * omega)

        ym = 0

        for i in range(self.data.shape[0]):
            ym += self.data.Y[i] / self.data.shape[0]

        sqreq = 0

        for i in range(self.data.shape[0]):
            sqreq += ((a * self.data.X[i] + b) - ym) ** 2

        sqtot = 0

        for i in range(self.data.shape[0]):
            sqtot += (self.data.Y[i] - ym) ** 2

        r2 = sqreq / sqtot

        return lambda x: a * x + b, r2

    class __Polynomial:

        def __init__(self, data) -> None:
            self.data = data

        def vandermonde(self) -> Callable[[Any], float]:

            matrix = np.zeros((self.data.shape[0], self.data.shape[0]))

            for k in range(self.data.shape[0]):
                matrix[:, k] = self.data.X[:].copy() ** k

            array = np.array(self.data.Y.tolist()).reshape(self.data.shape[0], 1)
            coefficient_matrix = sl.gauss(matrix, array)[:]

            def __f(coefficients, x):
                y = 0
                for i in range(0, coefficients.shape[0]):
                    y += float(coefficients[i]) * (x ** i)

                return y

            return lambda x: __f(coefficient_matrix, x)

        def lagrange(self, x: float) -> float:

            def L(k, x):

                up = 1
                down = 1

                for i in [x for x in range(self.data.X.shape[0]) if x != k]:
                    up = up * (x - self.data.X[i])

                for i in [x for x in range(self.data.X.shape[0]) if x != k]:
                    down = down * (self.data.X[k] - self.data.X[i])

                return up / down

            y = 0

            for i in range(self.data.X.shape[0]):
                y += self.data.Y[i] * L(i, x)

            return y

        def newton(self, x: float) -> float:

            d = np.array(np.zeros((self.data.shape[0], self.data.shape[0])))

            d[0] = self.data.Y

            i = j = 0

            while i < self.data.shape[0]:

                while j < (self.data.shape[0] - (i + 1)):
                    d[i + 1][j] = (d[i][j + 1] - d[i][j]) / (self.data.X[(i + 1) + j] - self.data.X[j])
                    j += 1

                i += 1
                j = 0

            def f(x):

                y = d[0][0]
                i = 0

                while (i + 1) < self.data.shape[0]:

                    mult = 1
                    k = 0
                    while k <= i:
                        mult = mult * (x - self.data.X[k])
                        k += 1

                    y += d[i + 1][0] * mult
                    i += 1

                return y

            self.f = f

            return f(x)

        def gregory(self, x: float) -> float:

            h = self.data.X[0] - self.data.X[1]

            d = np.array(np.zeros((self.data.shape[0], self.data.shape[0])))

            d[0] = self.data.Y

            i = 0
            while i < self.data.shape[0]:

                j = 0
                while j < (self.data.shape[0] - (i + 1)):
                    d[i + 1][j] = (d[i][j + 1] - d[i][j]) / ((i + 1) * h)
                    j += 1

                i += 1

            y = d[0][0]

            i = 0
            while (i + 1) < self.data.shape[0]:
                mult = 1
                k = 0

                while k <= i:
                    mult = mult * (x - self.data.X[k])
                    k += 1

                y += d[i + 1][0] * mult
                i += 1

            return -y
