#!/usr/bin/python3
a = (1, 2)
b = (1, 2)
print(a is b)
print(id(a))
print(id(b))


c = [1, 3]
d = [1, 3]
print(c is d)
print(id(c))
print(id(d))

'''
Tuples with similar objects have the same identity as well as value
while list don't have same value. so using 'is' to compare lists
returns false but returns true for tuples. "is" checks for Identity
which is the actual memery address assigned to the object whereas "=="
compares the values held by the varaibles. 
'''
