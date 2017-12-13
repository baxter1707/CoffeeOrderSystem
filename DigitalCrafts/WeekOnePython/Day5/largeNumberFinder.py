numbers = [2,3,45,1222,234,789,5,6]

#high = 0

#for index in numbers:
#    if index > high:
#        high = index
#print(index)


n = 0
for index in range(0, len(numbers)):
    if numbers[index] > n:
        n = numbers[index]

print("The largerst number in the array is {0}".format(n))
