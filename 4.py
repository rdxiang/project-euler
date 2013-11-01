import math

for x in range(1, 100000):
	divisible = True
	for y in range (1. 20):
		if x % y != 0:
			divisible = False
	if divisible:
		print x
