#!/usr/bin/python3
"""Contains inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if object obj is an
    instance of class a_class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

