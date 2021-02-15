import time
import random

def bubble_sort(array):
	for i in range(len(array)):
		for j in range(len(array) -1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

	return array
				
ints = [1, 4, 5, 7, 9, 0, 3, 2, 10, 6, 8, 17, 12]

START = time.time()

print("Here is a list of integers that need to be sorted in accending order:", "\n", ints, "\n")
bubble_sort(ints)
print("Like magic, the list is now in order! We used Bubble Sort.", "\n", ints)

END = time.time()

print("\nIt took:", START - END, "seconds")


 # Big-O run-time complexity of this algorithm in the worst case is O(n^2). 


