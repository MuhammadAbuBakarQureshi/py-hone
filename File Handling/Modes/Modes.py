'''
    r+

open for reading and writing. The stream is positioned at the beginning of the file.
'''

# file = open("File Handling/Modes/mode_demo.txt", "r+")

# file.write("txt file") # I can write in this file

# print(file.read()) # I can also read from this file

# file.close()

'''

    w+

open for reading and writing. The file is created if it does not exit, otherwise it truncated.
The stream is positioned at the beginning of the file
'''

# file = open("File Handling/Modes/mode_demo.txt", "w+")

# # you can read and write

# file.close()


'''

    a+

open for reading and writing. The file is created if it does not exit. The stream is positioned at the end of the file.

'''

file = open("File Handling/Modes/mode_demo.txt", "a+")

file.write("This is first line\n")

print(file.read())

file.close()