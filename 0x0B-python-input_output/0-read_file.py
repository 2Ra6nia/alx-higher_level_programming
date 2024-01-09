#!/usr/bin/python3
""" Defining  read_file function"""


def read_file(filename=""):
    """ read utf file """
    with open(filename, encoding='utf-8') as content:
        print(content.read(), end="")
