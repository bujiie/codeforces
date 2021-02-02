#!/usr/bin/env python3

import fileinput

# Assume we only have one line of input
slices = int(fileinput.input().readline().strip())

if slices < 3:
	print('NO', end='')
elif (slices - 2) % 2 == 0:
	print('YES', end='')
else:
	print('NO', end='')
	
