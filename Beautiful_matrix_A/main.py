#!/usr/bin/env python3

import fileinput

m = []
for i, line in enumerate(fileinput.input()):
    line = line.strip()
    m.append(list(map(lambda n: int(n), line.split(' '))))

c = (2,2)
p = None

for r in range(len(m)):
    if 1 in m[r]:
        p = (r, m[r].index(1))
        break

cr, cc = c
pr, pc = p
print(abs(pr-cr) + abs(pc-cc))