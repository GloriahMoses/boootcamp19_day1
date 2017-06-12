import unittest
from temp_converter import convert_celcius_to_farenheight

class TempConverterTest(unittest.Testcase):
	#given temp in celcius = correct value in F
	#data type for input
	# throes an exception error when data type is incorrect
	#check for null values -> throw an error
	"""
		F = C* 9/5 + 32
	"""
	def test_celsis_is_converted_to_farenheight():
		actual = convert_celcius_to_farenheight(10)
		expected = 50
		self.assertEqual(actual, expected,
			'Celcius shold convert to correct Farenheight' )
		self.assertEqual(convert_celcius_to_farenheight(20))