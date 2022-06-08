#!/usr/bin/python3

def uniq_add(my_list=[]):
    added = []
    summ = 0
    for num in my_list:
        if num in added:
            continue
        else:
            summ += num
            added.append(num)
    return summ
