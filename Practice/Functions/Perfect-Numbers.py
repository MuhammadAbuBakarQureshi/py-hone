'''
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently,
a perfect number is a number that is half the sum of all of its positive divisors (including itself).

'''


'''
FIRST METHOD (LONG)

'''

# def perfect_Number(number):

#     divisors = []

#     total = 0

#     if number >= 0: # If it is positive

#         for i in range(1, number): # Finding Divisors

#             if number % i == 0:

#                 divisors.append(i)
    
#             # Total of the divisors
        
#         for i in divisors:

#             total += i

#         if total == number:

#             total += number

#             half = total / 2

#             if half == number:
                
#                 return True
    
#     return False


'''
SECOND METHOD (SHORT)

'''

def perfect_Number(number):

    sum = 0

    for i in range(1, number):

        if number % i == 0:

            sum += i

    return sum == number

number = int(input("Enter a number : "))

print(perfect_Number(number))