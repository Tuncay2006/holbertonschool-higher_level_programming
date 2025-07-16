#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""

import requests

response = requests.get("https://intranet.hbtn.io/status")
content = response.text

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
