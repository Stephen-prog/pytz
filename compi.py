# Python compound interest calculator
from html.parser import interesting_normal

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle must be greater than or equal to 0!")

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate <= 0:
        print("Interest rate must be greater than or equal to 0!")

while time <= 0:
    time = int(input("Enter the Time in years: "))
    if time <= 0:
        print("Time must be greater than or equal to 0!")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: €{total:.2f}.")
