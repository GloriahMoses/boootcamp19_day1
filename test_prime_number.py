import unittest
from prime_number2 import prime_number

class Prime_numberTest(unittest.TestCase):
	
	"""
	this class contains test_cases for the the function 
	prime_number
	"""
	
	#checking output
	def test_prime_number(self):
		expected = [2, 3, 5]
		self.assertEqual( prime_number(7),expected)

	#check if ouput is a list
	def test_type(self):
		expected = [2, 3, 5]
		self.assertIsInstance(expected, list)

	def test_check_start_point(self):
		self.assertNotIn( 1, prime_number(7))

	#check for number below 2 and return false
	def test_no_less_than_two(self):
		result =   prime_number(1)
		self.assertFalse(result)

	#check for negative numbers
	def test_negative_number(self):
		result =  prime_number(-7)
		self.assertFalse(result)
		
	#checking for list contents
	def test_n_as_int(self):
		expected = [2, 3, 5]
		for i in expected:
			self.assertIsInstance(i, int )


if __name__ == '__main__':
	unittest.main()