from yoshi_otter.interpolation import Interpolation

import pandas as pd
import numpy as np

import unittest


class TestInterpolation(unittest.TestCase):

    def setUp(self) -> None:
        def f(x):
            return 2 * x

        X = np.linspace(0, 10, num=100)
        Y = [f(x) for x in X]

        self.data = pd.DataFrame(data={'X': X, 'Y': Y})

    def test_class_instantiation(self):
        interpolation = Interpolation(self.data)
        self.assertIsInstance(interpolation, Interpolation)

    def test_minimums(self):
        interpolation = Interpolation(self.data)
        func, r2 = interpolation.minimums()

        self.assertEqual(func(1), 2)

    def test_polynomial_vandermonde(self):
        interpolation = Interpolation(self.data)
        func = interpolation.polynomial.vandermonde()

        self.assertAlmostEqual(func(1), 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_lagrange(self):
        interpolation = Interpolation(self.data)
        result = interpolation.polynomial.lagrange(1)

        self.assertAlmostEqual(result, 2)

    # @unittest.skip("Temporally not working")
    def test_polynomial_newton(self):
        interpolation = Interpolation(self.data)
        result = interpolation.polynomial.newton(1)

        self.assertAlmostEqual(result, 2)

    @unittest.skip("Temporally not working")
    def test_polynomial_gregory(self):
        interpolation = Interpolation(self.data)
        result = interpolation.polynomial.gregory(1)

        self.assertAlmostEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
