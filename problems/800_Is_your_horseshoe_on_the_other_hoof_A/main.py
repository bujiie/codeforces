#!/usr/bin/env python3

import fileinput
from collections import defaultdict

with fileinput.input() as fp:
    colors=set([int(n) for n in fp.readline().strip().split(' ')])
    print(0 if len(colors) > 4 else 4-len(colors))



		
