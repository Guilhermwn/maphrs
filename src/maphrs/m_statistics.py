from typing import Literal

def root(number:int|float, n:int) -> int|float:
    return number ** (1/n)

def sqrt(number: int|float) -> int|float:
    return root(number, 2)

def mean(values: list[int|float]):
    return sum(values) / len(values)

def standard_deviation(values: list[int|float], type: Literal["sample", "populational"]="sample"):
    if len(values) < 2:
        raise Exception("Minimum length of values need to be 2")
    if type.lower() == "sample":
         return sqrt(sum([ (xi - mean(values))**2 for xi in values ]) / (len(values)-1))
    if type.lower() == "populational":
         return sqrt(sum([ (xi - mean(values))**2 for xi in values ]) / (len(values)))

