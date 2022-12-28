#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list) - 1):
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
    return my_list[idx]
