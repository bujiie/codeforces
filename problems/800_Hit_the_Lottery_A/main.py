#!/usr/bin/env python3

import fileinput

denom = [100, 20, 10, 5, 1]
with fileinput.input() as fp:
    total = int(fp.readline().strip())

    count = 0
    for d in denom:
        bills, remainder = total // d, total % d
        count += bills
        total = remainder
    print(count)

		
