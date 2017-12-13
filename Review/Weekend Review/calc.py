import calcFunct as calc

first = float(raw_input("Enter first number."))
mathOp = (raw_input("Enter +, -, *, or /"))
second = float(raw_input("Enter second number."))

if mathOp == "+":
    answer = calc.add(first, second)

elif mathOp == "-":
    answer = calc.subtract(first, second)

elif mathOp == "*":
    answer = calc.multiply(first, second)

elif mathOp == "/":
    answer = calc.divide(first, second)
#
