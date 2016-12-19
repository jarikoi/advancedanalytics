#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    return solve_it2(item_count,capacity,items)

def indent(i):
    return "******"*i

#[sum(a) for a in zip(*array)]
class result:
    def __init__(self,i):
        self.taken=[0]*i
        self.value=0
    
def returnRes(i):
        r=result(i)
        return r

def compute_o(i_c,k,items,taken,i):
    #which items where taken
    if (i_c == 0):
        return returnRes(i)
    else:
        # if we can fit this item
        if (items[0].weight <= k):
            # compute on rest of list
            o1=compute_o(i_c-1,k,items[1:],taken,i)
            #o2=items[0].value+compute_o(i_c-1,k-items[0].weight,items[1:],taken,i)
            o2=compute_o(i_c-1,k-items[0].weight,items[1:],taken,i)
            o2.value=o2.value+items[0].value
            print indent(i)+"i_c = " + str(i_c)
            print indent(i)+"items.len = " + str(len(items))
            print indent(i)+"o2 = " + str(o2.value)
            print indent(i)+"o1 = " + str(o1.value)
            if (o2.value > o1.value):
                o2.taken[items[0].index] = 1
                print indent(i)+"taken = " + str(o2.taken)
                return o2
            else:
                print indent(i)+"taken = " + str(o1.taken)
                return o1
        else:
            # if this item can not fit
            o=compute_o(i_c-1,k,items[1:],taken,i)
            return o
    

def solve_it2(item_count2,capacity2,items2):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    #taken will be modified by called function
    taken = [0]*len(items2)

    result = compute_o(item_count2,capacity2,items2,taken,item_count2)
    print "finaltaken = " + str(taken)
    # prepare the solution in the specified output format
    output_data = str(result.value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, result.taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

