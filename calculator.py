choose = 0
list1 = []
while 7 != choose:
    print("""Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Show History
6. Clear History
7. End!""")

    try:
        choose = int(input("Choose an operation: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choose == 7:
        print("Finish.")
    elif choose < 1 or choose > 7:
        print("You should choose between 1 and 7.")
        continue
    elif choose == 5:
        n = 0
        for i in list1:
            n = n + 1
            print(f"{n}. {i}")
        if list1 == []:
            print("History is already empty.")
    elif choose == 6:
        if list1 == []:
            print("There is no history to clear.")
        else:
            list1.clear()
            print("History cleared successfully.")
    else:
        try:
            num1 = float(input("Put your First Number: "))
            num2 = float(input("Put your Second Number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choose == 1:
            result = num1 + num2
            print(f"Result: {result}")
            list1.append(f"{num1} + {num2} = {result}")
        elif choose == 2:
            result = num1 - num2
            print(f"Result: {result}")
            list1.append(f"{num1} - {num2} = {result}")
        elif choose == 3:
            result = num1 * num2
            print(f"Result: {result}")
            list1.append(f"{num1} * {num2} = {result}")
        elif choose == 4:
            if num2 == 0:
                print("Cannot divide by zero")
                continue
            else:
                result = num1 / num2
                print(f"Result: {result}")
                list1.append(f"{num1} / {num2} = {result}")