#!/usr/bin/python3
'''
Arg:
    value - integer to be printed
Return:
    returns - the value to be printed
'''


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
    except (TypeError,ValueError):
        return False

    return (value)
