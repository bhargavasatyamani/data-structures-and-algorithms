"""
THREE NUMBER SORT

You're given an array of integers and another array of three distinct integers. The first array is guaranteed 
to only contain integers that are in the second array, and the second array represents a desired order for the
integers in the first array. For example, a second array of [x, y, z] represents a desired order of
[x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.

Write a function that sorts the first array according to the desired order in
the second array.

The function should perform this in place (i.e., it should mutate the input
array), and it shouldn't use any auxiliary space (i.e., it should run with
constant space: <span>O(1)</span> space).

Note that the desired order won't necessarily be ascending or descending and
that the first array won't necessarily contain all three integers found in the
second array—it might only contain one or two.

Sample Input
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

Sample Output
[0, 0, 0, 1, 1, 1, -1, -1]
"""

def threeNumberSort_solution1(array, order):
    # This has time complexity of O(n*3)
	currentIdx = 0
	for x in order:
		swapped = True
		while swapped:
			swapped = False
			for i in range(currentIdx, len(array)-1):
				if array[i] == x:
					continue
				elif array[i+1] == x:
					array[i], array[i+1] = array[i+1], array[i]
					swapped = True
				else:
					continue
		for i in range(currentIdx, len(array)):
			if array[i] != x:
				currentIdx = i
				break
	
	return array





