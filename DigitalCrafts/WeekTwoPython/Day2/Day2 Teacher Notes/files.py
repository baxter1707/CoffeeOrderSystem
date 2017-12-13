
filename = "helloworld.txt"

# reading the whole file at once
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("READING LINE BY LINE")
# reading the file line by line
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.rstrip('\n'))


# writing a file
with open('filetowrite.txt','w') as file_object:
    file_object.write('Bye World. I am using Python to write a file')


# appending file
with open('appendingToFile.txt','a') as file_object:
    file_object.write('Bye World')
    file_object.write('\n')
