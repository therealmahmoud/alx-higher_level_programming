#!/usr/bin/python3
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    response = resp.read()
    print("Body response:")
    print("- type:", type(response))
    print("- content:", response)
    print("- utf8 content:", response.decode())