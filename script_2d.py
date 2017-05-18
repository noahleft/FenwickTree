#!/usr/local/bin/python3

from FenwickTree.BIT2D import Fenwick2D
import random

n = (100,100)

base_array = [[random.randint(0,100) for y in range(n[1])] for x in range(n[0])]

fenwick_tree_2d = Fenwick2D(base_array)

# for array in base_array:
#     print(array)

if all([fenwick_tree_2d.check((x,y)) for x in range(n[0]) for y in range(n[1])]):
    print('all pass')
