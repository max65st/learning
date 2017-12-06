digit_sought = 2 
numbers = [2, 4, 5, 9, 10, 15]

def binary_search(sorted_numbers, number_sought):
	low = 0
	high = len(sorted_numbers)
	x = (high - low) / 2
	middle = int(x)
	while (low <= high):
		x = (high - low) / 2
		middle = int(x)
		print("Middle: " + str(middle))
		if sorted_numbers[middle] == number_sought:
			print(sorted_numbers[middle])
		elif sorted_numbers[middle] < number_sought:
			low = middle
			return low
			print("low=middle " + str(low))
		elif sorted_numbers[middle] > number_sought:
			high = middle
			return high
			print("high=middle " + str(high))
		else:
			print("Number not found")

binary_search(numbers, digit_sought)


