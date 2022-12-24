#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("{}".format('0' + str(number)), end=", ")
#    elif number >= 10 and number <= 99:
#       if number == 99:
#            break;
    elif number >= 10 and number <= 99:
        print("{}".format(number), end='\n' if number == 99 else ", ")
