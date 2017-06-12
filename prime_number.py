def prime(n):
	prime_numbers = []
	if n<2:
		print False
	else:
		state = True
		number=n+1
		for i in range(2,number):
			while state:
				if number%i==0:
					prime_numbers.append(i)
				else:
					pass
	print prime_numbers
prime(5)


					