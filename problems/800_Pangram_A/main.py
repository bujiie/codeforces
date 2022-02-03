#!/usr/bin/env python3

import fileinput

word_len = -1
word = None
with fileinput.input() as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            word_len = int(line)
        else:
            word = line

if word_len < 26:
    print("NO")
else:
    ans = "NO"
    letters = set()
    for c in list(word):
        letters.add(c.lower())
        if len(letters) >= 26:
            ans = "YES"
            break
    print(ans)
    
            

		
