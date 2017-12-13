#empty array
#names - []

#names = ["Alex","John","Mary","Steve"]
#print(names[0])


#loop
#Most common loop is the for loop

#for index in range(1,10):
#    print(names[index])
###This will crash because range is 1-9 and their are only 4 items in the array

numbers = [1,2,3,4,5,6,7,8]

for index in range(0, len(numbers)):
    print(numbers[index] * 2)


for name in names:
    print(name)
    print(name)


##appending the items to the array. (Adding items to the array)

names.append("Seinfeld")

print(names)

##to delete items from an array
del names[1]

print(names)

##inserting at particular position
names.insert(4,"John")

print(names)
