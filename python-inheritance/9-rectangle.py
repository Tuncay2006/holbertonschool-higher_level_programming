#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class to represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle object"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
