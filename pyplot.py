# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:54:20 2022

@author: fitsum
"""

import matplotlib.pyplot as plt
data = [1,10,20,5,15,6]
data.sort()
square = [number**2 for number in data]
data.sort()
plt.plot(data,square,'bv')
plt.title("Data")
plt.xlabel("numbers")
plt.ylabel("square")
plt.grid()
plt.show()