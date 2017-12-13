number = int(raw_input("Please enter a number."))

if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz!")

elif number % 3 == 0 and number % 5 != 0:
    print("Fizz")

elif number % 3 != 0 and number % 5 == 0:
    print("Buzz!")
