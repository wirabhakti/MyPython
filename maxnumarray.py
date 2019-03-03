#!/usr/bin/env python3
"""this funtion return maximum number of an array"""

import sys

arr = eval(sys.argv[1])

def returnmax(arr):
    initialval = 0
    for i in range(len(arr)):
        if arr[i] > initialval:
            initialval = arr[i]
    print(initialval)

if __name__ == "__main__":
    returnmax(arr)
