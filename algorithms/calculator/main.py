from algorithms.calculator.calculator import ReversePolishNotationCalculator
from algorithms.calculator.converter import ReversePolishNotationConverter

if __name__ == '__main__':
    r = ReversePolishNotationConverter('(1+2)^(1-2)-3').convert()
    print(ReversePolishNotationCalculator().calculate(r))
