#!/usr/bin/env python3
import random
import cProfile

if __name__ == '__main__':
	a = [random.randrange(1000) for i in range(1000)]
	print(a)
	cProfile.run('bubble(a)')
	print(a)
