#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square of size and position of the new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square of size with the # character."""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                for j in range(self.__size):
                    if j == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                    print("#", end="")
                print()
