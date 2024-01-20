#!/usr/bin/python3
""" The python command """
from models.base import Base


class Rectangle(Base):
    """ THe Rectangle class inherited from base"""
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
        """ The setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ The setter for  height"""
        self.__height = value

    @property
    def x(self):
        """ Getter and Setter got x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x"""
        self.__x = value

    @property
    def y(self):
        """ getter and  setter for Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The settert for Y"""
        self.__y = value
