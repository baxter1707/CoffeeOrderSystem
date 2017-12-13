name = raw_input("What is your name?")
age = raw_input("What is your age?")
address = "777 Preston St"
#This is called String continuation.
#message = "My name is " + name + " and my age is " + age + "."

# {0} and {1} are assigned to name and then age using the .format(name,age) at
# the end of the code. Name is assigned to {0} and age is assigned to {1}.
#.format is a function
message = "My name is {0} and my age is {1} and my address is {2}".format(name,age,address)

#message ="My name is [name], and my age is [age]."
print(message)


#print(name)
#print(age)
