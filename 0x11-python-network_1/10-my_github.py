#!/usr/bin/python3
"""Write Python script that takes your GitHub credentials (username\
and password) and uses the GitHub API to display your id"""


if __name__ == '__main__':

    import requests
    from sys import argv

    user = argv[1]
    pwd = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, pwd))
    print(r.json().get("id"))
