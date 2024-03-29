#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value
"""
from urllib import request
import sys

if __name__ == '__main __':
    url = sys.argv[1]
    request = request.Request(url)
    with request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
