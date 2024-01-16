#!/usr/bin/python3
""" The python command"""


class MyList(list):
    """ class of my list"""

    def print_sorted(self):
        """ prints sorts list"""
        print(sorted(self))
