#digit_sought =115
numbers = [2, 4, 5, 9, 10, 15]

def binary_search(sorted_numbers, number_sought):
	low = 0
	high = len(sorted_numbers) -1
	middle = -1
	while (low < high):
		x = (high + low) / 2
		middle = int(x)
		print("Middle: " + str(middle))
		print("Low: " + str(low))
		print("High: " + str(high))
		if sorted_numbers[middle] == number_sought:
			return sorted_numbers[middle]
			#return("Found: " + str( sorted_numbers[middle]))
		elif sorted_numbers[middle] > number_sought:
			high = middle 
			#print("high=middle " + str(high))
		elif sorted_numbers[middle] < number_sought:
			if low == middle:
				low = middle + 1
			else:
				low = middle 
			#print("low=middle " + str(low))
		print ("------")
	print("Number not found")

#zahl = binary_search(numbers, digit_sought)
#print(zahl)


for i in range(1, 16):
	print(binary_search(numbers, i))

