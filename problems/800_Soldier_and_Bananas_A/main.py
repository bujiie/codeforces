#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    k,n,w = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
   
    t = 0 
    for i in range(w):
        t += k * (i+1)

    if n > t:
        print(0)
    else:
        print(t-n)
		
