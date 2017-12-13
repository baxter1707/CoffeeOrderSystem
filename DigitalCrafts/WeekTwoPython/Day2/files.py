
#           /projects/todo/hello.txt
filename = "helloworld.txt"

##This is reading the entire file at once.
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

##Reading the file line by line: using .readlines()
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)
        #print(line.rstrip('\n'))


##Writing a file  ((this will overwrite everything exisiting in file))
with open("filetowrite.txt", "w") as file_object:
    file_object.write("bye World. I am using python to write this.")

#Appending or adding to a file
with open("appendingToFile.txt","a") as file_object:
    file_object.write("Bye world,")
    file_object.write ("\n")
