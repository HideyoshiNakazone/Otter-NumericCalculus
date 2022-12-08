from yoshi_otter.shared import InvalidFunctionSignature
from yoshi_otter import algebra as ot

import unittest


class TestOtterAlgebra(unittest.TestCase):

    def setUp(self):
        def f(x):
            return 2*x

        def g(x, y):
            return x*y

        self.f = f
        self.g = g

    def test_class_instantiation(self):
        algebra = ot.Algebra(self.f)
        self.assertIsInstance(algebra, ot.Algebra)

    def test_derivative(self):
        algebra = ot.Algebra(self.f)
        derivative = algebra.d(0)

        self.assertEqual(derivative, 2)

    def test_derivative_raises_exception(self):
        algebra = ot.Algebra(self.g)

        with self.assertRaises(InvalidFunctionSignature):
            algebra.d(0)


if __name__ == '__main__':
    unittest.main()
