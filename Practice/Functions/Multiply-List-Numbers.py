
def multpily_list(numbers):

    total = 1

    for values in numbers:

        total *= values

    return total


numbers = [8, 2, 3, -1, 7]

print(multpily_list(numbers))