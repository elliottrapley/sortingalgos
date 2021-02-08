def selection_sort(array):
	index_length = range(0, len(array)-1) 

	for i in index_length:
		min_value = i # we assign the first index value to be the minimum value

		for j in range(i+1, len(array)): # iterate through all elements to the right of the minimum value
			if array[j] < array[min_value]:
				min_value = j

		if min_value != i: # if we find an item that is a lower value than the default, then we swap them.
			array[min_value], array[i] = array[i], array[min_value]

	return array 


ints = [1, 4, 5, 7, 9, 0, 3, 2, 10, 6, 8, 17, 12]

print(selection_sort(ints))

# Big O complexity for this algorithm is O(n^2). This is because it uses a nested loop.
# Selection sort is more effecient that bubble sort because we cut down the number of swaps required on each iteration.