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

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_positions(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Waiter", "Janitor"]
        return position in valid_positions

employee1 = Employee("Danny", "Manger")
employee2 = Employee("Sandra", "Cashier")
employee3 = Employee("Deborah", "Cook")

print(Employee.is_valid_positions("Waiter"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())