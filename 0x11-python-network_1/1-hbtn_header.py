#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value
"""
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
