# Polymorphism = Greek word that means "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" =Object must have necessary attributes/methods

# from abc import ABC, abstractmethod

# class Shape:

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(5), Square(7), Triangle(9, 11), Pizza("pepperoni", 13) ]

# for shape in shapes:
#     print(f"The area is {shape.area()}cm^2")



# Duck-typing = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck."

# class Animal:
#     is_alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW")

# class Car:
#     is_alive = False

#     def speak(self):
#         print("BEEP!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.is_alive)



# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

# class Employee:

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

    # Instance method
#     def get_info(self):
#         return f"{self.name} = {self.position}"

#     @staticmethod
#     def is_valid_positions(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Waiter", "Janitor"]
#         return position in valid_positions

# employee1 = Employee("Danny", "Manger")
# employee2 = Employee("Sandra", "Cashier")
# employee3 = Employee("Deborah", "Cook")

# print(Employee.is_valid_positions("Waiter"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())


# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
"""
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gps = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Don-don", 4.0)
student2 = Student("Rita", 3.2)
student3 = Student("Raphael", 3.8)

print(Student.get_count())
print(Student.get_average_gpa())
"""

# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects
"""
class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa

student1 = Student("Danny", 3.2)
student2 = Student("Ghost", 3.5)

print(student1)
print(student1 == student2)
print(student1 > student2)
"""

"""
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found"

book1 = Book("The Lord of The Rings", "J.R.R. Tolkien", 1077)
book2 = Book("Othello", "William Shakespeare", 114)
book3 = Book("Dune Messiah", "Frank Herbert", 352)

print(f"{book1['num_pages']} pages")
print(book3['publisher'])
"""


# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter,setter, and deleter method

"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width =new_width
        else:
            print("Width must be greater than zero.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")

rectangle = Rectangle(3, 4)

rectangle.width = 8
rectangle.height = 9

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)
"""


# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator


# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You added sprinkles 🎉*")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You added fudge 🍫*")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨.")

# get_ice_cream("vanilla")



# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

"""
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't  divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")
"""

# Python file detection

"""
import os

file_path = "C:/Users/nicol/OneDrive/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.exists(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("THis is a directory")
else:
    print(f"Location not found")
"""



# Python writing files (.txt, .json, .csv)

"""
import json
import csv

employees = [["Name", "Age", "Occupation"],
            ["Joe", 38, "Electrician"],
            ["Kent", 47, "Mechanic"],
            ["Elise", 30, "Receptionist"]]

file_path = "C:/Users/nicol/OneDrive/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
"""



# Python reading files (.txt, .json, .csv)

"""
import csv
file_path = "C:/Users/nicol/OneDrive/Desktop/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("Permission Required to access this file!")
"""



# Dates and times with python

"""
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 10)
jetzt = datetime.datetime.now()

jetzt = jetzt.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 1,00,00,00)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
"""


# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)