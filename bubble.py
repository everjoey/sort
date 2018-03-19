#!/usr/bin/env python3
import random
import cProfile

def bubble(a):
	i = len(a) - 1
	flag = 1
	while flag == 1:
		flag = 0
		for j in range(i):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				flag = 1
		i -= 1
	
if __name__ == '__main__':
	a = [random.randrange(1000) for i in range(1000)]
	print(a)
	cProfile.run('bubble(a)')
	print(a)
