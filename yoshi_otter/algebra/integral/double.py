from typing import Callable


class Double:

    def __init__(self, function: Callable[[float, float], float]):
        self.f = function

    def riemann(self, a: float, b: float, c: float, d: float,
                n: int = 10 ** 4, m: int = None) -> float:

        if m is None:
            m = n

        dx = (b - a) / n
        dy = (d - c) / m
        kappa = a
        psi = c
        theta = 0

        while (psi + dy) < d:

            while (kappa + dx) < b:
                theta = theta + self.f(kappa, psi)
                kappa = kappa + dx

            psi = psi + dy
            kappa = a

        return theta * dx * dy

    def simpson(self, a: float, b: float, c: float, d: float,
                n: int = 10 ** 4, m: int = None) -> float:

        if m is None:
            m = n

        dx = (b - a) / n
        dy = (d - c) / m

        def x(i):
            return a + i * dx

        def y(i):
            return c + i * dy

        def g(i):

            sigma = 0
            upsilon = 0

            zeta = 1
            csi = 1

            while zeta <= (m / 2):
                sigma += self.f(x(i), y(2 * zeta - 1))
                zeta += 1

            while csi <= ((m / 2) - 1):
                upsilon += self.f(x(i), y(2 * csi))
                csi += 1

            return (dy / 3) * (self.f(x(i), y(0)) + self.f(x(i), y(m)) + 4 * sigma + 2 * upsilon)

        eta = 0
        theta = 0

        psi = 1
        kappa = 1

        while psi <= (n / 2):
            eta += g(2 * psi - 1)
            psi += 1

        while kappa <= ((n / 2) - 1):
            theta += g(2 * kappa)
            kappa += 1

        return (dx / 3) * (g(0) + g(n) + 4 * eta + 2 * theta)
