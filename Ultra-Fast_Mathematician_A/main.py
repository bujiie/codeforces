#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	b1 = fp.readline().strip()
	b2 = fp.readline().strip()
	
	b = int(b1,2) ^ int(b2,2)
	print(format(b, f'0{len(b1)}b'))
