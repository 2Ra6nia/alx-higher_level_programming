#!/usr/bin/pyhon3
""" Defining append_write function"""


def append_write(filename="", text=""):
    """ append in utf file"""
    with open(filename, "a", encoding="utf-8") as content
         content.write(text)
