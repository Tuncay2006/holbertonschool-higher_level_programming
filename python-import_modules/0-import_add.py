#!/usr/bin/python3
# add_0.py dosyasından add fonksiyonunu getiriyoruz
from add_0 import add  # <--- add_0 burada sadece 1 kez geçiyor

a = 1
b = 2

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))


