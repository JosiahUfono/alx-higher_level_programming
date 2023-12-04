#!/usr/bin/python3
'''Defines a Square class which inherits from Rectangle superclass.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents a square.'''

    def __init__(self, size):
        '''Initialises a new square.

        Arg:
            size: The size of the new square.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
