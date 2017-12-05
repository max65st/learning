digit_sought = 5
numbers = [2, 4, 5, 9, 10, 11, 15]

def binary_search(sorted_numbers, number_sought):
	low = sorted_numbers[0] 
	high = sorted_numbers[len(sorted_numbers)-1]
	print(low)
	print(high)
	
#	while (low <= high):
	middle = (high - low) / 2
	print(middle)
	if middle == number_sought:
		return middle
	elif middle < number_sought:
		low = middle
	elif middle > number_sought:
		high = middle
	else:
		return "Number not found"

binary_search(numbers, digit_sought)


