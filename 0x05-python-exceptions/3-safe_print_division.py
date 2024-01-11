#!/usr/bin/python3

'''
Args:
    a - dividend or numerator
    b - divisor or denominator
Return:
    return - quotient
'''


def safe_print_division(a, b):
    result = None
    try:
        result = a/b
    except ZeroDivisionError:
        return (None)
    finally:
        print("Inside result:{}".format(result))
    return (result)
