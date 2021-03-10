from algorithms.calculator.reverse_polish_notation.element import Element


class Digit(Element):
    def __init__(self, digit_as_string: str):
        self.digit = float(digit_as_string)
