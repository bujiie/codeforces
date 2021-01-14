#!/usr/bin/env python3

import fileinput

participants = None
place = None
scores = []
for i, line in enumerate(fileinput.input()):
	line = line.strip()

	if i == 0:
		[participants, place] = list(map(lambda n: int(n), line.split(' ')))
	elif len(line) > 0:
		scores = list(map(lambda n: int(n), line.split(' ')))
		scores.sort(reverse=True)

threshhold = scores[place-1]

c = 0
for score in scores:
	if score > 0 and score >= threshhold:
		c += 1

print(c)
