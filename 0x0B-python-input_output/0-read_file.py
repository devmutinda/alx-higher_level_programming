#!/usr/bin/python3
"""
This module reads a text file and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
