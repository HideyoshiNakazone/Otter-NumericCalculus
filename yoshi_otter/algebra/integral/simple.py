from typing import Callable


class Simple:
    def __init__(self, function: Callable[[float], float]) -> None:
        self.f = function

    def riemann(self, a: float, b: float, n: int = 10 ** 6) -> float:

        delta = (b - a) / n

        psi = a
        theta = 0

        while (psi + delta) <= b:
            theta += (self.f(psi) + self.f(psi + delta)) / 2
            psi += delta

        integral = delta * theta

        return integral

    def simpson(self, a: float, b: float, n: int = 10 ** 6) -> float:

        def x(i):
            return a + i * h

        h = (b - a) / n

        eta = 0
        theta = 0

        psi = 1
        kappa = 1

        while psi <= (n / 2):
            eta = eta + self.f(x(2 * psi - 1))
            psi = psi + 1

        while kappa <= ((n / 2) - 1):
            theta = theta + self.f(x(2 * kappa))
            kappa = kappa + 1

        return (h / 3) * (self.f(x(0)) + self.f(x(n)) + 4 * eta + 2 * theta)