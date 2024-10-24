students = ["Muhammad", "Ali", "Usman", "Asad", "Babar", "Hamza"]

for name in students:

    if name == "Babar":

        break # we want to break the loop at "Babar"

    elif name == "Usman":

        continue # Now usman will not be printed beacuse

    print(name)