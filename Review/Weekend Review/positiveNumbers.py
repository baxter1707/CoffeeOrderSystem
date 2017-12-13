numbers = [-1,16,-99,12,43,2,-3,-45,13]

num = []

for index in range(0, len(numbers)):
    if numbers[index] > 0:
        num.append(numbers[index])

print(num)
