#!/usr/local/bin/python3

from FenwickTree.BIT import Fenwick1D
import random

base_array = [random.randint(0,100) for x in range(25)]

fenwick_tree_1d = Fenwick1D(base_array)