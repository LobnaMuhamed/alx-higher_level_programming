#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
