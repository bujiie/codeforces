#!/usr/bin/env python3

import fileinput


with fileinput.input() as fp:
	fp.readline()

	count = 0
	for line in fp:
		p,q = list(map(lambda n: int(n), line.strip().split(' ')))
		if (q-p) >= 2:
			count += 1

	print(count)	
