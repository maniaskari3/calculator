choose = 0
while 5 != choose:
    print("""Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. End!""")

    try:
        choose = int(input("Choose an operation: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choose == 5:
        print("Finish.")
    elif choose < 1 or choose > 5:
        print("You should choose between 1 and 5.")
        continue
    else:
        try:
            num1 = float(input("Put your First Number: "))
            num2 = float(input("Put your Second Number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choose == 1:
            print(f"Result: {num1 + num2}")
        elif choose == 2:
            print(f"Result: {num1 - num2}")
        elif choose == 3:
            print(f"Result: {num1 * num2}")
        elif choose == 4:
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(f"Result: {num1 / num2}")