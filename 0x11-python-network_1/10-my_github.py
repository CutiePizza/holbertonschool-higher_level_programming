#!/usr/bin/python3
"""
Task 10
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        r = requests.get(
                'https://api.github.com/user',
                auth=requests.auth.HTTPBasicAuth(
                    username,
                    password
                    )
                )
        print(r.json()['id'])
    except:
        print("None")
