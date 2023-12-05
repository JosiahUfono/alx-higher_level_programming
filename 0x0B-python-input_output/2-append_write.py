#!/usr/bin/python3
'''A function that appends a string to the end of a text.'''


def append_write(filename="", text=""):
    '''Appends data to the end of a string.

    args:
        filename: The name of the file being written to.
        text: The string to be appended to filename file.'''
    with open(filename, mode="a", encoding="utf-8") as f:
        append_data = f.write(text)
        return (append_data)
