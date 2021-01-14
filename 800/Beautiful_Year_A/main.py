#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	year = int(fp.readline().strip())

	i = year
	while True:
		i += 1
		s = str(i)
		s_len = len(s)
		digits = set(s)
		if len(digits) == s_len:
			print(i)
			break


		
