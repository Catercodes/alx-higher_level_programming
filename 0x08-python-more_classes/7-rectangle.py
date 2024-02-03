#!/usr/bin/python3
""" The Shebang for python"""


class Rectangle:
    """ The rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Public instantiation"""
        self.width = width    # Instance attribute
        self.height = height  # Instance attribute
        type(self).number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of a rectangle"""
        _perimeter = (self.__width + self.__height) * 2
        if self.__height == 0 or self.__width == 0:
            return 0
        return _perimeter

    def __str__(self):
        """representing character '#'"""
        if self.__width == 0 or self.__height == 0:
            # _hash = str(self.print_symbol)
            return ""
        return ('\n'.join([str(self.print_symbol)
                * self.__width] * self.__height))
        # for i in range(self.__height):
        #   row = (self.__width * '#' + '\n')
        #  rectangle = row * (self.__height - 1) + (self.__width * '#')
        # return rectangle

    def __repr__(self):
        """ return the string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        self.number_of_instances -= 1
