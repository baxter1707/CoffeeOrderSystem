
names = ["Alex","John","Mary","Steve","Seinfeld"]

nameToDelete = raw_input("Please enter the name to delete. ")
indexToDelete = -1
##if nameToDelete in names:
##    print("Name is found")


for index in range(0, len(names)):
    if nameToDelete.lower() == names[index].lower():
        indexToDelete = index
        break

del names[indexToDelete]
print(names)
