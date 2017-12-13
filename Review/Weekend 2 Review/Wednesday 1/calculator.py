import calcFunctions as calc

while True:

    no1 = float(raw_input("Please enter your first number."))
    mathOp = raw_input("Please choose '+','-','*','/' or press 'q' to quit.")
    no2 = float(raw_input("Please enter your second number."))


    if mathOp is "+":
        calc.add(no1,no2)

    elif mathOp is "-":
        calc.sub(no1,no2)

    elif mathOp is "*":
        calc.multiply(no1,no2)

    elif mathOp is "/":
        calc.divide(no1,no2)

    elif mathOp is "q":
        break
