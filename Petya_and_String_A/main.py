#!/usr/bin/env python3

import fileinput

l1 = None
l2 = None
with fileinput.input() as fp:
    l1 = fp.readline().strip().lower()
    l2 = fp.readline().strip().lower()

broke = False
for i in range(len(l1)):
    if ord(l1[i]) < ord(l2[i]):
        print('-1')
        broke = True
        break
    elif ord(l1[i]) > ord(l2[i]):
        print('1')
        broke = True
        break

if broke is not True:
    print('0')


		
