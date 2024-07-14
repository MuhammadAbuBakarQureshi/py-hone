import numpy as np
from numpy import random

'''
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation()

'''


'''                 SHUFFLING ARRAY


The shuffle() method makes changes to the original array

'''

arr = np.array([1, 2, 3, 4])

random.shuffle(arr)

print("\nShuffling array\n", arr)




'''                 PERMUTATIONS OF THE ARRAY


The Permutaion() method does not change the original array

''' 

arr = np.array([1, 2, 3, 4])

print("\n\nPermutation of the array\n", random.permutation(arr))

