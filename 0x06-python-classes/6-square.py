#!/usr/bin/python3
"""The Shebang """


class Square:
    """The square class """

    def __init__(self, size=0, position=(0, 0)):
        """private attribute"""
        self.__size = size
        self.__position = position
        """ A TypeError"""
        if not isinstance(size, int):
            """raising Exceptions"""
            raise TypeError("size must be an integer")
        if size < 0:
            """ raising ValueErro Exception"""
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """property 'def size(self):' to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        """property setter"""
        if not isinstance(value, int):
            """Exceptions"""
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ calculates  the area of square"""
        return self.__size ** 2

    def my_print(self):
        """ This function prints square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * '#')

    @property
    def position(self):
        """ Private instance atrribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the size of the area"""
        return self.area ** 2

    def my_print(self):
        """ representing the coordinates by '#'"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
