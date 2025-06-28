#!/usr/bin/python3
"""Tanımlayıcı docstring: Rectangle sınıfını tanımlar."""


class Rectangle:
    """Dikdörtgeni tanımlayan sınıf."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Genişliği döndürür."""
        return self.__width

    @width.setter
    def width(self, value):
        """Genişliği ayarlar, doğrulama yapar."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Yüksekliği döndürür."""
        return self.__height

    @height.setter
    def height(self, value):
        """Yüksekliği ayarlar, doğrulama yapar."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
