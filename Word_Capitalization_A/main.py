#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    line = fp.readline().strip()
    letters = list(line)
    letters[0] = letters[0].upper()
    print(''.join(letters))
		
