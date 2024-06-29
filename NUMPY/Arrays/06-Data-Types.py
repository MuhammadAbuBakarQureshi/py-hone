import numpy as np


'''     Finding Data types
'''

arr = np.array([2, 4])

print(arr.dtype) # int32

arr = np.array(["Apple", "Banana"])

print(arr.dtype)




'''     Creating Arrays With a Defined Data Type
'''

arr = np.array([4, 2, 6], dtype = 'int16')

print(arr.dtype) # int16



'''     Get size
'''

arr = np.array([1 ,3 , 5])

''' "itemsize" gives Each Element size in the array
'''
print(arr.itemsize) # 4


''' "size" gives How many elements in the array
'''
print(arr.size) # 3


'''     Float is 8 bytes
'''