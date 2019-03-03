#!/usr/bin/env python3

"""This function will sort dictionary by its values
   and retun selected item from sorted dict
"""

def returnminDict(_dct):
    dict_items = _dct.items()
    list_items = list(dict_items)
    init_items = list_items[0]
    for i in range(len(list_items)):
        if list_items[i][1] > init_items[1]:
            continue
        else:
            init_items = list_items[i]
    return init_items



def selectDictSort(_dct):
    new_dict = {}
    while _dct:
        mindict = returnminDict(_dct)
        new_dict.update(dict((mindict,)))
        _dct.pop(mindict[0])
    return new_dict

def returnItemSelection(_dct, n):
    sorteddict = selectDictSort(_dct)
    listsortDict = list(sorteddict.items())
    return listsortDict[n - 1]
