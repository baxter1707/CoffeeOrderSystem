// console output is not visible to normal user
console.log("hello world")

var name = "John"
var age = 23

// creating a function with no parameters
function greet() {
  console.log("calling function greet")
}

// calling greet function
greet()

function greetByNameAndAge(name,age) {
  console.log(name + " " + age)
}

greetByNameAndAge(name,age)

function add(a,b) {
  return a+b
}

var result = add(4,5)
console.log(result)

// arrays

// empty array
//var names = []

// array with names
var names = ["John","Mary","Alex","Steve"]
console.log(names)

// for loop in javascript
for(var index = 0; index<names.length; index++) {
  // print out name at particular index
  console.log(names[index])
}

// if-else conditions

if(age < 18) {
  console.log("You are less than 18")
} else if(age > 18 && age < 21) {
  console.log("You are greater 18 and less than 21")
} else if(age > 21 || age == 50) {
  console.log("You are > 21 or your age is 50")
} else {
  console.log("else block")
}

let message = "Hello World"

function greetMe() {

    let message = "Hello How are you"

    if(age > 18) {
      // variables defined using var are global scope
      // use let to define scope
      let message = "Good Bye"
      console.log(message)
    }
    else {
      // message variable refers to the one declared on line 59
      message = "Good Bye"
    }

    console.log(message)
}



greetMe()

// constant is defined only once and you cannot change it after it has been assigned
const pi = 3.142

// cannot assign pi variable because it is declared as a constant
//pi = 5.0


// Classes and Objects

let user = new Object()
user.firstName = "John"
user.lastName = "Doe"
user.make = "Honda"
user.model = "Accord"
console.log(user)

// creating a car class which in reality is just a function

function start() {
  console.log("Starts the server!")
}

function Car(make,model) {
  this.make = make
  this.model = model

  // declaring anonymous function
  this.start = function() {
    console.log("Starting Car")
  }

  this.changeGear = function(gearNumber) {
    console.log("changing gear to " + gearNumber)
  }

}



// create a new car object
let car = new Car('Honda','Accord')
let car1 = new Car('Toyota','Camry')

//car.make = "Honda"
//car.model = "Accord"
console.log(car)

car.start()
car.changeGear(3)

// calling start and changeGear on car1 object
car1.start()
car1.changeGear(4)

function Task() {

  this.name = ""
  this.priority = 0
}

let task = new Task()
task.name = "Wash the car"
task.priority = 1

// adding task to a tasks array
let tasks = [task]

tasks.push(3)


console.log(tasks)
