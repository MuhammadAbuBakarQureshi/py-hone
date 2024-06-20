def check_range(number):

    if number in range(3,6):

        print(number, "is in the range")
    else:

        print(number, "is not in the range")



number = int(input("Enter the number in the range from 3 to 6: "))

check_range(number)