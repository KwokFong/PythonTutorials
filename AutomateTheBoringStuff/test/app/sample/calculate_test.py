import unittest
from app.sample.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test1_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.subtract(10, 2))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(20, self.calc.multiply(10, 2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.divide(10, 2))


if __name__ == '__main__':
    unittest.main()
