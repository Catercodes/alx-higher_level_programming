#!/usr/bin/python3
"""Contains function read_file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r', encoding="utf-8") as a_file:
        data = a_file.read()
        print(data, end="")
