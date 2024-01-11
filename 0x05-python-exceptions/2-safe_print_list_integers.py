#!/usr/bin/python3
'''
Args:
    my_list: list of type int, string, etc.
    x: number of items in my_list to be printed
Return:
    return number of items printed
'''


def safe_print_list_integers(my_list=[], x=0):

    count = 0

    try:
        for idx in range(x):
            try:
#                integer_value = int(my_list[idx])
                print("{:d}".format(my_list[idx]), end="")
                count += 1
            except (TypeError, ValueError):
                pass
    finally:
        print()
    return (count)
