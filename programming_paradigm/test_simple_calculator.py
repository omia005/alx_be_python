from simple_calculator.py import SimpleCalculator
import unittest

class test_SimpleCalculator(unittest.TestCase):
   def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

   def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
     
   def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.add(4, 1), 3)

   def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.add(4, 1), 4)

   def test_division(self):
        self.assertEqual(self.calc.subtract(6, 3), 2)
        self.assertEqual(self.calc.add(4, 0))

if __name__ == '__main__':
    unittest.main()
