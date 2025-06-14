import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(125, 50), 175)
        self.assertEqual(self.calc.add(20, -18), 2)
        self.assertEqual(self.calc.add(-3, 13), 10)
        self.assertEqual(self.calc.add(-27, -3), -30)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(18, 9), 9)
        self.assertEqual(self.calc.subtract(13, 75), -62)
        self.assertEqual(self.calc.subtract(10, -3), 13)
        self.assertEqual(self.calc.subtract(-97, 26), -123)
        self.assertEqual(self.calc.subtract(-85, -45), -40)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(15, 6), 90)
        self.assertEqual(self.calc.multiply(-7, 9), -63)
        self.assertEqual(self.calc.multiply(4, -23), -92)
        self.assertEqual(self.calc.multiply(-5, -41), 205)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(40, 8), 5)
        self.assertEqual(self.calc.divide(-95, 5), -19)
        self.assertEqual(self.calc.divide(122, -2), -61)
        self.assertEqual(self.calc.divide(-33, -3), 11)

    
    def test_divide_by_zero(self):
        return self.assertEqual(self.calc.divide(10, 0), None)