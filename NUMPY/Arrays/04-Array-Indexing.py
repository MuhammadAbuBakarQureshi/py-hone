import numpy as np

'''     Accessing 1-Dimensional Array
'''

arr = np.array([1, 3, 5, 7])

print(arr[3]) # 7



'''     Accessing 2-Dimensional Array
'''

arr = np.array([

        [1, 2, 3],
        [4, 5, 6]
    ]
)

print(arr[1, 2]) # 6




'''         Accessing 3-Dimensional Array
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

print(arr[1, 0, 2]) # 33

print(arr[-1, 1, -2]) # 202