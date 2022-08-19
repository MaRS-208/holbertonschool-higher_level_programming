#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
            (type(r)), (r), (r.decode('utf-8'))))
