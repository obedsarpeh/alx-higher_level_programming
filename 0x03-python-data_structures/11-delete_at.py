#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for idx in range(len(my_list)):
        if idx < 0 and idx > len(my_list):
            print("{:d}".format(my_list[idx]))
        else:
            print("{:d}".format(del my_list[idx]))
    return my_list[idx]
            
