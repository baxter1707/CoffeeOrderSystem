
class Car:

    ##Fucntion inside the class that is responsible for initialing the class: Car.
    ## self is is referencing the bmw, or object
    def __init__(self,make,model):
###Everything self.  are properties of the object
        self.make = make
        self.model = model
        self.noOfCyl = 4   ###ASK ABOUT IF YOU HAVE TO ADD TO DEF LINE

    ##self will always reference to the current object
    ##In the above self = bwm, but below self = Toyota
    def start(self):
        print("Starting Car")


##Object
bmw = Car("BMW", "Series 3")
print(bmw.make)
print(bmw.model)

toyota = Car("Toyota", "Camry")
print(toyota.make)
print(toyota.model)




###Defining a PERSON
class Person:                              ##This is used when you dont know, and you would have to use it at the end.
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastname
        self.middleName= ''
        self.age = -1
        self.height = 0

    def walk(self):
        print("Person is walking")

    def talk:
        print("Person is talking.")

    def sing(self, songName):
        print("Person is singing" + songName)



person1 = Person('John','Doe')
person1.age = 23
person1.weight = 190

person1.walk()
person1.talk()
person1.sing("Song Name")
