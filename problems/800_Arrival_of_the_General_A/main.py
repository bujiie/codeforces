#!/usr/bin/env python3

import fileinput

S=[]
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            continue
        else:
            S=[int(n) for n in line.split(' ')]

mn, mx = min(S), max(S)

# we want the index of the min value that's closest
# to the right side of the list (it's destination).
mn_pos = len(S)-S[-1::-1].index(mn)-1
mx_pos = S.index(mx)

total=len(S)-1-mn_pos+mx_pos
# if the min and max value crossed paths, that means
# they shared one swap that brought them both closer
# to their destinations meaning we can reduce the
# move count by ONE.
if mn_pos < mx_pos:
    total -= 1

print(total)
