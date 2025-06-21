#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = []
    for num in my_list:
        if num not in unique_nums:
            unique_nums.append(num)
    total = 0
    for num in unique_nums:
        total += num
    return total
