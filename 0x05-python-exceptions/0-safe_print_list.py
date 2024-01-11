#!/usr/bin/python3
'''
Args:
    my_list: list of type int, string, etc.
    x: number of items in my_list to be printed
Return:
    return number of items printed
'''


def safe_print_list(my_list=[], x=0):

    count = 0

    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return (count)
