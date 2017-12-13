
class Address:
    def __init__(self, street, state, zipCode):
        self.street = street
        self.state = state
        self.zipCode = zipCode


class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.addresses = []

# creating customer
customer = Customer()
customer.firstName = "John"
customer.lastName = "Doe"

# creating addresses
address1 = Address("1200 Richmond Ave","TX","77042")
address2 = Address("3200 Harvin Ave","TX","77098")
address3 = Address("1234 Woodlands","TX","77089")

customer.addresses.append(address1)
customer.addresses.append(address2)
customer.addresses.append(address3)

# print customer with addresses
print(customer.firstName + " " + customer.lastName)
# print customer addresses
for address in customer.addresses:
    print(address.street + " " + address.state)
    print("\n")


class Job:
    def __init__(self):
        self.title = ""
        self.location = ""
        self.department = ""

class Employee(object):
    def __init__(self,first_name,last_name):
        self.firstName = first_name
        self.lastName = last_name
        self.job = Job()

employee = Employee("John","Doe")

employee.job.title = "Mechanic"
employee.job.location = "Houston"
employee.job.department = "IT"

#print(employee.firstName + " " + employee.lastName)
#print(employee.job.title + " " + employee.job.location)
