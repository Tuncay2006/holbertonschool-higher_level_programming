#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name (str): name of the value
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
