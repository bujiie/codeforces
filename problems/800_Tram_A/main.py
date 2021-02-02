#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n = int(fp.readline().strip())

    stops = []

    max_p = 0
    curr_p = 0
    for i in range(n):
        a,b = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
        curr_p -= a
        curr_p += b

        if curr_p > max_p:
            max_p = curr_p

    print(max_p)	
