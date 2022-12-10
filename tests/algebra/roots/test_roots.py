import unittest

from yoshi_otter.algebra.roots import Roots


class TestRoots(unittest.TestCase):

    def setUp(self):
        def f(x):
            return x

        self.f = f

    def test_class_instantiation(self):
        roots = Roots(self.f)
        self.assertIsInstance(roots, Roots)

    def test_bissec(self):
        roots = Roots(self.f)
        result = roots.bissec(-1, 1)

        self.assertAlmostEqual(result, 0, 6)

    def test_newton(self):
        roots = Roots(self.f)
        result = roots.newton(-1)

        self.assertAlmostEqual(result, 0, 6)

    def test_bissec_newton(self):
        roots = Roots(self.f)
        result = roots.bissec_newton(-1, 1)

        self.assertAlmostEqual(result, 0, 6)


if __name__ == '__main__':
    unittest.main()
