with open('my_numbers.txt') as file_object:
	"""reads content of my_numbers & stores it as one long str"""
	numbers = file_object.read()
	"""Ausgabe ohne Blank line am Ende"""
	print(numbers.strip())
