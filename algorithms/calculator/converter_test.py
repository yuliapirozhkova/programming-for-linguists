# @unittest.skip
import unittest

from algorithms.calculator.converter import ReversePolishNotationConverter
from algorithms.calculator.reverse_polish_notation import OpenBracket, CloseBracket


class ConverterTestCase(unittest.TestCase):
    def test_read_simple_digit(self):
        rpn = ReversePolishNotationConverter.convert('.234')
        print(rpn)
        expected_result = 1.234
        self.assertEqual(digit.digit, expected_result)

    def test_read_digit_without_integer(self):
        rpn_converter = ReversePolishNotationConverter('234')
        digit = rpn_converter.read_digit('.')
        expected_result = 0.234
        self.assertEqual(digit.digit, expected_result)

    def test_read_digit_without_fractional(self):
        rpn_converter = ReversePolishNotationConverter('.')
        digit = rpn_converter.read_digit('1')
        expected_result = 1.0
        self.assertEqual(digit.digit, expected_result)

    def test_open_bracket_checker(self):
        rpn_converter = ReversePolishNotationConverter('.')
        open_bracket_operator = OpenBracket()
        self.assertTrue(rpn_converter.is_open_bracket(open_bracket_operator))
        close_bracket_operator = CloseBracket()
        self.assertFalse(rpn_converter.is_open_bracket(close_bracket_operator))

