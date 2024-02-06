#!/usr/bin/python3
""" The Shebang """
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding="utf-8") as f:
        data = f.write(text)
        return data
