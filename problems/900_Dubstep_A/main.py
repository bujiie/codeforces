#!/usr/bin/env python3

import fileinput
import re

with fileinput.input() as fp:
	sound = fp.readline().strip()
	trimmed = re.sub(r'^((WUB)+)?|((WUB)+)?$', "", sound)
	print(re.sub(r'(WUB)+', ' ', trimmed))

		
