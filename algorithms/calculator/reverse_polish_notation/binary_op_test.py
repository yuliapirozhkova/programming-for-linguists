import unittest

from algorithms.calculator.reverse_polish_notation import Digit
from algorithms.calculator.reverse_polish_notation.binary_op import Plus, Minus, Multiplier, Divider, Power


# @unittest.skip
class BinaryOpImplementationTestCase(unittest.TestCase):
    def test_plus(self):
        argument_1 = Digit(1)
        argument_2 = Digit(2)
        operator = Plus()

        self.assertEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_1.digit + argument_2.digit)

    def test_minus(self):
        argument_1 = Digit(1)
        argument_2 = Digit(2)
        operator = Minus()

        self.assertNotEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit - argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit - argument_1.digit)

    def test_multiple(self):
        argument_1 = Digit(3)
        argument_2 = Digit(2)
        operator = Multiplier()

        self.assertEqual(operator(argument_1, argument_2).digit, operator(argument_1, argument_2).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit * argument_2.digit)

    def test_division(self):
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        operator = Divider()

        self.assertNotEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit / argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit / argument_1.digit)

    def test_power(self):
        argument_1 = Digit(3)
        argument_2 = Digit(2)
        operator = Power()

        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit ** argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit ** argument_1.digit)

    def test_divider_multiplier_feature(self):
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        divider = Divider()
        multiplier = Multiplier()

        division_result = divider(argument_1, argument_2)
        self.assertEqual(multiplier(division_result, argument_2).digit, argument_1.digit)

    def test_plus_minus_feature(self):
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        minus = Minus()
        plus = Plus()

        minus_result = minus(argument_1, argument_2)
        self.assertEqual(plus(minus_result, argument_2).digit, argument_1.digit)
