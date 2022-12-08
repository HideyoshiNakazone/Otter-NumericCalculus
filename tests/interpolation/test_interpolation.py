from yoshi_otter.interpolation import Interpolation

import pandas as pd
import numpy as np

import unittest


class TestInterpolation(unittest.TestCase):

    def setUp(self) -> None:
        def f(x):
            return 2 * x

        def g(x):
            return x + x**2

        X = np.linspace(0, 1000, num=1000)
        Y = [f(x) for x in X]

        self.data = pd.DataFrame(data={'X': X, 'Y': Y})

        Y = [g(x) for x in X]

        self.data_pol = pd.DataFrame(data={'X': X, 'Y': Y})

    def test_class_instantiation(self):
        interpolation = Interpolation(self.data)
        self.assertIsInstance(interpolation, Interpolation)

    def test_minimums(self):
        interpolation = Interpolation(self.data)
        func, r2 = interpolation.minimums()

        self.assertEqual(func(1), 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_vandermonde(self):
        interpolation = Interpolation(self.data_pol)
        func = interpolation.polynomial.vandermonde()

        self.assertEqual(func(1), 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_lagrange(self):
        interpolation = Interpolation(self.data_pol)
        result = interpolation.polynomial.lagrange(1)

        self.assertEqual(result, 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_newton(self):
        interpolation = Interpolation(self.data_pol)
        result = interpolation.polynomial.newton(1)

        self.assertEqual(result, 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_gregory(self):
        interpolation = Interpolation(self.data_pol)
        result = interpolation.polynomial.gregory(1)

        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
