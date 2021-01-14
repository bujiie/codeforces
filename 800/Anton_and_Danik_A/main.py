#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	fp.readline()
	games = list(fp.readline().strip())
	A = games.count('A')
	D = games.count('D')

	if A > D:
		print('Anton')
	elif A < D:
		print('Danik')
	else:
		print('Friendship')

		
