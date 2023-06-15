#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    roman_num = 0
    if not isinstance(roman_string, str) and roman_string is None:
        return (0)
    for i in roman_string:
        if i in roman_i:     
            roman_num += roman_i[i]
    return (roman_num)
