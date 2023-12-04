#!/usr/bin/python3
''' A class that inherits from list.'''


class MyList(list):
    '''A class which prints a list'''

    def print_sorted(self):
        '''prints a sorted list.'''
        print(sorted(self))
