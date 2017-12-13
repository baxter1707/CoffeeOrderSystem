import json

# creating class User
class User(object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def toDictionary(self):
    #    {"key":"value"}
        return {"firstname":self.firstname,"lastname":self.lastname}

filename = 'tasks.json'

# dictionary
user = {"firstname":"John","lastname":"Doe"}

# create user object
userFromClass = User('Mary','Doe')

with open(filename,'w') as file_object:
    #json.dump(user,file_object)
    userDictionary = userFromClass.toDictionary()
    json.dump(userDictionary,file_object)

with open(filename) as file_object:
    userDictionary = json.load(file_object)

    firstname = userDictionary["firstname"]
    lastname = userDictionary["lastname"]

    user = User(firstname,lastname)
    print(user.firstname)
    print(user.lastname)
