
class Customer(object):
    def __init__(self):
        self.firstName = ""
        self.lastName = ""







class Job(object):
    def __init__(self):
        self.title = ""
        self.location = ""
        self.department = ""


class Employee(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
##      This is now calling the self from the Job Class
        self.job = Job()

employee1 = Employee('John', 'Doe')
employee1.job.title = "Mechanic"
employee1.job.location = "Houston"
employee1.job.department = "Warehouse"

print(employee1.firstname + " " employee1.lastName)
print(employee1.job.title + " " employee1.job.location)
