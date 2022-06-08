#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None) or len(a_dictionary) < 1:
        return None
    highest = float('-inf')
    highkey = None
    for key in a_dictionary:
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
            highkey = key
    return highkey
