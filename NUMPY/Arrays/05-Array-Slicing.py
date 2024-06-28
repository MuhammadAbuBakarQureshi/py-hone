import numpy as np

'''
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

'''


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#  The result includes the start index, but excludes the end index.

print(arr[3:6]) # [3, 4, 5]



'''     Negative slicing
'''


print(arr[-3:-1]) #[8, 9] 



'''     Step

Select every element from the array and step is equal to 3

'''


print(arr[::3]) # [0, 3, 6, 9]





'''         Slicing 2-Dimensional Array
'''


arr = np.array(
    [
        [2, 5, 3],
        [8, 6, 7]
    ]
)

'''

arr[ (row_range) 0 : 1 , (column_range) 2 : 3 ]

'''

print(arr[ 0 : 1, 2 : 3]) # [3]