#!/usr/bin/python3
"""Rectangle sınıfını tanımlayan modül."""


class Rectangle:
    """Bir dikdörtgeni tanımlayan sınıf."""

    def __init__(self, width=0, height=0):
        """Yeni dikdörtgeni başlatır."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Genişliği döndürür."""
        return self.__width

    @width.setter
    def width(self, value):
        """Genişliği ayarlarken kontrol yapar."""
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
        """Yüksekliği ayarlarken kontrol yapar."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Dikdörtgenin alanını döndürür."""
        return self.__width * self.__height

    def perimeter(self):
        """Dikdörtgenin çevresini döndürür.
        Eğer genişlik veya yükseklik 0 ise, çevre 0 olur.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Dikdörtgeni '#' ile çizer."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """eval() ile yeniden oluşturulabilir string döner."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Nesne silindiğinde mesaj yazdırır."""
        print("Bye rectangle...")
