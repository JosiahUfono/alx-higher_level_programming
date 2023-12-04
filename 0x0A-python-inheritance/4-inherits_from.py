#!/usr/bin/python3
'''Defines an inherited class checking function.'''


def inherits_from(obj, a_class):
    '''Checks if an object is an inherited instance of a class.

    Args:
        obj: The object being checked.
        a_class: The class to be compared with.
    Return:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        otherwise False.'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
