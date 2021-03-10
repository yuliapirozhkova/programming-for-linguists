from algorithms.calculator.calculator import ReversePolishNotationCalculator
from algorithms.calculator.converter import ReversePolishNotationConverter

if __name__ == '__main__':
    r = ReversePolishNotationConverter('1+1').convert()
    print(ReversePolishNotationCalculator().calculate(r))

