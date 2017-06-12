def prime_number(n):
	"""
	this function takes in a number then generates
	all the prime numbers in the range of that number
	and append to a list which is the output
	"""
	primes = []
	if n<2:
		return False

	else:
		for prime in range(2, n):
		    for b in range(2, prime):
		        if (prime % b == 0):
		            break
		    else:
		        primes.append(prime)

		return primes