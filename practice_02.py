# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:44:16 2021
@author: fitsum

numpy is faster than list and is a fixed type.
numpy is faster read less byte of the memory
numpy utilizes a contiguous memory
SIMD=>  single instruction multiple data
Application of NumPy:
    mathematics (MATLAB Replacement)
    plotting
    backend
    machinelearning
"""
import numpy as np
a = np.array([2,3,4,5,6])
print(a)

b = np.array([[2,3],[3,4]])
print(b)
print(b.ndim)
print(b.shape)
print(a.dtype)