#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	last = None
	g = 1
	for m in fp:
		s = m.strip()
		if last is None:
			last = s
			continue

		if s != last:
			g += 1
			last = s
	print(g)

		
