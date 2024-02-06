#!/usr/bin/python3
#""" The Shebang """
#def write_file(filename="", text=""):
#   with open(filename, mode='w', encoding="utf-8") as f:
#       data = f.write(text)
#       return data
#!/usr/bin/python3
"""Contains function read_file"""


def write_file(filename="", text=""):
    """writes a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='w', encoding="utf-8") as a_file:
        data = a_file.write(text)
        return data
