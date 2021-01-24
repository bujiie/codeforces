#!/usr/bin/env python3

import fileinput
import math

with fileinput.input() as fp:
	n,k = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	# 0 1 2 3 4 5 6 7 8 9
	# 1 3 5 7 9 2 4 6 8 10
	l = 0
	if n % 2 > 0:
		# odd number of values
		l = (n//2) + 1
	else:
		l = (n//2)

	if k > l:
		k = k-l
		print(2*k)
	else:
		# look at odds
		print((2*k) -1 )
		

		
