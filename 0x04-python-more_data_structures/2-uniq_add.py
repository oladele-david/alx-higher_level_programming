#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    new_list = set(my_list)
    for i in new_list:
        uniq_sum += i
    return uniq_sum
