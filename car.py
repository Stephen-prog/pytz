class Car:
    def __init__(self, make, model, year, color, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving the {self.make} {self.model}.")

    def stop(self):
        print(f"You stopped driving the {self.make} {self.model}.")

    def buy(self):
        print(f"You want to buy {self.color} {self.make} {self.model}")

    def info(self):
        print(f"This is a {self.year} {self.make} {self.model}")