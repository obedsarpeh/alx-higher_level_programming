#!/usr/bin/python3
character = ""
for alphabet in range(97, 123):
    character = chr(alphabet)
    if character != 'e' and character != 'q':
        print(f"{character}".format(str(character)), end="")
