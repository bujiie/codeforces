#!/usr/bin/env python3

import fileinput
import re


with fileinput.input() as fp:
    word = fp.readline().strip()

    w_len = len(word)
    u_len = len(re.findall(r'[A-Z]',word))
    l_len = w_len - u_len

    if u_len <= l_len:
        print(word.lower())
    else:
        print(word.upper())
    
		
