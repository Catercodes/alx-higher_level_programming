#!/usr/bin/python3
"""The Shebang """


class Square:
    """The square class """

    def __init__(self, size=0):
        """private attribute"""
        self.__self = size
        """ A TypeError"""
        if not isinstance(size, int):
            """raising Exceptions"""
            raise TypeError("size must be an integer")
        if size < 0:
            """ raising ValueErro Exception"""
            raise ValueError("size must be >= 0")
