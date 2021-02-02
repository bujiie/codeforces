#!/usr/bin/env python3

import fileinput
import math


with fileinput.input() as fp:
	n = int(fp.readline().strip())
	
	if n % 2 == 0:
		print(n//2)
	else:
		print(-1*((n//2)+1))

		
