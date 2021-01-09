#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    l, b = list(map(lambda n: int(n), fp.readline().split(' ')))

    years = 0
    while l <= b:
        l *= 3
        b *= 2
        years += 1

    print(years) 
		
