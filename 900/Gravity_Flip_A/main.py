#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	ai = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	ai.sort()
	c = list(map(lambda i: str(i), ai))
	print(' '.join(c))
		
		

		
