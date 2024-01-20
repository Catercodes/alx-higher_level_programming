#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the constructor of the base class """
        super().__init__(id)

        """ Assign each argument to the right attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ Getter and Setter got x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ getter and  setter for Y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
