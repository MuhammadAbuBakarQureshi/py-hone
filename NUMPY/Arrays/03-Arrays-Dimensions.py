import numpy as np

'''     0 - Dimensional array
'''

arr = np.array(88)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     1 - Dimensional array
'''

arr = np.array([1, 2, 3])

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     2 - Dimensional array
'''

arr = np.array([

        [2, 4, 6],
        [1, 3, 5]
    ]
)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     3 - Dimensional array
'''

arr = np.array([

        [
            [10, 20, 30],
            [100, 200, 300]
        ],

        [
            [11, 22, 33],
            [101, 202, 303]
        ]
    ]
)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"





'''             Check the Dimensions of array using attribute "ndim"
'''

'''

    ndim attribute is used to get dimensions of the array

    as you can see, I have already used it in upper print functuions

'''




'''             Create an array using ndmin
'''

arr = np.array([1, 3, 4], ndmin = 4) # ndmin = 4 means now this array will be 4 dimwnsional 

print(arr)


'''             Check shape of the array
'''

arr = np.array(
       [
            [
                [1, 3, 4],
                [2, 4, 5]
            ],
            [
                [3, 5, 2],
                [6, 4, 2]
            ]
       ]
)

print(arr.shape)