import random

s = "\n"
"""list of random numbers"""
numbers = random.sample(range(90), 50)
"""sort numbers"""
numbers.sort()
"""list in STR"""
y = s.join(str(e) for e in numbers)
filename = 'my_numbers.txt'

with open(filename, 'w') as file_object:
	file_object.write(y)
