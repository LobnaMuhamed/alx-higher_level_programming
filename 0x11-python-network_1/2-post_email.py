#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = email.encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
