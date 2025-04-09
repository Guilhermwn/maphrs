import statistics as s
import math as mt

from maphrs.statistics.descriptive import standard_deviation
from maphrs.eletronics.basic import find_resistor_association
from maphrs.objects.eletronics import ResistorUnity, Resistor, COMMERCIAL_RESISTORS

x = [10,34,23,54,9]
y = [1,5,6,10,13]

# print(standard_deviation(x))

# assert m_s.mean(x) == s.mean(x)
# assert m_s.sqrt(2) == mt.sqrt(2)
# assert m_s.standard_deviation(x) == s.stdev(x)
# assert m_s.relative_error(9.76, 9.78) == ((9.76 - 9.78) / 9.78) * 100
# save_opt = {"save":True, "filename": "plot", "format":"svg", "bytes": True}
# parallel = Resistor(100)|Resistor(200)

assoc_s = find_resistor_association(13260, "parallel", 30)
assoc_p = find_resistor_association(13260)

print(assoc_s)
print(assoc_p)