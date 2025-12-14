#!/usr/bin/python3
"""Module for creating Square class with area calculation"""

class Square:
    """A class representing a square with a private size attribute."""
    
    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

