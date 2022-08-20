#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":

    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("""Body response:
\t- type: {}
\t- content: {}""".format((type(r.text)), (r.text)))
