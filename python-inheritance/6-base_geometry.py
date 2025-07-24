#!/usr/bin/python3
"""
Module that defines BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """BaseGeometry class with area method that raises an Exception."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
