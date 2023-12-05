#!/usr/bin/python3
'''Function that reads a UTF-8 text and prints its content.'''


def read_file(filename="my_file_0.txt"):
    '''Function that reads a UTF-8 encoded text and prints it
     to stdout.

     arg:
     filename: Name of the file to be read.'''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
