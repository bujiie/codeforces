#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	r = fp.readline().strip()

	if '1' in r:
		print('HARD')
	else:
		print('EASY')
	
		
