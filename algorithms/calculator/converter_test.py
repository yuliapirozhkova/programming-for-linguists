import unittest
from typing import Iterable

from parameterized import parameterized

from algorithms.calculator.converter import ReversePolishNotationConverter
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation, Digit


class ConverterTestCase(unittest.TestCase):
    @staticmethod
    def fill_rpn_with_data(rpn: ReversePolishNotation, data: Iterable):
        for element in data:
            rpn.put(element)

    def assert_rpn_equal(self, first: ReversePolishNotation, second: ReversePolishNotation):
        for actual_element in first:
            expected_element = next(second)
            self.assertEqual(actual_element, expected_element)

    @parameterized.expand([
        ['234', 234],
        ['.234', 0.234],
        ['1.', 1],
        ['1.4', 1.4],
    ])
    def test_digit(self, actual: str, expected_digit: float):
        actual_rpn = ReversePolishNotationConverter.convert(actual)
        expected_rpn = ReversePolishNotation()
        self.fill_rpn_with_data(expected_rpn, [Digit(expected_digit)])
        self.assert_rpn_equal(actual_rpn, expected_rpn)

    def test_raise_error_for_open_bracket(self):
        ReversePolishNotationConverter.convert(')')
        # self.assertRaises(KeyError, ReversePolishNotationConverter.convert, '(')
