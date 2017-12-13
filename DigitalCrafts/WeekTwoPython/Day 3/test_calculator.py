import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        print("SETUP IS RUN")

    def test_can_create_calculator_object(self):

        self.assertNotEqual(self.calculator,None)

        # checking if 2 = 2 if yes then pass the tes
        #self.assertEqual(2,5)
        #self.assertNotEqual(calculator,None)

    def test_can_add_numbers(self):
        ##self.calculator = Calculator()---this was removed becuase it is added to the setUp method. And the setUp method runs first every single time before a test is run.
        self.assertEqual(6,self.calculator.add(4,2))

    def test_can_subtract_numbers(self):
        self.assertEqual(6,self.calculator.subtract(8,2))

    def test_can_multiply_numbers(self):
        self.assertEqual(6,self.calculator.multiply(2,3))

    def test_can_divide_numbers(self):
        self.assertEqual(6,self.calculator.divide(12,2))


unittest.main()
