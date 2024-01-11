#!/usr/bin/python3
""" Defining write_file function """


def write_file(filename="", text=""):
    """ write in utf file"""
    with open(filename, "w", encoding="utf-8") as conten:
        return conten.write(text)
