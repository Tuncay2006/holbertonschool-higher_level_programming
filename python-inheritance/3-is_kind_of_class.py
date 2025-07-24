#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of a class
or an instance of a subclass of that class.
"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
