from typing import Callable


class Edo:

    def __init__(self, function: Callable[[float], float]) -> None:
        self.F = function

    def euler(self, a: float, y: float, b: float, n: int = 10**6) -> float:

        dx = (b - a) / n

        def x(i):
            return a + i * dx

        for i in range(n):
            y = y + (self.F(x(i), y)) * dx

        return y

    def runge(self, a: float, y: float, b: float, n: int = 10**6) -> float:

        dx = (b - a) / n

        def x(i):
            return a + i * dx

        for i in range(n):
            y = y + (dx / 2) * (self.F(x(i), y) + self.F(x(i + 1), (y + (dx * self.F(x(i), y)))))

        return y

    def adams(self, a: float, y: float, b: float, n: int = None
              ) -> float:

        if n is None:
            n = 10 ** 6

        dx = (b - a) / n

        def x(i):
            return a + i * dx

        for i in range(n):
            f0 = self.F(x(i), y)
            f1 = self.F(x(i + 1), y + dx * self.F(x(i) + (dx / 2), y + (dx / 2) * self.F(x(i), y)))
            f2 = self.F(x(i + 2), y + (dx / 2) * (3 * f1 - f0))

            y += (dx / 12) * (5 * f2 + 8 * f1 - f0)

        return y