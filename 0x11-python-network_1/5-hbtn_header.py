#!/usr/bin/python3
"""ends a request to the URL
displays the value of the variable X-Request-Id in the response header"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
