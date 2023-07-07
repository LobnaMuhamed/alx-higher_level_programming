#!/usr/bin/python3
""" prevent user from dynamically creating new instaince atrr """


class LockedClass:
    """ prevent user from dynamically creating new instaince atrr """
    __slots__ = ['first_name']
