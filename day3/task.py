# size = input("What size of pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     print("Invalid size")

# print(f"Your final bill is: ${bill}")   

# Main Project

print('''
      ________           ________
     /  ______  \       /  ______  \
   /  /        \  \   /  /        \  \
 /  /            \  "  /            \  \
|  |               \ /               |  |
|  |                "                |  |
|  |                                 |  |
 |  |                               |  |
  |  |                             |  |
    |  |                         |  |
      |  |                     |  |
        |  |                 |  |
          |  |             |  |
            |  |         |  |
              |  |     |  |
                |  | |  |
                  | | |
                   | |
                    |
''')

one = input("You're in a fight, what do you want to do? Type 'stay' or 'run': ")
if one == "stay":
    two = input("You are going to be faced with faced with a lot of challenges in life, what do you want to do? Type 'stay' or 'run': ")
    if two == "stay":
        three = input("You might lose your life, what do you want to do? Type 'stay' or 'run': ")
        if three == "stay":
            print("You have found the love of your life")
        else:
            print("You gave up!")    
    else:
        print("You gave up!")    
else:
    print("You gave up!")