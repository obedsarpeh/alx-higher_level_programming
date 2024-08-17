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

        """
        Initializes a private size attribute

        Args:
            size (int): The size of the square (optional, defaults to 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
