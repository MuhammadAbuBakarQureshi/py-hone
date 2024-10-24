from numpy import random

'''
# The choice() method allows you to generate a random value based on an array of values.

# The choice() method takes an array as a parameter and randomly returns one of the values.
'''

array = [3, 12, 6, 2, 7, 23]

random_number = random.choice(array)

print("\nRandom number using choice method\n", random_number)



'''
The choice() method also allows you to return an array of values.

Add a size parameter to specify the shape of the array.
'''



'''            Generating 2-D array
'''

random_number = random.choice(array, size=(2, 2))

print("\n\nRandom 2-D array using choice method\n", random_number)