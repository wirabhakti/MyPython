#!/usr/bin/env python3


def insertion_sort(arr):
    selected_num = arr[0]
    for i in range(len(arr)):
        selected_num = arr[i+1]
        for i in arr[:selected_num]:

