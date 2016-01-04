import math

def validate_numbers(numlist):
	size = len(numlist)
	try:
		return set(numlist) == generate_valid_set(size) and check_if_size_is_valid(size)
	except TypeError: 
		return False

def generate_valid_set(size):
	return set(range(1, size + 1))

def check_if_size_is_valid(size):
	return size**0.5 % 1 == 0 and size >= 4

