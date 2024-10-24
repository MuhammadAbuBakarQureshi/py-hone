with open("File Handling/WITH Function/demo.txt", "r") as file_Read:

    print(file_Read.read())

with open("File Handling/WITH Function/demo.txt", "w") as file_Write:

    file_Write.write("This message is written using WITH")