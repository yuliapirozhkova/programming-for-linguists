from algorithms.calculator.reverse_polish_notation.digit import Digit
from algorithms.calculator.reverse_polish_notation.op import Op


class BinaryOp(Op):
    @staticmethod
    def function(first_element, second_element) -> float:
        raise NotImplementedError


class Plus(BinaryOp):
    priority = 0
    symbol = '+'

    @staticmethod
    def function(first: Digit, second: Digit) -> float:
        return first.digit + second.digit


class Minus(BinaryOp):
    priority = 0
    symbol = '-'

    @staticmethod
    def function(first: float, second: float) -> float:
        return first - second


class Multiplier(BinaryOp):
    priority = 1
    symbol = '*'

    @staticmethod
    def function(first: float, second: float) -> float:
        return first * second


class Divider(BinaryOp):
    priority = 1
    symbol = '/'

    @staticmethod
    def function(first: float, second: float) -> float:
        return first / second


class Power(BinaryOp):
    priority = 2
    symbol = '^'

    @staticmethod
    def function(first: float, second: float) -> float:
        return second ** first
