import functions
##EC Calculator made by unicornzss
while True:
    print("Welcome to the EC calculator!")
    num1 = int(input("num1>"))
    ANT = input("*,-,+,/,>,< -->")
    num2 = int(input("num2>"))

    if ANT == "+":
        functions.adder(int(num1), int(num2))
    elif ANT == "-":
        functions.negater(int(num1), int(num2))
    elif ANT == "*":
        functions.timr(int(num1), int(num2))
    elif ANT == "/":
        functions.div(int(num1), int(num2))
    elif ANT == ">":
        functions.grt(int(num1), int(num2))
    elif ANT == "<":
        functions.low(int(num1), int(num2))