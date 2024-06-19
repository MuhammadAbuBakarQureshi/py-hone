num = input("Enter a number : ")

num = int(num)

i = 2

while i < num:

    if (num % i) == 0:

        print("Not a prime number")
        break

    i += 1

if num == i:

    print("Prime number")