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


# @unittest.skip
class OperatorPriorityTestCase(unittest.TestCase):
    def test_priority(self):
        plus = OpFactory.get_op_by_symbol('+')
        minus = OpFactory.get_op_by_symbol('-')
        multiplier = OpFactory.get_op_by_symbol('*')
        divider = OpFactory.get_op_by_symbol('/')
        power = OpFactory.get_op_by_symbol('^')
        self.assertFalse(plus.is_more_prioritized_than(minus))
        self.assertFalse(minus.is_more_prioritized_than(plus))
        self.assertFalse(minus.is_more_prioritized_than(multiplier))
        self.assertTrue(multiplier.is_more_prioritized_than(minus))
        self.assertFalse(multiplier.is_more_prioritized_than(divider))
        self.assertFalse(divider.is_more_prioritized_than(multiplier))
        self.assertFalse(divider.is_more_prioritized_than(power))
        self.assertTrue(power.is_more_prioritized_than(divider))
