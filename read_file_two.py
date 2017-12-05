filename = 'my_numbers.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
print(lines)

numbers = []
for line in lines:
	numbers += line.rstrip()
print(lines)
numbers = [int(x) for x in numbers]

print(numbers)

