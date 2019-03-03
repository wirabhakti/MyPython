#!/usr/bin/env python3

"""this function will return CountingDict which key is the
item to be count and value is the number key is counted"""

import argparse, re  #import module needed for this operation


def returnToList(arr):
    regex = re.compile(r'(\d)+')
    return regex.findall(arr)

parser = argparse.ArgumentParser(prog='Counting item in list', description='This program will return dictionary with item as a key and item occurance in list as the value')
parser.add_argument('list_array', help="dont forget give double/single quote", type=returnToList)



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

if __name__ == '__main__':
    args = parser.parse_args()
    print(CountList(args.list_array))
