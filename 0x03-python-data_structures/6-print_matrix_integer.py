#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   new = []
   for i in range (3):
       new.append([row[i] for row in matrix])
       print("{:d}".format(int(new[i])))
