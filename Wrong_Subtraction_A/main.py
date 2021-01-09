#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n, k = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

    for i in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1

    print(n)
        

    
    
    
		
