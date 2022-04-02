# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:13:49 2022

@author: fitsum
"""

dictionary = {
    "name":"fitsum",
    "age":24,
    "weight":54
    }
print(dictionary)
print(dictionary["name"])
print(len(dictionary))
print(type(dictionary))
print(dictionary.get("name"))
print(dictionary.items())
print(dictionary.keys())

if "name" in dictionary:
  print("Yes, 'name' is one of the keys in the dictionary")