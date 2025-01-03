# import math
# Exercise 1 Rectangle Area Calc

# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = str(length * width)
# print("The area of the rectangle is " + area)

# Exercise 2 Shopping Cart Program
# item = input("What would you like to purchase?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: €{total}")

# Circumference of a circle
# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm")

# Area of a circle
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area is: {round(area, 2)}cm²")

# Pythagoras theorem
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"Side C = {c}")

# if statements
# name = input("Enter your name: ")
# if name == "":
#    print("Please enter your name!")
# else:
#    print(f"Hello {name}")
# online = True
# if online:
#    print("This user is online.")
# else:
#    print("This user is offline.")

# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y
# num = 7
# a = 8
# b = 9
# age = 10
# temperature = 5
# user_role = "Don Barzini"
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(access_level)

# name = input("Enter your full name: ")
# phone_number = input("Enter your Phone Number: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("q")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")
# print(phone_number)

# print(help(str))   # this shows all string methods

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = "9876-0645-3281-2468"
# credit_number = credit_number[::-1]
# last_digits = credit_number[-4:]
# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# print(credit_number)

