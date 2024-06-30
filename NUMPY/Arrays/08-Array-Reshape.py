import numpy as np

'''
The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
'''


'''         Reshape From 1-D to 2-D
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(4, 3) # 4 rows and 3 columns

# TIP: If you multiply rows and cloumns it will give the size of the "arr"

print("\nFrom 1-D to 2-D \n", new_arr)




'''         Reshape From 1-D to 3-D
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(2, 3, 2) # The outermost Dimension have 3 arrays, each with 2 elements

print("\nFrom 1-D to 2-D \n", new_arr)





'''

                                Can We Reshape Into any Shape?


Yes, as long as the elements required for reshaping are equal in both shapes.

We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as 
that would require 3x3 = 9 elements.

'''



'''         Returns copy or view?


The example below returns the original array, so it is a view.
'''

arr = np.array([1, 2, 3, 4])

print("\n\n", arr.reshape(2, 2).base)





'''

                        Unknown Dimension
                        
You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.

'''


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print("\n\n", arr.reshape(2, 2, -1))

# We can not pass -1 to more than one dimension.





'''                 Flattening the Arrays

Flattening arrays means converting multi-dimensional array to one dimensional array

'''


arr = np.array([[1, 2, 3], [4, 5, 6]])

print("\n\n", arr.reshape(-1))