# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:29:41 2021

@author: fitsum
"""

'''
Variable:
    a location in the memory that used to store some data or value
    they are given unique names to differentiate between different memory locations. the rules for writing a varaible name is the same as the rules for writting identifiers in python.
    we don't need to declare a variable before using it. In python, we simply assign a value to a variable and it will exist. we dont even have to declare the type of the variable. this is handled internally according to the type of value we assign to the variable.
'''
#Variables Assignments:
a=10
b=6.5
c="machine learning"
#multiple line
a,b,c=10,3,"ML"

#storage locations:

x =6
print(id(x))
print(id(a))
