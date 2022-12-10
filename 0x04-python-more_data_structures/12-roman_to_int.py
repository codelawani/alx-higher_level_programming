#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_dict = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}
    nums = []
    for char in roman_string:
        for k, v in list(roman_dict.items()):
            if char == k:
                nums.append(v)
    number = 0
    num_of_nums = len(nums)
    for i in range(num_of_nums):
        if i != num_of_nums - 1:
            j = i + 1
            if nums[i] < nums[j]:
                nums[i] = -nums[i]
        number += nums[i]
    return number
