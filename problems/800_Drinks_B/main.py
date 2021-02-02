#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	fracts = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	print(format(100*sum(fracts)/(n*100), '.12f'))

		
