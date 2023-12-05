#!/usr/bin/python3
'''a function that writes an Object to a text file.'''
import json as j


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file,
    using a JSON representation:

        args:
            my_obj: JSON obj to be written to a file.
            filename: File to be written to.
        '''
    with open(filename, mode="w") as f:
        j.dump(my_obj, f)
