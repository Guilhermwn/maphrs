import statistics as s
import math as mt

from maphrs.stats.descriptive import standard_deviation

x = [10,34,23,54,9]
y = [1,5,6,10,13]

print(standard_deviation(x))

# assert m_s.mean(x) == s.mean(x)
# assert m_s.sqrt(2) == mt.sqrt(2)
# assert m_s.standard_deviation(x) == s.stdev(x)
# assert m_s.relative_error(9.76, 9.78) == ((9.76 - 9.78) / 9.78) * 100

save_opt = {"save":True, "filename": "plot", "format":"svg", "bytes": True}
