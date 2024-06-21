def plaindrome_String(string):

    i = len(string) - 1

    for value in string:

        print(i)

        if value != string[i]:

            return False

        if i == (len(string)-1)/2:

            break

        i -= 1

    return True


string = input("Enter a string : ")

print(plaindrome_String(string))