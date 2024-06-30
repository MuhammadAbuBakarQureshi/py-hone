import numpy as np


'''                 IMPORTANT CONCEPTS


axis = 0 (Vertically (row wise))

axis = 1 (Horizontally (cloumn wise))

'''


'''     Concatenating 1-D arrays
'''

arr_1 = np.array([1, 2, 3, 4, 5])

arr_2 = np.array([6, 7, 8 ,9, 10])

arr = np.concatenate((arr_1, arr_2)) # There is just row wise concatenation in 1-Dimension array

print("1-Dimension arrays concatenation\n", arr)






'''     Concatenating 2-D arrays
'''

arr_1 = np.array(

    [
        [1, 2],
        [3, 4]
    ]
)

arr_2 = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)

# By default it will concatenate row wise

arr = np.concatenate((arr_1, arr_2), axis = 1) # Now, it will concatenate column wise 

print("\n\n2-Dimension arrays concatenation\n", arr)





'''     Concatenating 3-D array
'''

arr_1 = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

arr_2 = np.array(
    [
        [
            [9, 10],
            [11, 12]
        ],
        [
            [13, 14],
            [15, 16]
        ]
    ]
)

# By default it will concatenate row wise

arr = np.concatenate((arr_1, arr_2), axis = 2) # Now, it will concatenate column wise

print("\n\n3-Dimension array concatenation\n", arr)