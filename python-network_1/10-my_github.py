#!/usr/bin/python3
"""Fetches your GitHub user ID using Basic Auth with personal access token"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        json_data = response.json()
        print(json_data.get("id"))
    else:
        print("None")
