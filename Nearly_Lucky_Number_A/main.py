#!/usr/bin/env python3

import fileinput
import re

with fileinput.input() as fp:
	n = fp.readline().strip()
	if len(re.findall(r'4|7',n)) in [4,7]:
		print('YES')
	else:
		print('NO')

		
