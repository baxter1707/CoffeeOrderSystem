numbers = [12,43,2,75,3,22,18]

num = 1000000000  ###Does this number have to be super high or can it be something else?

for index in range(0, len(numbers)):
    if numbers[index] < num:
        num = numbers[index]

print(num)
