#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for key, valued in a_dictionary.items():
        if valued == value:
            to_del.append(key)
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
