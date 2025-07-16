#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib only"""

from urllib import request

url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
