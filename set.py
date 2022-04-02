# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:38:18 2022

@author: fitsum
"""

set01 = {1,2,3,3,5,4}
set01.add("banana")
set02 ={"banana", "apple","orange","pineapple","lemon"}

#set01.remove("banana")

#set01.discard("apple")
set01.pop()

print(set01)
print(type(set01))
print(set01.intersection(set02))
print(set01.difference(set02))
print(set02.difference(set01))

for x in set01:
    print(x)
print(set01.union(set02))
#set01.intersection_update(set02)
set01.symmetric_difference_update(set02)
print(set01)
