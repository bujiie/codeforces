#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    n,m = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

    if n+m < 4:
        print("Akshat")    
    elif (n*m) % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")
        


		
