#!/usr/bin/python3
'''A function that writes text to a file and counts the characters.'''


def write_file(filename="", text=""):
    '''Writes a string to a file.

    args:
        filename: File containing string to be written to.
        text: String written to filename file.'''
    with open(filename, mode='w', encoding="utf-8") as f:
        write_data = f.write(text)
        return (write_data)
