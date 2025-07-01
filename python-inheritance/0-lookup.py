#!/usr/bin/python3

def lookup(obj):
    return dir(obj)


# Örnek test:
class MyClass:
    def __init__(self):
        self.value = 42

    def say_hi(self):
        return "Hi"

# Nesne oluştur
obj = MyClass()

# lookup fonksiyonunu kullan
print(lookup(obj))
