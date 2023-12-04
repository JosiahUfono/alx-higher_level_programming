#!/usr/bin/python3
''' Defines a class checker '''


def is_kind_of_class(obj, a_class):
    '''Checks of obj is an instance of a_class or an inherited class

    Args
        obj: Object being verified.
        a_class: class being compared to obj.
        Return: True if obj is an instance of a_class class or
            inherits from same class, otherwise return False.'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
