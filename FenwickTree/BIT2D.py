#!/usr/local/bin/python3

fenwick_index = lambda x: x+1
update_parent_index = lambda x: x + (x & -x)
sum_parent_index = lambda x: x - (x & -x)

class Fenwick2D(object):
    def __init__(self,data_array):
        self.data = data_array
        self.dimension = (len(data_array),len(data_array[0]))
        self.create_fenwick_tree()
    def create_fenwick_tree(self):
        self.fenwick_tree = [[0 for y in range(self.dimension[1]+1)] for x in range(self.dimension[0]+1)]
        for index_x in range(self.dimension[0]):
            for index_y in range(self.dimension[1]):
                item = self.data[index_x][index_y]
                self.update((index_x, index_y), item)
    def update(self, index, value):
        new_index_x = fenwick_index(index[0])
        new_index_x_list = []
        while new_index_x<=self.dimension[0]:
            new_index_x_list.append(new_index_x)
            new_index_x = update_parent_index(new_index_x)
        new_index_y = fenwick_index(index[1])
        new_index_y_list = []
        while new_index_y<=self.dimension[1]:
            new_index_y_list.append(new_index_y)
            new_index_y = update_parent_index(new_index_y)
        for new_index_x in new_index_x_list:
            for new_index_y in new_index_y_list:
                self.fenwick_tree[new_index_x][new_index_y] += value
    def calculate(self,index):
        new_index_x = index[0]
        new_index_x_list = []
        while new_index_x > 0:
            new_index_x_list.append(new_index_x)
            new_index_x = sum_parent_index(new_index_x)
        new_index_y = index[1]
        new_index_y_list = []
        while new_index_y > 0:
            new_index_y_list.append(new_index_y)
            new_index_y = sum_parent_index(new_index_y)
        ret_sum = 0
        for new_index_x in new_index_x_list:
            for new_index_y in new_index_y_list:
                ret_sum += self.fenwick_tree[new_index_x][new_index_y]
        return ret_sum
    def check(self,index):
        ans = sum([sum([y for y in x[:index[1]]])  for x in self.data[:index[0]]])
        if self.calculate(index) != ans:
            print(ans,' != ',self.calculate(index))
            return False
        return True