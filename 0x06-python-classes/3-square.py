#!/usr/bin/python3
"""The Shebang """


class Square:
    """The square class """

    def __init__(self, size=0):
        """private attribute"""
        self.__size = size
        """ A TypeError"""
        if not isinstance(size, int):
            """raising Exceptions"""
            raise TypeError("size must be an integer")
        if size < 0:
            """ raising ValueErro Exception"""
            raise ValueError("size must be >= 0")

    def area(self):
        """ calculates  the area of square"""
        return self.__size ** 2
