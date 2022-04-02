# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 08:51:19 2022

@author: fitsum
"""
import math
import numpy as np

print("-------Introduction to numpy-------")
a = np.array([1,2,3,4])
print(a)
print("Dimension of the array: ", a.ndim)
print("Shape of the array: ",a.shape)
print("Length of the array: ",len(a))



#The function that used to create the array
print("\n\n")
print("-------creating array using function-------")
b = np.arange(10)
print(b)

print("Dimension of the array: ", b.ndim)
print("Shape of the array: ",b.shape)
print("Length of the array: ",len(b))
print("\n\n")


print("-------numpy arange-------")
c = np.arange(1,10,2)
print(c)
print("Dimension of the array: ", c.ndim)
print("Shape of the array: ",c.shape)
print("Length of the array: ",len(c))
print("\n\n")


print("-------numpy linespace-------")
#numpy linespace is used to generate tuples
d = np.linspace(2.0, 3.0, num=10, dtype=float,endpoint=True,retstep=True)
print(d)
print("\n\n")

print("-------matrics------")
a = np.ones((2,3))
b = np.zeros((3,3))
c = np.eye(3)
d = np.diag([1,2,3,4,5,6])
print(b)
print(a)
print(c)
print(d)
print("\n\n")

print("-------Random------")
a = np.random.randn(10)
for i in range(len(a)):
    print(int(1000*a[i]))
    
print("\n\n")