import math

ab = int(input())
bc = int(input())
ac = math.sqrt(pow(ab, 2) + pow(bc, 2))

cm = bm = ac / 2.
b_radian = math.acos(bc / (2 * cm))
b_degree = int(round((180 * b_radian) / math.pi))
print(f'{b_degree}{chr(176)}')