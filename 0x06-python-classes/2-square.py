#!/usr/bin/python3

"""
Define a class square.
"""


class Square:
    """
    A class which the size attribute is private.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
