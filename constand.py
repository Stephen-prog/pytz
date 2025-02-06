# Concession stand program

menu = {"popcorn": 6.50,
        "soda": 3.00,
        "water": 2.50,
        "Lemonade": 3.50,
        "fries": 2.50,
        "pretzel": 2.00,
        "nachos": 4.50,
        "pizza": 4.00,
        "chips": 1.50}

cart = []
total = 0

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")
print("----------------------")

while True:
    food = input("Please select an item from the menu (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: €{total:.2f}")

