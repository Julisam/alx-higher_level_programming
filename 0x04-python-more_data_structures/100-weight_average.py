#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    prod = sum([a * b for a, b in my_list])
    sumw = sum([b for a, b in my_list])
    return prod / sumw
