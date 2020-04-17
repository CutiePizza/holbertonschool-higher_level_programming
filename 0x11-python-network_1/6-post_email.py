#!/usr/bin/python3
"""
Task five
"""
import requests
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]
        data = {"email": email}
        r = requests.post(url, data)
        print(r.text)
    except:
        pass
