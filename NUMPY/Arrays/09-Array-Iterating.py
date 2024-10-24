import numpy as np


'''         Iterating 1-D array
'''

arr = np.array([1, 2, 3, 4, 5, 6])

for value in arr:

    print(value)




'''         Iterating 2-D array
'''

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for value in arr:

    print(value)


'''
To return the actual values, the scalars, we have to iterate the arrays in each dimension.
'''

for i in arr: #  "i" take a row

    for j in i:  # "j" take elements from that row

        print(j)





'''         Iterating 3-D array
'''

arr = np.array([
                    [
                        [1, 2, 3],
                        [4, 5, 6]
                    ],

                    [
                        [7, 8, 9],
                        [10, 11, 12]
                    ]
                ]
)


# for i in arr:

#     for j in i:

#         for k in j:

#             print(k)



'''         Using nditer() function to iterate from arrays easily as compared to for loop
'''


for i in np.nditer(arr):

    print(i)







'''         Iterating array with different data types
'''

for i in np.nditer(arr, flags = ['buffered'], op_dtypes = 'S' ):

    print(i) # Now, it will print as string value instead of integer





'''         If you want to print the index with values then we use "ndenumerate()" function instead of "nditer()"        
'''

for index, value in np.ndenumerate(arr):

    print(index, value)






'''         Iterating with different step size
'''

arr = np.array([

            [1, 2, 3, 4, 5], 
    
            [6, 7, 8, 9, 10]
            ]
)

for value in np.nditer(arr[:,::2]):

    print(value)
