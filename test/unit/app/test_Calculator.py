import unittest

from app.Calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1,2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4,3), 1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2,3), 6)

    def test_divide(self):
        with self.subTest():
            self.assertEqual(Calculator.divide(9,3), 3)
        with self.subTest():
            with self.assertRaises(AssertionError):
                Calculator.divide(3,0)

    def test_power(self):
        with self.subTest():
            self.assertEqual(Calculator.power(2,3), 8)
        with self.subTest():
            self.assertEqual(Calculator.power(2,-2), 0.25)
        with self.subTest():
            with self.assertRaises(AssertionError):
                Calculator.power(2,2.5)

    def test_square_root(self):
        with self.subTest():
            self.assertTrue(1.9999999 < Calculator.square_root(4) < 2.0000001)
        with self.subTest():
            with self.assertRaises(AssertionError):
                Calculator.square_root(-1)