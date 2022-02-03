#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n,m = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
   
    isect = set()
    for i in range(n):
        for j in range(m): 
            isect.add((i,j))

    player = "Malvika"
    while len(isect):
        i,j = isect.pop()
        for ii in range(n):
            isect.discard((ii,j))
        for jj in range(m):
            isect.discard((i,jj))
        player = "Akshat" if player == "Malvika" else "Malvika"

    print(player)

		
