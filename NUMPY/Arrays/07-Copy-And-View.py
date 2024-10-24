import numpy as np

'''

                                The Difference Between Copy and View


                                
1. The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

2. The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not 
affect the copy.

3. The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will 
affect the view.

'''




'''         Copy
'''

arr = np.array([1, 2, 3, 4, 5])

new_arr = arr.copy()

# Now if I change original array "arr" it will not affect the copy one "new-arr"

arr[0] = 23

print(arr) # original array

print(new_arr) # copy array




'''         View
'''

arr = np.array([1, 2, 3, 4, 5])

new_arr = arr.view()

# If I change original array "arr" it will change the view array "new-arr"

arr[0] = 23

print(arr) # original array

print(new_arr) # view array


# Now, if I change the view array "new-arr" it will change the original array "arr"

new_arr[0] = 1

print(arr) # original array

print(new_arr) # view array



'''         Copies owns the data, and view doesn't owns the data


Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.
'''


print(arr.base) # None

print(new_arr.base) # [1 2 3 4 5]



'''
The copy returns None.

The view returns the original array.
'''