def count(string):

    upper_count = 0

    lower_count = 0

    index = len(string)

    while index != 0:

        if string[index-1].isupper():

            upper_count += 1

        elif string[index-1].islower():

            lower_count += 1

        index -= 1

    print("No. of Upper case characters : ", upper_count)

    print("No. of lower case characters : ", lower_count)


string = input("Enter the string : ")

count(string)