choose = 0
while 5 != choose:
    print("""Choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. End!""")

    choose = int(input("Choose an operation : "))
    if choose == 5:
        print("Finish.")
    else:
        num1 = int(input("Put your First Number : "))
        num2 = int(input("Put your Second Number : "))
        if choose == 1:
            print(num1 + num2)
        elif choose == 2:
            print(num1 - num2)
        elif choose == 3:
            print(num1 * num2)
        elif choose == 4:
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(num1 / num2)
        else:
            print("Your Number is Wrong")