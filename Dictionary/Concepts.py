'''
It Stored data in key value form

'''

marks = {
    "Chemistry" : 84,
    "Maths" : 90
    }

print(marks["Chemistry"]) # Print Value using Print Fucntion



'''
Add new value

'''
marks["Physics"] = 86


print(marks) # print the whole Dictionary Including key and Value


# Print Values using loop

for score in marks:

    print(marks[score])