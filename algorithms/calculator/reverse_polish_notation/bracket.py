"""
Programming for linguists

Interfaces for brackets
"""
from algorithms.calculator.reverse_polish_notation.op import Op


class Bracket(Op):
    """
    Base interface for brackets
    """
    pass

class OpenBracket(Bracket):
    """
    Interface for open bracket
    """
    symb = '('
    #priority

class CloseBracket(Bracket):
    """
    Interface for close bracket
    """
    symb = ')'
    #priority