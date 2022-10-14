"""
This exercise stub and the test suite contain several enumerated constants.

For this challenge, enumerated constants are written as a NAME assigned to an 
arbitrary, but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    
    if (list_one == list_two):
        return EQUAL
    for i in range(len(list_one)):
        cut = list_one[i:i + len(list_two)]
        if cut == list_two:
            return SUPERLIST
    for f in range(len(list_two)):
        cut = list_two[f:f + len(list_one)]
        if cut == list_one:
            return SUBLIST
    return UNEQUAL