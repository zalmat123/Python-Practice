# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:57:28 2021

@author: fitsum
"""

'''
Identation:
    programming language like c,c++, and java, use curly brace({}) to define block. but python uses indentation
    the block of the code starts with identation and ended with one unindented line
    generally for whitespace is used for indentation but tab is prefereable
    block of code(function/ condition / class)
    
'''
class rectangle:
    width,height =0,0
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def area(self):
        total = self.width * self.height
        return total
    def parameter(self):
        return 2*(self.width+self.height)

obj = rectangle(3,4)
print("Area = "+str(obj.area()))
print("parameter = "+str(obj.parameter()))

