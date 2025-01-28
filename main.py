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

class Animal:
    is_mammal = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")