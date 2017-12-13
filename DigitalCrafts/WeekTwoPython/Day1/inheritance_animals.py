
##You need (object) anytime you want to use inheritance features
class Animal(object):

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def run(self):
        print("I run normally")

    def walk(self):
        print('I am walking')

    def eat(self):
        print("I am eating")

##The (Animal) is telling the cheetah class that it ALS) uses everything in Animal class
## super = parent
class Cheetah(Animal):
    def __init__(self):
        ##Calling the animal class intializer/constructor
        ##super = parent             Passing in name and species of parent class
        super(Cheetah,self).__init__("Cheetah", "Cats")
        #self.name = ""

    def run(self):
        print("Cheetah is running super fast.")



cat = Animal("Tiger", "Cat Species")
cat.walk()
cat.eat()

ch = Cheetah()
ch.run()
ch.walk()
ch.eat()
