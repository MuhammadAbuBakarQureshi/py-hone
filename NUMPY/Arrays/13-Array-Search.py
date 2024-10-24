import numpy as np

arr = np.array([1, 4, 2, 3, 4, 5])

search = np.where(arr == 4) # It will return tuple with indexes

print("\n",search)




'''         Find even and odd numbers from arr using where
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\n\nEven numbers from array")

for i in np.nditer(np.where(arr%2 == 0)):

    print(arr[i])
    
print("\n\nodd numbers from array")

for i in np.nditer(np.where(arr%2 == 1)):

    print(arr[i])
    




'''         Search Sorted

There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be 
inserted to maintain the search order.

'''


arr = np.array([6, 7, 8, 9])

search_Sorted = np.searchsorted(arr, 7) # 1

print("\n\n", search_Sorted, "\n")



'''     By default it will return left most index but we give the side = 'right' to return right most index
'''

search_Sorted = np.searchsorted(arr, 7, side = 'right')

print("\n\n", search_Sorted, "\n") # 2

'''     YOu can also pass array instead of one nunmber in searchsorted() function
'''