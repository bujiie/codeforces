#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())

	odd = 'I hate '
	even = 'I love '

	r = []
	for i in range(1,n+1):
		if i % 2 == 0:
			r.append(even)
		else:
			r.append(odd)
	r = 'that '.join(r)
	r += 'it'
	print(r)
		
