import math

someNumber = 600851475143
candidates = range(2,int(math.sqrt(someNumber)))
primes = []

candidates = [candidate for candidate in candidates if someNumber%candidate is 0]

for candidate in candidates:
	isPrime = True
	for x in range( 2, int(math.sqrt(candidate))):
		if candidate % x == 0:
			isPrime = False
			break
	if isPrime:
        print(candidate)