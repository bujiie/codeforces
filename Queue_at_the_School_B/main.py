#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n,t = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
    line = list(fp.readline().strip())

    for i in range(t): 
        j = 0
        while j < n-1:
            if line[j] == 'B' and line[j+1] == 'G':
                line[j], line[j+1] = line[j+1], line[j]
                j += 2
            else:
                j += 1
    
    print(''.join(line)) 
		
