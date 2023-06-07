#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ldgt = number % 10
    if ldgt > 5:
        print(f"Last digit of {number} is {ldgt} and is greater than 5")
    elif ldgt == 0:
        print(f"Last digit of {number} is {ldgt} and is 0")
    elif ldgt > 0 and ldgt < 6:
        print(f"Last digit of {number} is {ldgt} and is less than 6 and not 0")
elif number < 0:
    ldgt = ((number * -1) % 10) * -1
    print(f"Last digit of {number} is {ldgt} and is less than 6 and not 0")
