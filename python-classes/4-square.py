#!/usr/bin/python3
"""Square class with size validation, area calculation, and print functionality."""

class Square:
    """A class to define a square and perform operations on it."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
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
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

