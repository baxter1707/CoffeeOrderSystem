while True:
    user = int(raw_input("Please enter the number you would like to check. "))

    if user % 2 == 0:
        print("Your number is even!")

    elif user % 2 != 0:
        print("Your number is odd...")

    else:
        break
