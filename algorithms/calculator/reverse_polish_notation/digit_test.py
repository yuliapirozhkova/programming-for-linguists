import unittest

from algorithms.calculator.reverse_polish_notation import Digit


class DigitTestCase(unittest.TestCase):
    def test_initialize_digit_from_sting(self):
        digit = Digit('1.4')

        self.assertEqual(digit.digit, 1.4)

    def test_initialize_digit_from_float(self):
        digit = Digit(1.4)

        self.assertEqual(digit.digit, 1.4)

    def test_initialize_digit_from_normalized_string(self):
        digit = Digit('1e-4')

        self.assertEqual(digit.digit, 1*10**-4)
