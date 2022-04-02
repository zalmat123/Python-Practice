# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:15:24 2022

@author: fitsum
"""

tuple01 = (1,2,4,3)
"""
1. access the element of the tuple
0, 1, 2, 3, ... , len(tuple01)-1
"""
print(tuple01[2])
"""
2. update the value of each element
"""

print(tuple01[2:])
if 2 in tuple01:
    print("yes")
if 5 not in tuple01:
    print("Yes")

fruit = ("banana","orange","apple","pineapple");
yellow, green, *red = fruit
print(yellow)
print(red)
print(type(red))

for i in tuple01:
    print(i)
for i in range(len(tuple01)):
    print(tuple01[i])
i=0
while i < len(tuple01):
    print(tuple01[i])
    i+=1
    
print(fruit*2)