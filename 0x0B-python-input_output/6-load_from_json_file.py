#!/usr/bin/python3
'''a function that creates an Object from a “JSON file.'''
import json as j


def load_from_json_file(filename):
    '''a function that creates an Object from a “JSON file”.

        args:
            filename: File to be written to.
            '''
    with open(filename) as f:
        return (j.load(f))
