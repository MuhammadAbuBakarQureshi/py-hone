import numpy as np

'''     0 - Dimensional array
'''

arr_0_dm = 88

arr = np.array(arr_0_dm)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     1 - Dimensional array
'''

arr_1_dm = [1, 2, 3]

arr = np.array(arr_1_dm)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     2 - Dimensional array
'''

arr_2_dm = [
        [2, 4, 6],
        [1, 3, 5]
    ]

arr = np.array(arr_2_dm)

print(arr.ndim, "Dimensional array \n", arr, "\n") # arr.ndim tells the dimension of the "arr"



'''     3 - Dimensional array
'''

arr_3_dm = [

        [
            [10, 20, 30],
            [100, 200, 300]
        ],

        [
            [11, 22, 33],
            [101, 202, 303]
        ]
    ]

arr = np.array(arr_3_dm)

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