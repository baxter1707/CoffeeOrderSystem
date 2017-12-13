numbers = [12,15,-1,-45,45,-90,62,34,-5]
new_numbers = []

zero = 0

#for number in range(0, len(numbers)):
#    if number >= zero:
#        print(number)


for number in numbers:
    if number >= zero:
        new_numbers.append(number)

print(new_numbers)
