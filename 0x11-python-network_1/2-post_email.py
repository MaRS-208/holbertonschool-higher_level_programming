#!/usr/bin/python3
"""Write a Python script that takes in URL and an email, sends\
a POST request to the passed URL with the email as a parameter,\
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    
    from urllib import request, parse
    from sys import argv
    
    vl = {"email": argv[2]}
    dt = parse.urlencode(vl).encode('ascii')
    rq = request.Request(argv[1], dt)
    with request.urlopen(rq) as response:
        rs = response.read()
        print(rs.decode('utf-8'))
