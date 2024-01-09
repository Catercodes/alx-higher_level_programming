#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    prints the strings ' My name is <first_name> <last_name>'
    Args:
        first_name:first_name
        last_   name:last_name
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    return:
        None
    """

    if not isinstance(first_name, str):
        """ raising exception"""
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """ raising exception"""
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
