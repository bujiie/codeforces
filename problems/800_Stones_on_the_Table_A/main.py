#!/usr/bin/env python3

import fileinput

with fileinput.input() as fp: 
    num_stones = int(fp.readline().strip())
    stones = list(fp.readline().strip())

    prev_stone = None
    remove_count = 0	
    for stone in stones:
        if prev_stone is None:
            prev_stone = stone
            continue
        
        if stone == prev_stone:
            remove_count += 1
        prev_stone = stone

    print(remove_count)
    	
