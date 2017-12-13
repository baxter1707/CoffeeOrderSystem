
numbers = [12,43,2,75,3,2,18]

num = 0

for index in range(0, len(numbers)):
    if numbers[index] > num:
        num = numbers[index]

print(num)


####ASK WHY THIS ONE DOES NOT WORK BUT THE ABOVE DOES!###

#num = 0

#for index in range(0, (len(numbers)):
#    if numbers[index] > num:
#        num = numbers[index]

#print(num)
