#!/usr/bin/env python3

import fileinput

num_words = 0
words = []

for i, line in enumerate(fileinput.input()):
	line = line.strip()
	if i == 0:
		num_words = int(line)
	else:
		words.append(line)

for word in words:
	if len(word) > 10:
		print(f'{word[0]}{len(word)-2}{word[-1]}')	
	else:
		print(word)
