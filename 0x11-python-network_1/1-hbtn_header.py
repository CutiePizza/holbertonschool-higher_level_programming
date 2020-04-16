#!/usr/bin/python3
"""
Task two
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        the_page = response.info()["X-Request-Id"]
        print(the_page)
