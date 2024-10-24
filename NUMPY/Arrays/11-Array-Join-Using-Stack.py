import numpy as np


'''                                 JOINING ARRAY USING STACK

Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis.
If axis is not explicitly passed it is taken as 0.

'''


arr_1 = np.array([1, 2, 3])

arr_2 = np.array([4, 5, 6])

arr = np.stack((arr_1, arr_2), axis = 1)

print(arr)




'''         Stacking along rows
'''

arr_1 = np.array([1, 2, 3])

arr_2 = np.array([4, 5, 6])

arr = np.hstack((arr_1, arr_2))

print("\n\nStacking along arrays\n", arr)




'''         Stacking along cloumns
'''

arr_1 = np.array([1, 2, 3])

arr_2 = np.array([4, 5, 6])

arr = np.vstack((arr_1, arr_2))

print("\n\nStacking along columns\n", arr)




'''         Stacking along height(depth)
'''

arr_1 = np.array([1, 2, 3])

arr_2 = np.array([4, 5, 6])

arr = np.dstack((arr_1, arr_2))

print("\n\nStacking along height(depth)\n", arr)







'''             Stacking 2-Dimensional arrays
'''


arr_1 = np.array(
                
                [
                    [1, 2, 3],
                    [4, 5, 6]
                ]
)

arr_2 = np.array(
                
                [
                    [7, 8, 9],
                    [10, 11, 12]
                ]
)

# Row Stack

arr = np.hstack((arr_1, arr_2))

print("\n\nStacking 2-Dimensional array row wise\n", arr)

# Column Stack

arr = np.vstack((arr_1, arr_2))

print("\n\nStacking 2-Dimensional array column wise\n", arr)

# Depth Stack

arr = np.dstack((arr_1, arr_2))

print("\n\nStacking 2-Dimensional array depth wise\n", arr)






'''             Stacing 3-Dimensional arrays
'''


arr_1 = np.array(
                [
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

arr_2 = np.array(
                [
                    [
                        [13, 14, 15],
                        [16, 17, 18]
                    ],

                    [
                        [19, 20, 21],
                        [22, 23, 24]
                    ]
                ]
)


# Row Stack

arr = np.hstack((arr_1, arr_2))

print("\n\nStacking 3-Dimensional Array row wise\n", arr)

# Column Stack

arr = np.vstack((arr_1, arr_2))

print("\n\nStacking 3-Dimensional Array cloumn wise\n", arr)

# Depth Stack

arr = np.dstack((arr_1, arr_2))

print("\n\nStacking 3-Dimensional Array depth wise\n", arr)