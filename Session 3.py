#Comparison operators
#Comparison operators compare values to decide whether something is True or False
#Boolean data types are True or False

#Summary of comparison operators
# Equal to ==
# Not equal to !=
# Greater than >
# Less than <
# Greater than or equal >=
# Less than or equal <=

# today = input('What day is it? ')
# is_monday = today == 'Monday' #CASE SENSITIVE
# print('Today is Monday: {}'.format(is_monday))
##This prints Today is Monday: True if input = Monday or False if input = other day

# #float() converts strings to floats (decimals)
# temperature = input('What is the temperature? ')
# is_freezing = float(temperature) <= 0.0
# print('The temperature is freezing: {}'.format(is_freezing))
##if input is less than or equal to 0, it will print True


# Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger
# restaurant to go to.
#
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# Burger is within budget: True
#
# Hint: remember to convert the input from a string to a decimal with float()

# price = input("How much does the burger cost? ")
# is_price = float(price) <= 10
# print("Burger is within budget: ",is_price)

#LOGICAL OPERATORS are used to combine multiple conditions
#and -> both expressions are TRUE
#or -> at least one expression is TRUE
#not -> reverse the expression (TRUE becomes FALSE or vice versa)

# mars_choice = input('Would you like to visit Mars? y/n ')
# is_willing = mars_choice == 'y'
# affordable = input('Can you afford to visit Mars? y/n ')
# can_afford = affordable == 'y'
# should_visit_mars = is_willing and can_afford
# print('You should visit Mars: {}'.format(should_visit_mars))
# # y & n -> prints False

# Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian
# option The output should say whether the cost is within budget AND has a vegetarian option
# Restaurant meets criteria: True

# price = input("How much does the burger cost? ")
# is_price = float(price) <= 10
# veg = input("Does the restaurant have a vegetarian option? Y/N ")
# criteria = is_price and veg
# print("Restaurant meets criteria: ",criteria)

#IF STATEMENTS run a block of code depending on whether a condition is TRUE or FALSE
# password = input('password: ')
# if password == 'dinosaurs':
#     print('Success!')
#
# name = input("What is your name? ")
# is_admin = name == 'admin'
# password = input("What is your password? ")
# is_password_correct = password == 'dinosaurs'
# if is_admin and is_password_correct:
#     print('Welcome')
# if not is_admin or not is_password_correct:
#     print('Go away')

# Exercise 3.3: Rewrite the output of your burger program to use if statements
# If it is a good choice it should be:
# This restaurant is a great choice!
#
# If it is not a good choice it should be:
# Probably not a good idea

# price = input("How much does the burger cost? ")
# is_price = float(price) <= 10
# veg = input("Does the restaurant have a vegetarian option? Y/N ")
# has_veg = veg == "Y"
# criteria = is_price and has_veg
# #
# # #This prints whether it's a good choice or not based on whether the criteria are met
# if criteria:
#     print("This is a good choice!")
# if not criteria:
#     print("This is not a good choice")


#ELSE STATEMENTS used with an if statement, will only run if IF STATEMENT is FALSE
# password = input('password: ')
# if password == 'jumanji':
#     print('Success!')
# else:
#     print('Failure!')

# name = input("What is your name? ")
# is_admin = name == 'admin'
# password = input("What is your password? ")
# is_password_correct = password == 'dinosaurs'
# if is_admin and is_password_correct:
#     print('Welcome')
# else:
#     print('Go away')

# Exercise 3.4: Now that you've finished your burger, you want to pay for your food. Let's write a
# program to calculate your meal and apply a discount if applicable.
# If your total meal costs more than £20 AND you have a discount, the price will be reduced by 10%.
# The program should print "Discount applied" or "No discount" depending on whether the discount
# criteria was met.

# meal_price = float(input('How much did the meal cost? '))
# discount_choice = input('Do you have a discount? Y/N ')
#
# is_discount = discount_choice == "Y"
# over_twenty = meal_price >= 20
# discount_applicable = discount_choice == 'Y' and over_twenty
#
# if discount_applicable:
#     meal_price = meal_price * 0.9
#     print("Discount applied")
#
# else:
#     print("No discount")
#     print("Total cost: {}", meal_price)


#ELIF STATEMENTS are used after IF STATEMENTS to check whether another condition is True or False
#You can have multiple elif statements in one if statement

# dog_size = int(input('How big is the dog? '))
# if dog_size > 75:
#     print('That is a big dog')
# elif dog_size < 10:
#     print('That dog could fit in my pocket')
# elif dog_size < 25:
#     print('That is a small dog')
# else:
#     print('That is an average dog')

# Exercise 3.5: You're cooking a pizza and need to check that the oven is at the right temperature.
# Write a program to:
#
# Ask the user to input the temperature
# Prints "The oven is too hot" if the temperature is over 200
# Prints "The oven is too cold" if the temperature is under 150
# Prints "The oven is at the perfect temperature" if the temperature is 180
# Prints "The temperature is close enough" for any other temperature


#RANDOM - built in library for random data
# import random
# random_integer = random.randint(1, 100)
# print(random_integer)

# sides = int(input("How many sides does the dice have? "))
# random_integer = random.randint(1, sides)
# print("You rolled a ", random_integer)
