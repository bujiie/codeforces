#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n,h = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
    friends = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

    w = 0
    for a in friends:
        if a > h:
            w += 2
        else:
            w += 1

    print(w)
		
