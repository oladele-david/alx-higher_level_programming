#!/usr/bin/

def custom_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (count)
