#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n = int(fp.readline().strip())
    p = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

    l = [None]*n
    for i,j in enumerate(p):
        l[j-1] = str(i+1)

    print(' '.join(l))
    
		
