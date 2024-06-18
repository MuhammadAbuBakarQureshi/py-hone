age = input("Enter your age : ")

if int(age) >= 18:

    print("You can vote")

elif int(age) < 18 and int(age) > 3:

    print("You cannot vote")

else:

    print("You are kid")
