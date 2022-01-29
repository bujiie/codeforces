#!/usr/bin/env python3

import fileinput
from collections import defaultdict

H=defaultdict(int)
A=defaultdict(int)
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            continue
        h,a = [int(n) for n in line.split(' ')]
        H[h] += 1
        A[a] += 1

count = 0
for h in H:
    if h not in A:
        continue
    count += (H[h]*A[h])

print(count)
        
		
