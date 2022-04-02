# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:07:40 2021

@author: fitsum
"""
import time
from numpy import random
arr = random.randint(10, size=1000)
print(arr)
#current time 
pro_time = time.process_time()
print(f'pro_time:{pro_time}')
def partition(start, end, array):
	pivot_index = start
	pivot = array[pivot_index]
	while start < end:
		
		while start < len(array) and array[start] <= pivot:
			start += 1
		while array[end] > pivot:
			end -= 1
		
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	
	return end
	
def quick_sort(start, end, array):
	
	if (start < end):
		
		p = partition(start, end, array)
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		
quick_sort(0, len(arr) - 1, arr)

post_time = time.process_time()
print(f'Post_time:{post_time}')

print(f'Sorted array: {arr}')