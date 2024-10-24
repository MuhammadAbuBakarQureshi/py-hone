import numpy as np

'''
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
'''




'''             sort() function is used to sort ndarray
'''

arr = np.array([3, 11, 15, 20, 2, 5, 4])

print("\nSorting a integer array\n", np.sort(arr)) # sort() function returns copy of the original array


'''             You can also sort or any other data type
'''

arr = np.array(["banana", "chery", "apple"])

print("\n\nSorting a string array\n", np.sort(arr)) 


'''             sort a boolean array
'''

arr = np.array([True, False, True, True])

print("\n\nSorting a Boolean array\n", np.sort(arr))




'''             Sorting a 2-D array
'''

arr = np.array([[1, 3, 2], [6, 4, 5]])

print("\n\nSorting 2-Dimensional array\n", np.sort(arr))