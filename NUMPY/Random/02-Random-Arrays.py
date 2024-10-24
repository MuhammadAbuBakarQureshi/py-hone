from numpy import random

# randint() method takes size prameter where you can define shape of array


'''         Genertaing 1-D array
'''

random_array = random.randint(100, size = (5)) # 5 random numbers from 0 to 100

print("\nRandom 1-D array using randint\n", random_array)



'''         Generating 2-D array
'''

random_array = random.randint(100, size = (3, 5))  # 3 rows and 5 columns random array from 0 to 100

print("\n\nRandom 2-D array using randint\n", random_array)





# rand() methods allow you to specify the shape of the array


'''         Generating 1-D array
'''

random_array = random.rand(5) # 5 random numbers between 0 and 1

print("\n\nRandom 1-D array using rand\n", random_array)



'''         Generating 2-D array
'''

random_array = random.rand(3, 5) # 3 rows and 5 columns random array between 0 and 1

print("\n\nRandom 2-D array using rand\n", random_array)