#!/usr/bin/python3
'''Defines a class Rectangle that inherits from BaseGeometry.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a Rectangle class inherited from BaseGeometry class.'''

    def __init__(self, width, height):
        '''Intialises a new Rectangle.

        Arg
            width: The width of the Rectangle (int).
            height: The height of the Rectangle (int).'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
