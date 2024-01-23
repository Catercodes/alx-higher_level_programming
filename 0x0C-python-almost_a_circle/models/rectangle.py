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
        self.integer_validator(value, "width")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        """getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ The setter for  height"""
        self.integer_validator(value, "height")
        if value <= 0:
            raise ValueError("height must > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter and Setter got x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter and  setter for Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The settert for Y"""

        self.integer_validator(value, "y")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def integer_validator(self, value, name):
        """ This validetor"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def area(self):
        """function  calculate the area of a rec"""
        return self.__width * self.__height

    def __str__(self):
        """ String Representation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
            f" - {self.__width}/{self.__height}"

    def display(self):
        """ Display using the # character"""
        row = self.__width * '#'
        for i in range(self.__height):
            print(row)
