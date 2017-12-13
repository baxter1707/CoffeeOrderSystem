
class Car(object):
    def __init__(self,make,model):
            self.make = make
            self.model = model

    def start(self):
        print("Starting the gas car")


class ElectricCar(Car):
    def __init__(self):
        super(ElectricCar, self).__init__("Tesla","X")

## Overriding the parent method/function
    def start(self):
        print("Starting the Electric Car")

electric_car = ElectricCar()
print(electric_car.make)
print(electric_car.model)

electric_car.start()
