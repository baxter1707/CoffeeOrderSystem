
###Question, when not prime number run it looks funny.

number = int(raw_input("Please enter your number."))

if number > 1:
    for index in range(2, number):
        if (number % index) == 0:
            print("{0} is not a prime number!" ).format(number)
            break

        else:
            print(("{0} is a prime number!" ).format(number))

            break


        #elif (number % index) != 0:
        #    print("{0} is not a prime number!").format(number)

#            break
#
