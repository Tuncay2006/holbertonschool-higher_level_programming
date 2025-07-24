#!/usr/bin/python3
"""Function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: Object to add attribute to.
        name: Name of the new attribute.
        value: Value of the new attribute.

    Raises:
        TypeError: If the attribute can't be added.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
