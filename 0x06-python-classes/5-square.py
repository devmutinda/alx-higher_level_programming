#!/usr/bin/python3
"""This module defines a square class
"""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="" if j < self.__size - 1 else "\n")
