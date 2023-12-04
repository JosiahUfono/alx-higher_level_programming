#!/usr/bin/python3
'''Defines a class checking function.'''


def is_same_class(obj, a_class):
    '''A function that verifys the type (instance) of a class.

    Args
        obj: Object being verified.
        a_class: class being compared to obj.
        Return: True if object is an instance of A_class,
            otherwise returns False.'''
    if type(obj) == a_class:
        return True
    else:
        return False
