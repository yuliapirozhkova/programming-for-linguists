from algorithms.calculator.calculator import ReversePolishNotationCalculator
from algorithms.calculator.converter import ReversePolishNotationConverter

if __name__ == '__main__':
    r = ReversePolishNotationConverter.convert('(1+2)^(1-2)-3')
    print(ReversePolishNotationCalculator().calculate(r))
