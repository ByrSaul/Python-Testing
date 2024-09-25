import unittest
from src.calculator import sum, subtract, multiply, division

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_division(self):
        self.assertEqual(division(6, 2), 3)

    def test_error_division_by_zero(self):
         with self.assertRaises(ZeroDivisionError):
            division(5, 0)
