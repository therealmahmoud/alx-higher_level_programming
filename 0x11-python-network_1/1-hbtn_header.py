#!/usr/bin/python3
from urllib import request
import sys
"""script that takes in a URL,
sends a request to the URL and displays the value
"""

with request.urlopen(sys.argv[1]) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
