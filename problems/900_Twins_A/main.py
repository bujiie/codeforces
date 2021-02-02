#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
	n = int(fp.readline().strip())
	coins = list(map(lambda n: int(n), fp.readline().strip().split(' ')))

	coins.sort(reverse=True)

	m_coins = []
	r_coins = coins
	while sum(m_coins) <= sum(r_coins):
		m_coins.append(r_coins.pop(0))
	print(len(m_coins))
		
