import statistics as s
import math as mt

from src.maphrs import m_statistics as m

x = [10,34,23,54,9]

assert m.mean(x) == s.mean(x)
assert m.sqrt(2) == mt.sqrt(2)
assert m.standard_deviation(x) == s.stdev(x)