def count_vowels(input_string):

    vowels = {

        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0,
    }

    i = 0

    for i in range(i,len(input_string)):

        j = 0

        for j in vowels:

            if input_string[i].upper() == j.upper():

                vowels[j] += 1
                

    print(vowels)
    
input_string = input("Enter a string to check vowels init : ")

count_vowels(input_string)