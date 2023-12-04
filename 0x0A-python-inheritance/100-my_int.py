#!/usr/bin/python3
'''Defines class myInt.'''


class MyInt(int):
    '''Represents class MyInt which inherits the int class.'''

    def __eq__(self, arg):
        '''Overrides == with !=.
        arg: argument to be checked.'''
        return (self.real != arg)

    def __ne__(self, arg):
        '''Overrides != operator with ==.
        arg: argument to be checked.'''
        return (self.real == arg)
