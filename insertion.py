#!/usr/bin/env python3
import random
import time

def insertion(a):
	for i in range(1, len(a)):
		temp = a[i]
		j = i - 1
		while j >= 0 and a[j] > temp:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = temp

if __name__ == '__main__':
	a = [random.randrange(1000) for i in range(1000)]
	print(a)
	insertion(a)
	print(a)
