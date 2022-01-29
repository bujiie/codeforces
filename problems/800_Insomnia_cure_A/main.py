#!/usr/bin/env python3

import fileinput

mods=[]
total=-1
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        mods.append(int(line.strip()))
    total=mods[-1]
    mods=mods[:-1]

safe = set()
for n in range(1, total+1):
    match = False
    for m in mods:
        if n % m == 0:
            match = True
            break
    if not match:
        safe.add(n)

print(total - len(safe))

		
