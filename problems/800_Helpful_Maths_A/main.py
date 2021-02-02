#!/usr/bin/env python3

import fileinput

p = []
with fileinput.input() as fp:
    p = list(map(lambda n: int(n), fp.readline().strip().split('+')))

p.sort()
p = list(map(lambda n: str(n), p))
print('+'.join(p))
    
		
