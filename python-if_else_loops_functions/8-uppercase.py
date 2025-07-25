#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # küçük harf ise
            result += chr(ord(c) - 32)  # büyük harfe çevir
        else:
            result += c  # diğer karakterleri olduğu gibi ekle
    print("{}".format(result))
