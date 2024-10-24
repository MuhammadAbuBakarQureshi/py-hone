'''
FIRST METHOD (LONG)
'''

# def unique_List(numbers):

    
#     i = 0

#     condition = len(numbers)

#     while i < condition:


#         j = 0

#         check = numbers[i]

# # to check number with every element in list 

#         while j < condition:

#             if j == i:

#                 j += 1
        
#                 continue

#             elif check == numbers[j]:

#                 numbers.pop(j)

#                 condition = len(numbers)

#             j += 1

#         i += 1

#     print(numbers)


'''
SECOND METHOD (SHORT)

'''

def unique_List(numbers):
    
    new_list = []

    for value in numbers:
        
        if value not in new_list:
            
            new_list.append(value)

    print(new_list)

numbers = [0, 6, 2, 4, 5, 4, 5, 6, 3, 6]

unique_List(numbers)