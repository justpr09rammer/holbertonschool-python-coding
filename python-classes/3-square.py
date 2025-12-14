#!/usr/bin/python3
"""Square class with size validation and area calculation."""

class Square:
    """Square class to represent a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size  # Calls the setter to validate the size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to compute the area of the square."""
        return self.__size ** 2

