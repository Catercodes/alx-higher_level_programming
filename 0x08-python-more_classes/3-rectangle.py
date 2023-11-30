#!/usr/bin/python3
""" The Shebang for python"""


class Rectangle:
    """ This is a rectangle classs """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width    # Instance attribute
        self.height = height  # Instance attribute

    def width(self):
        """ Private instance attribute 'width'"""
        return self.__width   # Private instance attribute

    @property
    def width(self):
        """ private instance to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """ raising exceptions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """ Private instance attribute 'width' to retrieve it"""
        return self.__height

    @property
    def height(self):
        """ property setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Raising Exception"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of a rectangle"""
        _perimeter = (self.width + self.height) * 2
        if self.height == 0 or self.width == 0:
            return 0
        return _perimeter

    def __str__(self):
        """representing character '#'"""
        if self.width == 0 or self.width == 0:
            return ""
        for i in range(self.__height):
            row = (self.__width * '#' + '\n')
            rectangle = row * (self.__height - 1) + (self.__width * '#')
            return rectangle
