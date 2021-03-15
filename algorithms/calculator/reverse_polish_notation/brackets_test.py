import unittest

from algorithms.calculator.reverse_polish_notation.bracket import OpenBracket, CloseBracket


# @unittest.skip
class BracketsTestCase(unittest.TestCase):
    def test_open_bracket_symbol(self):
        open_bracket = OpenBracket()

        self.assertEqual(open_bracket.symbol, '(')

    def test_close_bracket_symbol(self):
        close_bracket = CloseBracket()

        self.assertEqual(close_bracket.symbol, ')')
