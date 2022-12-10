from yoshi_otter.algebra.edo import Edo

import unittest


class TestEdo(unittest.TestCase):

    def setUp(self):
        def f(x, y):
            return 2*x

        self.f = f

    def test_class_instantiation(self):
        edo = Edo(self.f)
        self.assertIsInstance(edo, Edo)

    def test_euler(self):
        edo = Edo(self.f)
        y = edo.euler(0, 0, 1)

        self.assertAlmostEqual(y, 1, 5)

    def test_runge(self):
        edo = Edo(self.f)
        y = edo.runge(0, 0, 1)

        self.assertAlmostEqual(y, 1, 5)

    def test_adams(self):
        edo = Edo(self.f)
        y = edo.adams(0, 0, 1)

        self.assertAlmostEqual(y, 1, 5)


if __name__ == '__main__':
    unittest.main()
