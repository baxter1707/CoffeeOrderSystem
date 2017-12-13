
import json

class Customer:

    def __init__(self,firstname = '',lastname = '', dictionary = {}):

        if 'firstname' in dictionary and 'lastname' in dictionary:
            self.firstname = dictionary['firstname']
            self.lastname = dictionary['lastname']
        else:
            self.firstname = firstname
            self.lastname = lastname

    def toDictionary(self):
        return {"firstname":self.firstname, "lastname":self.lastname}

#customer = Customer('john','doe')

filename = 'username.json'

with open(filename) as file_obj:
    dictionary = json.load(file_obj)
    customer = Customer(dictionary = dictionary)
    print(customer.firstname + " " + customer.lastname)
    #print(dictionary['firstname'])
    #print(customer.firstname)

#with open(filename,'w') as file_obj:
#    json.dump(customer.toDictionary(),file_obj)
