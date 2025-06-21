# print("Sanjana" [3])
# print(type("Sanjana"))
# print(type(321))
# print(type(True))

# Main Project

bill = float(input("What was the total bill? "))

tip = float(input("What percentage tip would you like to give? "))

split = float(input("How many people to split the bill? "))

print(f"Each person should pay: {round(bill * (1 + tip / 100) / split, 2)}")
