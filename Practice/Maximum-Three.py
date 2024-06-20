def max_of_two(num1, num2):

    if num1 > num2:

        return num1

    else:

        return num2
    
def max_of_three(num1, num2, num3):


    return max_of_two(num1, max_of_two(num2, num3))


print (max_of_three(9, 9, 9))