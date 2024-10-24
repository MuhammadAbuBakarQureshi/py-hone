with open("File Handling/Practice/Question 1/Q1.txt", "w+") as file:

    file.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")

    file.seek(0)

    data  = file.read()

    new_Data = data.replace("Java", "python")

    file.seek(0)

    file.write(new_Data)


    if new_Data.find("learning") != -1:

        print("Found")
    else:

        print("Not Found")