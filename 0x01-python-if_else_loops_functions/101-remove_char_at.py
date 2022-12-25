#!/usr/bin/python3
def remove_char_at(str, n):
    n <= 0 or n > 0
    if len(str) > n:
        str = str[:n] + str[n + 1:]
    return str
