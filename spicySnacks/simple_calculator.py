num1 = int(input("Enter first number: "))
sign = input("Enter sign (+, -, *, /)): ")
num2 = int(input("Enter second number: "))

if sign == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif sign == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif sign == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif sign == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
