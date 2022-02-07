#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n = fp.readline().strip()
    n1, n2 = n[:-1], n[:-2]+n[-1]
    print(max([int(n) for n in [n,n1,n2]]))


		
