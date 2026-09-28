num1 = int(input("Put your First Number : "))
num2 = int(input("Put your Second Number : "))
print("""Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division""")

choose = int(input("Choose an operation : "))
if choose == 1:
      print(num1 + num2)
elif choose == 2:
      print(num1 - num2)
elif choose == 3:
      print(num1 * num2)
elif choose == 4:
      print(num1 / num2)
else:
      print("Your Number is Wrong")