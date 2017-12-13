
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("{0} {1} {2}".format(self.year,self.make,self.model))

car1 = Vehicle("Mazda", "CX-5", "2013")
print(car1.make)
print(car1.model)
print(car1.year)
car1.print_info()
