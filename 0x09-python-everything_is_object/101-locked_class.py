#!/usr/bin/python3
""" The python package """


class LockedClas:
    """Locked class that allow no dynamically creation of instances
    attributes except named first_nam"""
    __slots__ = ['first_name']
