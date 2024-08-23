#!/usr/bin/python3
"""
0-square.py

This is a module that seeks to find the size of a square
"""


class Square:

    """
    A class with a private instance attribute 'size'
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializes a private size attribute

        Args:
            size (int): The size of the square (optional, defaults to 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """
        Computes and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2

    def my_print(self):

        """
        Prints the square using the character '#'.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
