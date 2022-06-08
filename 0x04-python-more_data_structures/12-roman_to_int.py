#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {
        "I" : 1,
        "V" : 5,
        'X' : 10,
        "L" : 50,
        "C" : 100, 
        "D" : 500,
        "M" : 1000
    }
    number = 0
    prev = 10000
    for char in roman_string.upper():
        if char not in roman:
            return None
        num = roman[char]
        if prev < num:
            number = num - prev
        else:
            number += num
        prev = num
    return number
