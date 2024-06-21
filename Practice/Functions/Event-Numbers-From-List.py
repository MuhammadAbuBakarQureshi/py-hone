def print_even(numbers):
        
    new_List = []

    for values in numbers:

        if (values % 2 == 0):

            new_List.append(values)
            
    return new_List

numbers = [1, 2, 3, 4, 5, 6, 7 , 8, 9]

print(print_even(numbers))