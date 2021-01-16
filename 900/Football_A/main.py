#!/usr/bin/env python3

import fileinput
import re 

with fileinput.input() as fp:
	l = fp.readline().strip()
	match = re.search(r'(0|1)\1{6,}', l)
	if match is None:
		print('NO')
	else:
		print('YES')

		
