#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    x = int(fp.readline().strip())

    step_sizes = [1,2,3,4,5]
    steps = 0
 
    for s in reversed(step_sizes):
        if x <= 0:
            break

        steps += (x//s)
        x = x % s         
         
    print(steps)		
