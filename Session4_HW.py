# Question 1
# I have a list of things I need to buy from my supermarket of choice.
# shopping_list = [
# "oranges",
# "cat food",
# "sponge cake",
# "long-grain rice",
# "cheese board",
# ]
# print(shopping_list[1])

# I want to know what the first thing I need to buy is.
# However, when I run the program it shows me a different answer to what I was expecting?
# What is the mistake? How do I fix it?
#You need to have [0] not [1] as Python counts 0 as the first value

# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices. '
#   'Finish the program by asking the user to input an item and then output its price.)
# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00,
# }
#
# type = input("What type of chocolate? ")
#
# if type == 'white':
#     print(chocolates['white'])
# elif type == 'milk':
#     print(chocolates['milk'])
# elif type == 'dark':
#     print(chocolates['dark'])
# elif type == 'vegan':
#     print(chocolates['vegan'])
# else:
#     print("We don't have that type")

# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers. After comparing the two sets of numbers,
# the program should output a prize based on the number of matches:

# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random
lottery_ticket = random.sample(range(1,100),7) #7 numbers of lottery ticket
print("These are your lottery numbers: ",lottery_ticket)
lottery_picks = random.sample(range(1,100),7) #Generates 7 random nums btwn 1-100
print("These are the picked numbers: ",lottery_picks)

matching_numbers = sum(num in lottery_ticket for num in lottery_picks)

if matching_numbers == 3:
    print("Prize: £20")
if matching_numbers == 4:
    print("Prize: £40")
if matching_numbers == 5:
    print("Prize: £100")
if matching_numbers == 6:
    print("Prize: £10000")
if matching_numbers == 7:
    print("Prize: £1000000")

else:
    print("You aren't a winner this time!")






