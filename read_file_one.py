with open('my_numbers.txt') as file_object:
	numbers = file_object.read()
	print(numbers.strip())
