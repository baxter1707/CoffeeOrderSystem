
class Calculator(object):

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def add(self,no1,no2):
        result = no1+no2
        print("The total is {0}".format(result))

    def subtract(self,no1,no2):
        result = no1-no2
        print("The total is {0}".format(result))

    def multiply(self,no1,no2):
        result = no1*no2
        print("The total is {0}".format(result))

    def divide(self,no1,no2):
        result = no1/no2
        print("The total is {0}".format(result))


no1 = int(raw_input("Please enter the first number."))
no2 = int(raw_input("Please enter the second number"))
mathOp = raw_input("Please choose '+' '-' '*' '/' )")
calc = Calculator(no1,no2)

while True:
    if mathOp == "+":
        calc.add(no1,no2)

    elif mathOp == "-":
        calc.subtract(no1,no2)

    elif mathOp == "*":
        calc.multiply(no1,no2)

    elif mathOp == "/":
        calc.divide(no1,no2)

    break
