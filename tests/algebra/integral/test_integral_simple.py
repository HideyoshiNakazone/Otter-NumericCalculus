from yoshi_otter.algebra.integral.simple import Simple

import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        def f(x):
            return 2*x

        self.f = f

    def test_class_instantiation(self):
        Simple(self.f)

    def test_riemann(self):

        simple = Simple(self.f)

        integral = simple.riemann(0, 1)

        self.assertAlmostEqual(integral, 1, 5)

    def test_simpson(self):

        simple = Simple(self.f)

        integral = simple.simpson(0, 1)

        self.assertAlmostEqual(integral, 1, 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
