age = 13
isFelon = True
isResident = False
name = "John"

#if name is not equal to
if name != "John":
    print("You are not john")

if age < 18:
    print("You are to young to vote!")

elif isFelon == True or isResidnet == False:
    print("You are a Felon.")

else:
    print("Welcome and you can vote")

#cat var created is only used inside of the if statement created
if name == "John":
    cat = "My Cat"
