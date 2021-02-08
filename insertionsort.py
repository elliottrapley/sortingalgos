def insertion_sort(array):
	index_length = range(1, len(array))

	for i in index_length:
		value_to_sort = array[i] # store the value to sort as a variable. 

		while array[i-1] > value_to_sort and i > 0: # while loop to compare the value to the value on its left. 
			array[i], array[i-1] = array[i-1], array[i]
			i = i - 1 # go to the next item to the right. 

	return array

ints = [1, 4, 5, 7, 9, 0, 3, 2, 10, 6, 8, 17, 12]

print(insertion_sort(ints))