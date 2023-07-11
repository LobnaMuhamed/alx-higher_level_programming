#!/usr/bin/python3

""" class myList that inherits from list """


class MyList(list):

    """ print the list but sorted """
    def print_sorted(self):
        print(sorted(self))
