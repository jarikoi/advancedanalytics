#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
timelimit=2400
optimal=1

def setNonOptimal():
    global optimal 
    optimal = 0

def setOptimal():
    global optimal 
    optimal = 1

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
    return " "*i


# Class for passing back resulting value and taken array from recursive function
class optResult:
    def __init__(self,i):
        self.taken=[0]*i
        self.value=0
#$        self.optimal=1 #1 is optimal, 0 is non optimal

#function for computing optimal solution
# number of i_c = items in current computattion
# k capacity
# items = items available, weight, value and index
# i = total number of items in original problem
def compute_o(i_c,k,items,i,start_time):
    #sys.stdout.write(str(i_c)+"|")
    #which items where taken
    if (i_c == 0):
        return optResult(i)
    elif (time.time()-start_time > timelimit):
        r= optResult(i)
        setNonOptimal()
        return r
    else:
        # if we can fit this item
        if (items[0].weight <= k):
            # compute on rest of list
            o1=compute_o(i_c-1,k,items[1:],i,start_time)
            o2=compute_o(i_c-1,k-items[0].weight,items[1:],i,start_time)
            o2.value=o2.value+items[0].value
            #print indent(i)+"i_c = " + str(i_c)
            #print indent(i)+"items.len = " + str(len(items))
            #print indent(i)+"o2 = " + str(o2.value)
            #print indent(i)+"o1 = " + str(o1.value)
            if (o2.value > o1.value):
                o2.taken[items[0].index] = 1
                #print indent(i)+"taken = " + str(o2.taken)
                return o2
            else:
                #print indent(i)+"taken = " + str(o1.taken)
                return o1
        else:
            # if this item can not fit
            o=compute_o(i_c-1,k,items[1:],i,start_time)
            return o
    

def solve_it2(item_count2,capacity2,items2):
    result = compute_o(item_count2,capacity2,items2,item_count2,time.time())
    #print "finaltaken = " + str(result.taken)
    # prepare the solution in the specified output format
    output_data = str(result.value) + ' ' + str(optimal) + '\n'
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

