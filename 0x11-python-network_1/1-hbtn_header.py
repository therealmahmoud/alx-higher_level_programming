#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value
"""
from urllib import request
import sys

req = request.Request(sys.argv[1])
with request.urlopen(req) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
