import random

s = "\n"
"""LIST of random numbers"""
numbers = random.sample(range(90), 10)
"""Sort numbers"""
numbers.sort()
"""List in STR"""
y = s.join(str(e) for e in numbers)
filename = 'my_numbers.txt'

with open(filename, 'w') as file_object:
	file_object.write(y)
