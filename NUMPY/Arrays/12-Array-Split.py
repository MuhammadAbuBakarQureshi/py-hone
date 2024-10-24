import numpy as np


'''         
                    SPLITTING

we use array_split() for splitting array, we pass array and number of splits
'''


'''         Splitting 1-Dimensional Array 
'''


arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = np.array_split(arr, 3)

print("\n", new_arr, "\n\n")



'''

Note: We also have the method split() available but it will not adjust the elements when elements are less in source array
for splitting like in example above, array_split() worked properly but split() would fail.

'''


print(new_arr[0]) # Print array at 0 index

print(new_arr[1]) # Print array at 1 index

print(new_arr[2]) # Print array at 2 index




'''         Splitting 2-Dimensional Array


    using axes
'''

arr = np.array(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]
            ]
)


split_arr = np.array_split(arr, 3, axis = 1) # Splitting row wise

print("\n\n", split_arr, "\n")





'''         
        An alternate solution is using hsplit() opposite of hstack()
'''


split_arr = np.hsplit(arr, 3)

print("\n\n", split_arr, "\n")




'''      Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
'''