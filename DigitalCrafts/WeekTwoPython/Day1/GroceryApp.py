
class Store(object):
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.grocery_list = []

    def add_items(self, grocery_item):
        self.grocery_list.append(grocery_item.title)
        self.grocery_list.append(grocery_item.price)



class Item(object):
    def __init__(self, title,price):
        self.title = title
        self.price = price



### STORES
walmart = Store("Walmart", "Retail")
amazon = Store("Amazon", "Online")
heb = Store("HEB", "Grocery")

### ITEMS
milk = Item("Milk","$2")
soda = Item("Soda", "$1")
fish = Item("Fish","$5")
paper = Item("Paper", "$3")
napkin = Item("Napkins","$2")
plate = Item("Paper Plates","$3")
chip = Item("Chips","$4")
chicken = Item("Chicken","$9")
beef = Item("Beef","$8")
cable = Item("Charging Cable","$15")
headphone = Item("Headphones", "$12")

#walmart.grocery_list.append(paper)

### METHODS TO ADD ITEMS TO STORE LIST
walmart.add_items(paper)
walmart.add_items(napkin)
walmart.add_items(plate)
amazon.add_items(headphone)
amazon.add_items(cable)
heb.add_items(milk)
heb.add_items(soda)
heb.add_items(fish)
heb.add_items(chip)


###LOOP TO PRINT EACH ITEM IN THE LIST
print(walmart.title + ", " + walmart.description)
#print(walmart.grocery_list)
for item in walmart.grocery_list:
    print(item)
print("\n")

print(amazon.title + ", " + amazon.description)
for item in amazon.grocery_list:
    print(item)
print("\n")

print(heb.title + ", " + heb.description)
for item in heb.grocery_list:
    print(item)
