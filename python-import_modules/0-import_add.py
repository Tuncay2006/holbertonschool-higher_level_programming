#!/usr/bin/python3
# add_0.py dosyasından add fonksiyonunu getiriyoruz
from add_0 import add

# a ve b değişkenlerini farklı satırlarda tanımlıyoruz
a = 1
b = 2

# Bu satırlar sadece dosya doğrudan çalıştırıldığında çalışacak
if __name__ == "__main__":
    # print fonksiyonu ile a + b = sonuç yazdırıyoruz
    print("{} + {} = {}".format(a, b, add(a, b)))

