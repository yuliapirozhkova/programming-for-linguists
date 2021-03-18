import unittest

from algorithms.calculator.reverse_polish_notation import OpFactory
from algorithms.calculator.reverse_polish_notation.binary_op import Plus, Minus, Multiplier, Divider, Power


# @unittest.skip
class OperatorCreationTestCase(unittest.TestCase):
    def test_create_plus(self):
        operator = '+'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Plus)

    def test_create_minus(self):
        operator = '-'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Minus)

    def test_create_multiplier(self):
        operator = '*'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Multiplier)

    def test_create_divider(self):
        operator = '/'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Divider)

    def test_create_power(self):
        operator = '^'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Power)

    def test_create_wrong_operator(self):
        operator = '.'
        self.assertRaises(AssertionError, OpFactory.get_op_by_symbol, operator)


# @unittest.skip
class OperatorPriorityTestCase(unittest.TestCase):
    def test_priority(self):
        plus = OpFactory.get_op_by_symbol('+')
        minus = OpFactory.get_op_by_symbol('-')
        multiplier = OpFactory.get_op_by_symbol('*')
        divider = OpFactory.get_op_by_symbol('/')
        power = OpFactory.get_op_by_symbol('^')
        self.assertFalse(plus > minus)
        self.assertFalse(minus > plus)
        self.assertFalse(minus > multiplier)
        self.assertTrue(multiplier > minus)
        self.assertFalse(multiplier > divider)
        self.assertFalse(divider > multiplier)
        self.assertFalse(divider > power)
        self.assertTrue(power > divider)
