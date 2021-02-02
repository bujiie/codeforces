#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	earnings = list(map(lambda n: int(n), fp.readline().strip().split(' ')))
	
	global_max = 0
	local_max = 0
	prev_e = 0
	for e in earnings:
		if e >= prev_e:
			local_max += 1
		else:
			local_max = 1

		if local_max > global_max:
			global_max = local_max
		prev_e = e

	print(global_max)


		
