#!/usr/bin/python3
"""This script finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds peak"""
    listints = list_of_integers
    low = 0
    high = len(listints) - 1
    #check for empty list
    if high < 0:
        return None
    for i in range(low, high):
        mid = low + (high - low) // 2
        #check for peak at middle
        if ((listints[mid] > listints[mid - 1]) and
        (listints[mid] > listints[mid + 1])):
            return listints[mid]
        #check for peak at start of list
        elif (listints[low] > listints[low + 1] and
        not listints[:low]):
            return listints[low]
        #check for peak at end of list
        if (listints[high] > listints[high - 1] and
        not listints[high + 1:]):
            return listints[high]
        #reset start
        elif listints[mid] > listints[mid + 1]:
            low = mid
        #reset end
        elif listints[mid] > listints[mid - 1]:
            high = mid
        else:
            high = mid
    return listints[i]
