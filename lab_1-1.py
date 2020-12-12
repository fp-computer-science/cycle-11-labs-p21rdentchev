# Ryan Dentchev

total = 0
while True:
    user_number = input("Input an number ")
    if user_number == "-1":
        break
    else:
        total += int(user_number)


print("Sum of numbers is {0}".format(total))
