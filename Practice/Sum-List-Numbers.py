'''
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''

def list_sum(numbers):

    sum = 0

    for values in numbers:

        sum += values
    
    return sum
    

numbers  = [8, 2, 3, 0, 7]

print(list_sum(numbers))