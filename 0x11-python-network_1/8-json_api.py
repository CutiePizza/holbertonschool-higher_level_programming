#!/usr/bin/python3
"""
Task five
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except:
        q = ""

    values = {'q': q}
    r = requests.post(url, values)
    try:
        print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
