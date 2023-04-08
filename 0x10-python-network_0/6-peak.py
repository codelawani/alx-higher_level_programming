#!/usr/bin/python3
"""This script finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """finds peak"""
    listints = list_of_integers
    low = 0
    high = len(listints) - 1
    if high < 0:
        return None
    for i in range(low, high):
        mid = low + (high - low) // 2
        if (listints[mid] > listints[mid - 1]) and (listints[mid] > listints[mid + 1]):
            return listints[mid]
        elif listints[low] > listints[low + 1] and not listints[:low]:
            return listints[low]
        if listints[high] > listints[high - 1] and not listints[high + 1:]:
            return listints[high]
        elif listints[mid] > listints[mid + 1]:
            low = mid
        elif listints[mid] > listints[mid - 1]:
            high = mid
        else:
            high = mid
    return listints[i]
