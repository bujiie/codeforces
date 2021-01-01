#!/usr/bin/env python3

import fileinput

test_cases = 0
tests = []
for i, line in enumerate(fileinput.input()):
	line = line.strip()

	if i == 0:
		test_cases = int(line)
	elif len(line) > 0:
		tests.append(list(map(lambda n: int(n), line.split(' '))))

problems = 0
for test in tests:
	if test.count(1) > 1:
		problems += 1

print(problems)
