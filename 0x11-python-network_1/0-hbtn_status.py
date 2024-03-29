#!/usr/bin/python3
from urllib import request
"""A script that fetches https://alx-intranet.hbtn.io/status
"""

with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    response = resp.read()
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
    print("\t- utf8 content:", response.decode())
