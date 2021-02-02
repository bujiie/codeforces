#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n,m = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
	k = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	diffs = []
	k.sort()

	i = 0
	s = -1

	while i+n <= len(k):
		sub_k = k[i:i+n]
		r = sub_k[-1] - sub_k[0] 
		if s < 0 or r < s:
			s = r
		i += 1

	print(s)

		
