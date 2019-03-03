#!/usr/bin/env python3

"""this function will return CountingDict which key is the
item to be count and value is the number key is counted"""

def CountList(arr):
    empty_dict = {}
    for i in arr:
        count = 0
        selected = i
        new_dict = dict.fromkeys([selected])
        for k in range(len(arr)):
            if arr[k] == selected:
                count += 1
            new_dict[selected] = count
        empty_dict.update(new_dict)
    return empty_dict
