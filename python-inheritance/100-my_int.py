#!/usr/bin/python3
"""Defines a rebel integer class MyInt."""


class MyInt(int):
    """MyInt is a subclass of int with inverted == and !=."""

    def __eq__(self, other):
        """Inverts the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality operator (!=)."""
        return super().__eq__(other)
