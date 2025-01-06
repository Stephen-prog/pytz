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

# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# : 03 = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# price1 = 3000.14159
# price2 = -9870.656
# price3 = 1200.347

# print(f"Price 1 is €{price1:+,.2f}")
# print(f"Price 2 is €{price2:+,.2f}")
# print(f"Price 3 is €{price3:+,.2f}")

# while loop = execute some code WHILE some condition remains true
# name = input("Enter your name: ")
# while name == "":
#     print("Please enter your name.")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

#age = int(input("Enter your age: "))
# while age <= 0:
#     print("Invalid age")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")

# food = input("Enter your favourite food: ")
# while not food == "q":
#      print(f" You like {food}")
#      food = input("Enter another favourite food: ")
# print("Tschuss! ")

# num = int(input("Enter a number between 1 and 10: "))
# while 1 < num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1 and 10: "))
# print(f"Your number is {num}.")

# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence etc.

# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")
# for x in  range(rows):
#     for y in range(columns):
#         print(symbol, end=" ")
#     print()

# collection = single "variable" used to store multiple values
#   List  = [] ordered or changeable. Duplicate OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ("apple", "orange", "banana", "pineapple")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# 2dlist = [list1, list2, list3]
# groceries = [["apple", "orange", "banana", "mango"],
#              ["broccoli", "carrots", "spinach"],
#              ["chicken", "fish", "turkey"]]
# for grocery in groceries:
#     for item in grocery:
#         print(item, end=" ")
#     print()

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#    print()

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# capitals = {"Nigeria": "Abuja",
#             "Ghana": "Accra",
#             "Germany": "Berlin",
#             "Japan": "Tokyo"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Nigeria"))

# if capitals.get("China"):
#     print(f"The capital is {capitals.get("Ghana")}.")
# else:
#     print("Capital not found.")
# capitals.update({"Russia": "Moscow"})
# capitals.update({"Japan": "Osaka"})
# capitals.pop("Ghana")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")

# Random numbers
# import random
# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(low, high) prints any random int between low and high
# number = random.random() prints any random float between 0 and 1
# option = random.choice(options) prints any random element from tuple or maybe list
# random.shuffle(cards)
# print(cards)
# print(help(random)) prints all random methods