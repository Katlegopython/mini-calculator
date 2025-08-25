# 🧮 Mini Calculator

# Get user input
num1 = float(input("Enter first number: "))
op = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator")
