#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	w1 = fp.readline().strip()
	w2 = fp.readline().strip()

	if w1 == w2[::-1]:
		print('YES')
	else:
		print('NO')
	

		
