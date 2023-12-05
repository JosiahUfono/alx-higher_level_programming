#!/usr/bin/python3
''' a function that returns the
    JSON representation of an object.'''
import json as j


def to_json_string(my_obj):
    '''a function that returns the
        JSON representation of an object (string).

        arg:
            my_obj: argument to be serialised (passed as JSON)'''
    return (j.dumps(my_obj))
