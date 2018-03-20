#!/usr/bin/env python3
import random
import cProfile

def selection(a):
	for i in range(0, len(a) - 1):
		min_val_index = i
		for j in range(i + 1, len(a)):
			if a[j] < a[min_val_index]:
				min_val_index = j
		a[i], a[min_val_index] = a[min_val_index], a[i]

if __name__ == '__main__':
	a = [random.randrange(1000) for i in range(1000)]
	print(a)
	cProfile.run('selection(a)')
	print(a)
