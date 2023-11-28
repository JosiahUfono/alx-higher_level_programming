#!/usr/bin/python3
'''A class that defines a rectangle.'''


class Rectangle:
    '''This class defines propoerties of a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle.'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method for the ranctangle's width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Setter method for the rectangle's width.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method for height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''setter method for height of the rectangle'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the rectangle.'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Returns the perimeter of the rectangle.'''
        if (self.__width or self.__height) == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))
