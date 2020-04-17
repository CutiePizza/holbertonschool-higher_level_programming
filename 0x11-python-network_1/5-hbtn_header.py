#!/usr/bin/python3
"""
Task five
"""
import requests
import sys


if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers["X-Request-Id"])
