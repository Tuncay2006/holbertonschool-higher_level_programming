#!/usr/bin/python3
"""Sends a POST request to a URL with an email as parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Email verisini encode et
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # İstek oluştur
    req = urllib.request.Request(url, data=data)

    # Yanıtı oku ve yazdır
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
