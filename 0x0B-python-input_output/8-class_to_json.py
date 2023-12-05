#!/usr/bin/python3
''' a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and
    boolean) for JSON serialization of an object:'''


def class_to_json(obj):
    '''Returns the dictionary represntation of a data structure.

    arg:
        obj: Data structure being returned. '''
    return (obj.__dict__)
