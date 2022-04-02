# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:39:02 2022

@author: fitsum
"""

list01 = [1,2,3,4]
print(len(list01))
for i in list01:
    print(i)
list01.append(3)
print("\n\n\n")
print(len(list01))
list01.sort()
for i in list01:
    print(i)


"""
Creation of List will be made in two ways:
    1. using assignment
    2. using list() function
"""
list02 = list([1,23,4])
print("list02")
print(list02)
print(list01)
print(type(list01))
"""
some common function:
    1. append()
    2. insert()
    3. remove()
    4. del()
    5. pop()
    6. len()
    7. type()
    8. sort()
    9. sorted()
    10. reverse()
    11. clear()
    12. copy()
    13.count()
    14. index()
    15.extend()
"""
list02.clear()
print(list02)
print(type(list02))
list02 = list01.copy()
print(list02)
print(type(list02))
list02.reverse()
print(list02)
print(list02.count(3))
print(list02.count(1))
list02.extend(list01)
print(list02)
list02.sort()
print(list02)
print(list02.index(3))
list02.insert(2,"fitsum mesfin")
print(list02)
