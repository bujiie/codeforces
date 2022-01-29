#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    line = fp.readline().strip()[1:-1]
    if len(line) == 0:
        print(0)
    else:
       print(len(set(line.split(', '))))
