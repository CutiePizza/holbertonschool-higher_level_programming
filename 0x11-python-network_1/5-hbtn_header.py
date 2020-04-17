#!/usr/bin/python3
"""
Task five
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print(r.headers["X-Request-Id"])
