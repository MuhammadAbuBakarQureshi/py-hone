def reverse(string):

    index  = len(string)

    reverse_String = ""

    while index != 0:

        last_char = string[index - 1]

        reverse_String = reverse_String + last_char

        index -= 1

    return reverse_String


string = input("Enter string to reverse it : ")

print("Reverse string : " + reverse(string))