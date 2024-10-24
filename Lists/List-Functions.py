
'''
append

Add new value in list
'''

marks = [89, 92, 70, 98, 42]

marks.append(94) 

print(marks) # [89, 92, 70, 98, 42, 94]


'''
insert

Add new value on the specific index

Syntax: list_name.insert(index, value)
'''

marks.insert(0, 76)

print(marks) # [76, 89, 92, 70, 98, 42, 94]


'''
in

check the value in the list
'''

print(99 in marks) # False

print(89 in marks) # True


'''
len

Length of the list
'''

print(len(marks))



'''
clear

Clear list
'''

marks.clear()

print(marks)