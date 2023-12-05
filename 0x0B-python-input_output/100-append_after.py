#!/usr/bin/python3
'''A function that inserts a line of text to a file,
    after each line containing a specific string.'''


def append_after(filename="", search_string="", new_string=""):
    '''A function that inserts a line of text to a file,
    after each line containing a specific string.

    args:
        filename: Name of the file being written to.
        search_string: String being seached
        new_string: String being added
    '''
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
