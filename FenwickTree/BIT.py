#!/usr/local/bin/python3

fenwick_index = lambda x: x+1
update_parent_index  = lambda x: x + (x & -x)
sum_parent_index = lambda x: x - (x & -x)

class Fenwick1D(object):
    def __init__(self,data_array):
        self.data = data_array
        self.create_fenwick_tree()
    def create_fenwick_tree(self):
        self.fenwick_tree = [0 for x in range(len(self.data)+1)]
        for index,item in enumerate(self.data):
            self.update(index, item)
    def update(self, index, value):
        new_index = fenwick_index(index)
        while new_index<=len(self.data):
            self.fenwick_tree[new_index] += value
            new_index = update_parent_index(new_index)
    def calculate_first_n(self,n):
        ret_sum = 0
        new_index = n
        while new_index > 0:
            ret_sum += self.fenwick_tree[new_index]
            new_index = sum_parent_index(new_index)
        return ret_sum
    def check(self,n):
        if sum(self.data[:n]) != self.calculate_first_n(n):
            print(sum(self.data[:n]),'diff ',self.calculate_first_n(n))
            return False
        else:
            return True