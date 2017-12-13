
class Restuarant:

    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.itemsOrdered = 0

    def info(self):
        #print("{0} is {1}".format(title,description))
        print(self.title + self.description)

    def orderItem(self):
        self.itemsOrdered += 1

    def displayOrderStatus(self):
        print("We ordered " + str(self.itemsOrdered) + " And item was " + self.title)

rest1 = Restuarant('Barnabys','Very good local food.')
rest1.orderItem()
#print(rest1.title)
#print(rest1.description)
print(rest1.info())
print(rest1.displayOrderStatus())
