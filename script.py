#!/usr/local/bin/python3

from FenwickTree.BIT import Fenwick1D
import random

n = 1000

base_array = [random.randint(0,100) for x in range(n)]

fenwick_tree_1d = Fenwick1D(base_array)


if all([fenwick_tree_1d.check(item) for item in range(n)]):
    print('all pass')