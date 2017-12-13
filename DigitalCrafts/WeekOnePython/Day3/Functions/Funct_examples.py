
## Making a function

def greet():
##continue to indent, as soon as you stop indenting Python ends the function
    print("hello world")
    print("Michael")

print("outside the function")

## Calling a function
greet()

## Greet user by name
def greet(name,age):
##continue to indent, as soon as you stop indenting Python ends the function
    print("hello " + name)
    print("bye")
    print("hello")

## Variables or arguments declared are only good within the function.

##This wont work because you have nothing in () you are calling an empty message.
#greet()

greet("John",23)

##ADD function
def add(no1,no2):
    result = no1 + no2
    return result
    ##print(anything) If you write anything after return it will not get executed.


result = add(2,3)
result = add("Hello"," world")


###Example 3 Airport (2 values or Tuple)
def getAirport():
    return "IAH,2345"

(name,code) = getAirport()


#Default Values

def create_pizza(name = "Cheese Pizza"):
    print(name)

create_pizza()
create_pizza(Chicken Pizza)

#When you dont know the number of arguments
#The * is used when you dontknow how many arguments the person will send in.
def add_toppings(*toppings):
    print(toppings)

add_toppings('Mushrooms', 'Green Peppers' 'Tomato','Cheese')
