#!/usr/bin/env python3

import fileinput

levels=-1
x=set()
y=set()
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            levels = int(line)
        if i == 1:
            x = set([int(n) for n in line.split(' ')][1:])
        else:
            y = set([int(n) for n in line.split(' ')][1:])
    xy = x.union(y)

print("I become the guy." if len(xy) >= levels else "Oh, my keyboard!")
		
