#!/usr/bin/env python3

import fileinput
import math

with fileinput.input() as fp:
	n,k = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	l = 0
	if n % 2 > 0:
		# odd number of values
		l = (n//2) + 1
	else:
		l = (n//2)

	if k  > l:
		k = l - k
		print(2*k)
	else:
		# look at odds
		print((2*k) -1 )
		

		
