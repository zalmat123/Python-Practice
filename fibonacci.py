# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:12:06 2022

@author: fitsum
"""


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

n=10
print("Fibonacci sequence:")
for i in range(n):
    print(recur_fibo(i))
