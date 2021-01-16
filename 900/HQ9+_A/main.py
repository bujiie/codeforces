#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	ins = list(fp.readline().strip())

	prints = False
	for i in ins:
		if i in ['H','Q','9']:
			print('YES')
			prints = True
			break

	if not prints:
		print('NO')



		
