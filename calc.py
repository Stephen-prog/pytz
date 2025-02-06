# Python calculator

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operator = input("Enter an operator (+ - * /): ")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"Invalid operator! ")
