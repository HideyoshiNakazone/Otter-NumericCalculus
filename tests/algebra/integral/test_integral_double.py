from yoshi_otter.algebra.integral.double import Double

import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        def g(x, y):
            return x*y

        self.g = g

    def test_class_instantiation(self):
        Double(self.g)

    def test_riemann(self):

        double = Double(self.g)

        integral = double.riemann(0, 1, 0, 1, n=10**3)

        self.assertAlmostEqual(integral, .25, 2)

    def test_simpson(self):

        double = Double(self.g)

        integral = double.simpson(0, 1, 0, 1, n=10)

        self.assertAlmostEqual(integral, .25, 7)  # add assertion here


if __name__ == '__main__':
    unittest.main()
