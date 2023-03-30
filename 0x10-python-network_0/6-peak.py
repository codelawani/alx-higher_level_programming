#!/usr/bin/python3
"""This script"""


def find_peak(list_of_integers):
    """finds peak"""
    listints = list_of_integers
    mid = len(listints) // 2
    # check if there's a list or left or right ints
    if not listints or not listints[:mid] or not listints[mid + 1:]:
        return None
    # check possible peak
    if listints[mid] >= listints[mid + 1] and listints[mid] >= listints[mid - 1]:
        return listints[mid]
    # check left
    peak = find_peak(listints[:mid + 1])
    # check right
    if not peak:
        peak = find_peak(listints[mid:])
    return peak
