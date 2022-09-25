#!/usr/bin/python3
"""
This script akes in a letter and sends a POST request to
"http://0.0.0.0:5000/search_user" with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        data = {'q': argv[1]}
    except as Exception:
        data = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data)

    print(req.json)