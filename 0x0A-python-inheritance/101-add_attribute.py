#!/usr/bin/python3
'''Defines a function that adds attributes to objects.'''


def add_attribute(obj, attribute, value):
    '''Add a new attribute to an object where possible.

    Arg
        obj: The object to add an attribute to.
        attribute: The name of the attribute to add to obj.
        value: The value of attribute.
    Raises TypeError: If the attribute can't be added.'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
