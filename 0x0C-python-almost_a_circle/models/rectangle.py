#!/usr/bin/python3
"""
    class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Represents the standard for the Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializes a new rectangle class
        Args:
            width = width of rectangle
            height = height of rectangle
            x = x co-ordinate position of rectangle
            y = y co-ordinate position of rectangle
            id = unique id of rectangle
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set value x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set method for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for a in range(self.y)]
        for b in range(self.height):
            [print(" ", end="") for c in range(self.x)]
            [print("#", end="") for d in range(self.width)]
            print("")
