
num = int(raw_input("Please enter a number.  "))

if num > 1:
    for index in range(2, num):
        if num % index == 0:
            print("Your number is not prime")

        else:
            print ("Your number is prime.")

        break
