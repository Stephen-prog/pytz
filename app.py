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

# function = A block of reusable code
#            place () after the function name to invoke it

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of {amount:.2f} is due: {due_date}.")
# display_invoice("Collin", 10.99, "12/12/2015")

# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z
# print(add(4, 5))
# print(subtract(16, 9))
# print(multiply(7, 9))
# print(divide(785, 5))
# def create_name(firstname, lastname):
#     firstname = firstname.capitalize()
#     lastname = lastname.capitalize()
#     return firstname + " " + lastname
# full_name = create_name("christian", "micheal")
# print(full_name)


# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces number of arguments
#                     1. positional 2. DEFAULT 3. keyword 4. arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)
# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500,0.1, 0))

# timer
# import time
# def count(end, start = 0):
#     for x in range(start, end+1):
#        print(x)
#        time.sleep(1)
#     print("DONE!")
# count(5)

# keyword arguments = an argument preceded by an identifier
#                     helps withs readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary
#def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num = get_phone(country=49, area=163, first=1234, last=3142)
# print(phone_num)


# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Lionel","Andreas","Messi")

# def print_address(**kwargs):
#         for key, value in kwargs.items():
#                 print(f"{key}: {value}")
# print_address(street= "Ortstraße",
#               apt= "68B",
#               city= "Hornbach",
#               state= "Birkenau",
#               zip= "69488")

# def shipping_label(*args, **kwargs):
#         for arg in args:
#             print(arg, end=" ")
#         print()
#         if "apt" in kwargs:
#             print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#         elif "pobox" in kwargs:
#             print(f"{kwargs.get('street')}")
#             print(f"{kwargs.get('pobox')}")
#         else:
#             print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

# shipping_label("Herr", "Dirk", "Müller",
#                street="Ortstraße",
#                apt= "68B",
#                city= "Hornbach",
#                state= "Birkenau",
#                zip= "69488"
#                )


# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# word = "BANANA"
# letter = input("Guess a letter in the secret word: ")
# if letter in word.lower():
#     print(f"{letter} is in the secret word.")
# else:
#     print(f"{letter} not found in secret word.")

# students = {"Lawrence", "Uche", "Chima", "Jerry"}
# student = input("Enter the student name: ")
# if student not in students:
#     print(f"{student} was not found.")
# else:
#     print(f"{student} is a student.")

# grades = {"Sara": "A",
#           "Ron": "B",
#           "Optimus": "A",
#           "Harry": "C",
#           "Joey": "D"}
# student = input("Enter the name of a student: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}.")
# elif student not in grades:
#     print(f"{student}'s grade not found.")

# email = "yoohoo@gmail.com"
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(squares)

# fruits = ["blueberry", "grape", "banana", "kiwi"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, -7, 8]
# position_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num <= 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 == 1]
# print(odd_num)

# grades = [97, 79, 88, 67, 49, 56]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)


# Match-case statement (switch): An alternative to using 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not valid"
# print(day_of_week(3))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False
# print(is_weekend("Sunday"))


# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files
# print(help("modules")) to view all available modules


# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in


# if__name__ = __main__: (this script can be imported OR run standalone)
#                         Functions and classes in this module can be reused
#                         without the main block of code executing

# ex. library = Import library for functionality
#               When running library directly, display a help page


# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and the layout of an object
# from car import Car

# car1 = Car("Mercedes-Benz", "S-Class", 2018, "white", False)
# car2 = Car("BMW", "X5", 2020, "silver", True)
# car3 = Car("Ferrari", "812", 2020, "black", False)
# car1.info()
# car2.buy()
# car3.drive()


# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allows you to share data among all objects created from that class

# class Student:

#     class_year = 2025   class variable
#     num_students = 0    class variable

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student("Jerry", 24)
# student2 = Student("Praise", 25)
# student3 = Student("Clara", 40)
# student4 = Student("Chandler", 28)
# student5 = Student("Joey", 27)
# student6 = Student("Phoebe", 28)
# print(f"The graduating class of {Student.class_year} has {Student.num_students} students.")


# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def move(self):
#         print(f"{self.name} is running.")

#     def sleep(self):
#         print(f"{self.name} is asleep.")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Horse(Animal):
#     def speak(self):
#         print("NEIGH!")

# dog = Dog("Pablo")
# cat = Cat("Felix")
# horse = Horse("Henry")



# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def rest(self):
#         print(f"{self.name} is resting.")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing.")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting.")

# class Deer(Prey):
#     pass
# class Tiger(Predator):
#     pass
# class Frog(Prey, Predator):
#     pass

# deer = Deer("Beefy")
# tiger = Tiger("Tyga")
# frog = Frog("Kermit")

#tiger.hunt()


# super() = Function used ina child class to call methods from a parent class (superclass).
#           Allows you t extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    # USING METHOD OVERRIDING,
    def describe(self):
        print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.142 * self.radius * self.radius}cm^2")
        # Extending the describe functionality from the parent class of shape
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        # Extending the describe functionality from the parent class of shape
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.base * self.height}cm^2")
        # Extending the describe functionality from the parent class of shape
        super().describe()

circle = Circle("grey", True, 3)
square = Square("blue", False, 5)
triangle = Triangle("green", True, 3, 2)

square.describe()

