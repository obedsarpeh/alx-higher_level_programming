#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        # my_list = my_list[::-1]
        my_list.sort(reverse=True)
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
