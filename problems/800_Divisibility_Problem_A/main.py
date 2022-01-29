#!/usr/bin/env python3

import fileinput

cases=[]
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            continue
        cases.append([int(n) for n in line.split(' ')])

for case in cases:
    a,b = case
    if a <= b:
        print(b-a)
    else:
        if a % b == 0:
            # evenly divisible so there's no need to
            # make a move.
            print(0)
        else:
            # if there's a remainder, we need to move
            # one more step. we can calculate what the
            # new total should be with the additional
            # step then subtract the old value of a to
            # get how many additional moves we need.
            print((b * ((a // b) + 1)) - a)

		
