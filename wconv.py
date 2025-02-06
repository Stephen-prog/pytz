# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (kg or lbs):")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"Invalid unit! ")


