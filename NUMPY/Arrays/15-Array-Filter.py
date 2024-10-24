import numpy as np

'''
Getting some elements out of an existing array and creating a new array out of them is called filtering.



                        BOOLEAN INDEX LIST

A boolean index list is a list of booleans corresponding to indexes in the array.
'''


arr = np.array([3, 2, 5, 1])

filter = [True ,False, True, False]

new_arr = arr[filter] # Create an array from index 0 and 2

print("\nFilter array\n", new_arr)



'''
In the example above we hard-coded the True and False values, but the common use is to create a filter array, based on conditions.
'''


arr = np.array([3, 2, 5, 7, 12, 59, 25, 54, 23, 15])

filter_arr = []

for elements in arr:

    if elements < 20: # if elements are less than 20, set the value True otherwise False

        filter_arr.append(True)
    
    else:

        filter_arr.append(False)

new_arr = arr[filter_arr]

print("\n\nFilter array\n", new_arr)




'''         Filter even numbers from array
'''


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filter_arr = []

for elements in arr:

    if elements % 2 == 0:

        filter_arr.append(True)

    else:

        filter_arr.append(False)

print(filter_arr)

new_arr = arr[filter_arr]

print("\n\nFilter Even numbers\n", new_arr)



'''         Creating Array directly from the array
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filter_arr = arr % 2 == 0

new_arr = arr[filter_arr]

print("\n\nFilter even numbers directly\n", new_arr)