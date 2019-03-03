#!/usr/bin/env python3

"""
this function return sorteed array with selection sort algorithm
With Selection sort, we divide our input list / array into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted that make up the rest of the list. We first find the smallest element in the unsorted sublist and place it at the end of the sorted sublist. Thus, we are continuously grabbing the smallest unsorted element and placing it in sorted order in the sorted sublist. This process continues iteratively until the list is fully sorted
"""

import sys
import minnumarray

arr = eval(sys.argv[1])

def selectionsort(arr):
    new_lst = [] #create new empty list
    while arr:
        minval = minnumarray.returnmin(arr)
        new_lst.append(minval)
        arr.remove(minval)
    print(new_lst)

if __name__ == "__main__":
    selectionsort(arr)
