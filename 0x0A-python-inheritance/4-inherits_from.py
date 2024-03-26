#!/usr/bin/python3

def inherits_from(obj, a_class):
    """ checking the instance"""
    if isinstance(obj, a_class):
        return True
    else:
        False
