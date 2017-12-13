import json ###???Forgot what this does???###

class Person(object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def toDictionary(self): ##Takes the users input and changes it to to dictionary format
        #returns the user input class and changes it to dictionary
        return {"firstname":self.firstname, "lastname":self.lastname}

    ##the below starts writing to a file in json
filename = "ToDoList.json"  ##this takes the file and assigns it to the variable filename


userFromClass = User('Mary','Doe')


with open(filename, 'w') as file_object: ##this opens the filename(ToDoList.json) as a writable .json file and creates the road or path file_object
    userDictionary = userFromClass.toDictionary() ##This runs the toDictionary method on the input data and changes it into a dictionary format
    json.dump(userDictionary,file_object)##This takes the var (userDictionary) and makes it json, and then pushes, or dumps it along the road to the filename.

with open(filename) as file_object: ##this is just opening the file to be read. it is not making changes to the file
    userDictionary = json.load(file_object)##This is loading the json file onto the path or road to the file name, and assigning it to the var userDictionary

    firstname = userDictionary["firstname"]##this is taking the json file var and pulling the firstname from it, and assigning it to the first name variable
    lastname = userDictionary["lastname"]

    user = User(firstname, lastname) ## this is taking the combined firstname and last name variable form the user class and assigning them to the new var user.
    print(user.firstname)
    print(user.lastname)
