from typing import Type

from algorithms.calculator.reverse_polish_notation.element import Element


class OpFactory:
    _registry = {}

    @staticmethod
    def add_op_class(cls: Type['Op']):
        if not cls.symbol:
            return
        OpFactory._registry[cls.symbol] = cls

    @staticmethod
    def get_op_by_symbol(op_symbol: str) -> Type['Op']:
        return OpFactory._registry[op_symbol]()


class OpMeta(type):
    def __new__(mcs, *args, **kwargs):
        op_class = super().__new__(mcs, *args, **kwargs)
        OpFactory.add_op_class(op_class)
        return op_class


class Op(Element, metaclass=OpMeta):
    priority = None
    symbol = None

    @staticmethod
    def function(*args, **kwargs) -> float:
        raise NotImplementedError
