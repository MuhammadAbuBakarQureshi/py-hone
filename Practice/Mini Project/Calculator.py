num1 = input("Enter first number : ")

operator = input("Enter the operator (+, -, *, /, %) : ")

num2 = input("Enter second number : ")

num1 = int(num1)

num2 = int(num2)

if operator == '+':

    sum = num1 + num2
    
    print("Result of addition of", num1, "and",  num2, "is :", sum)

elif operator == '-':

    subtract = num1 - num2
    
    print("Result of subtracting of", num1, "and",  num2, "is :", subtract)

elif operator == '*':

    multiply = num1 * num2
    
    print("Result of multiplication of", num1, "and",  num2, "is :", multiply)

elif operator == '/':

    divide = num1 / num2

    print("Result of Division of", num1, "and",  num2, "is :", divide)


elif operator == '%':

    modulo = num1 % num2

    print("Result of modulo of", num1, "and",  num2, "is :", modulo)

else:

    print("You have entered wrong operator")
