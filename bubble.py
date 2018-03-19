#!/usr/bin/env python3
import random
import time

def bubble_sort(a):
	i = len(a) - 1
	flag = 1
	while flag == 1:
		flag = 0
		for j in range(i):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				flag = 1
		i -= 1
