#!/usr/bin/env python3

"""this function return min number of an array"""

import sys

arr = eval(sys.argv[1])

def returnmin(arr):
    initialval = arr[0]
    for i in range(len(arr)):
        if arr[i] > initialval:
            continue
        else:
            initialval = arr[i]
    return initialval

if __name__ == "__main__":
    print(returnmin(arr))
