#!/usr/bin/python3
class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
