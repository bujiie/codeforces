#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp:
    username = fp.readline().strip()

    unique_chars = len(set(username))

    if unique_chars % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
