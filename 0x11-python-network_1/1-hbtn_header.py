#!/usr/bin/python3
"""Write a Python script that takes in URL, sends\
a request to the URL and displays the value of the\
X-Request-Id variable found in the header of the response"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
