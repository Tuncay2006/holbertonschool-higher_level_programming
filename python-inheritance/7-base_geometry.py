#!/usr/bin/python3
"""Defines BaseGeometry class."""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
