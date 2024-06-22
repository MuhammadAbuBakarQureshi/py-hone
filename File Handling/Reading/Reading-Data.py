f = open("File Handling/Reading/demo.txt", "r")

# data = f.read() # Reads Entire File

line1 = f.readline() # Reads one line at a time

line2 = f.readline() # Read one line at a time

f.close()

# print(data)

print(line1)

print(line2)