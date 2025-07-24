#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a method to print the list in sorted order without modifying it.
"""


class MyList(list):
    """A subclass of list that adds a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying the original list)."""
        print(sorted(self))
