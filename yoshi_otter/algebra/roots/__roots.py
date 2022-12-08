from typing import Callable


class Roots:

    def __init__(self, function: Callable[[float], float] = None
                 ) -> float:
        if function is not None:
            self.f = function

    def bissec(self, a: float, b: float, e: float = 10**-6) -> float:

        fa = self.f(a)

        while abs(a - b) > e:

            c = (a + b) / 2
            fc = self.f(c)

            if (fa * fc) < 0:

                b = c

            else:

                a = c

            c = (a + b) / 2

        return c

    def __d(self, x: float, e: float) -> float:
        return (self.f(x + e) - self.f(x - e)) / (2 * e)

    def newton(self, a: float, e: float = 10**-6) -> float:

        fa = self.f(a)
        da = self.__d(a, e)
        b = a - fa / da

        while abs(a - b) > e:
            b = a
            a -= (fa / da)
            fa = self.f(a)
            da = self.__d(a, e)

        return a

    def bissec_newton(self, a: float, b: float, e: float = 10**-6) -> float:

        fa = self.f(a)

        c = (a + b) / 2  # 'c' é a raiz calculada

        while abs(a - b) > 0.1:

            fc = self.f(c)

            if fa * fc < 0:

                b = c

            else:

                a = c
                fa = self.f(a)

            c = (a + b) / 2

        fc = self.f(c)
        dc = self.__d(c, e)
        h = c - fc / dc  # 'h' é uma variável de controle

        while abs(c - h) > e:
            h = c
            c -= (fc / dc)
            fc = self.f(c)
            dc = self.__d(c, e)

        return c