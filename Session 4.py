#####LISTS
#Ordered collections of values/items
#Written in [] and separated by ,
#Can hold one or various data types

# lottery_numbers = [4, 8, 15, 16, 23, 42]
# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

#Values in list can be accessed through their index in square brackets
# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# print(student_names[2]) ##Prints "Helena"

#To change a value in a list:
#list_name[index] = "value"

# student_names = [
# 'Diedre', # index 0
# 'Hank', # index 1
# 'Helena', # index 2
# 'Salome' # index 3
# ]
# student_names[1] = 'Joshua'
# print(student_names)

# Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes. Let's write a
# program to help me to remember the right clothes.
# The program should check if the first item in the clothes list is "shorts" . If it is it should change the value to "warm coat" .

# clothes = ["shorts", "shoes", "t-shirt",]
# if clothes[0] == "shorts":
#     clothes[0] = "warm coat"
# print(clothes)


### LIST FUNCTIONS
# len(): the number of items in a list
# max(): The biggest value in a list
# min(): The smallest value in a list
#min & max only work on integers, could character count strings w number of characters in an item


# costs = [1.2, 4.3, 2.0, 0.5]
# print("Number of items: ",len(costs))
# print("Biggest value: ",max(costs))
# print("Smallest value: ",min(costs))

#Change order of list:
#sorted(list) sorts it
#reversed(list) reverses it (doesn't set to descending order it just flips the order of numbers

# costs = [1.2, 4.3, 2.0, 0.5]
# print(sorted(costs))
# print(list(reversed(costs)))


# Exercise 4.2: Make a list of game scores. Using list functions write code to output information of the
# scores in the following format:
# Extension: Output all of the scores in descending order

# Number of scores: 10
# Highest score: 200
# Lowest score: 3

# scores = [3, 56, 25, 25, 170, 89, 94, 160, 200, 194]
# print("Number of scores: ",len(scores))
# print("Highest score: ",max(scores))
# print("Lowest score: ",min(scores))
#
# #For descending order, sort list first (makes ascending) into a new variable then reverse new variable
# sorted_scores = (sorted(scores), reverse == True)
# print(sorted_scores)


#append() can add elements to end of list ONLY
# students = [
# 'Diedre', 'Hank', 'Helena', 'Salome',
# ]
# print("List of students: ",students)
# student_name = input('What is the name of the new student? ')
# students.append(student_name)
# print("List of new students: ",students)

# 'in' operator can check if a value is in the list (TRUE or FALSE)

# student_name = input('Which student are you looking for? ')
# students = [
# 'Diedre', 'Hank', 'Helena', 'Salome',
# ]
# if student_name in students:
#     print('{} is in the class'.format(student_name)) #TRUE
# else:
#     print('{} is not in the class'.format(student_name)) #FALSE


# Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list
# and if 'bread' is in the list, add 'butter' to the shopping list.
# Try running the program with and without bread in the list to check that your program works.
# Remember the in operator checks if an item is in a list and the .append() method adds an item to a
# list.

# shopping_list = ["bread", "milk", "eggs"]
# has_butter = "butter"
# if "bread" in shopping_list:
#     shopping_list.append("butter")
#     print(shopping_list)
#
# if "bread" not in shopping_list:
#     print("You don't need butter")


## LISTS AND FOR LOOPS TOGETHER

# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# count = 0
# for i in student_names:
#     print(i) #Looping through list to print each element in the list
#
# for i in student_names:
#     count = count + 1
# print(count) #Prints total no of items in the list


# Exercise 4.4: I want to work out how much money I've spent on lunch this week. I've created a list of
# what I spent each day.
# Write a program that uses a for loop to calculate the total cost

# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
#
# for cost in costs:
#     total_cost = total_cost + cost
# print(round(total_cost))
## or do sum(costs)

###### DICTIONARIES
##Stores a collection of labelled items. Each item has a key and a value
## key: value, key: value

# person = {
# 'name': 'Jessica',
# 'age': 23,
# 'height': 172
# }

# #values are accessed using their keys
# variable[key]
# print(person["name"])

# Exercise 4.5: Print the values of name , post_code and street_number from the dictionary

# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127,
#         'latitude': 63,
#     }
# }
# print(place["name"])
# print(place["post_code"])
# print(place["street_number"])
#
# print(place["location"]["longitude"])
# print(place["location"]["latitude"])

### DICTIONARIES IN LISTS

# people = [{'name': 'Jessica', 'age': 23}, {'name': 'Trisha', 'age': 24},]
# for person in people:
#     print(person['name'])
#     print(person['age'])


# Exercise 4.6: Using a for loop, output the values name , colour and price of each dictionary in the list

# fruits = [
# {'name': 'apple', 'colour': 'red', 'price': 0.12},
# {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
# {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for element in fruits:
#     print(element['name'])
#     print(element['colour'])
#     print(element['price'])

#RANDOM CHOICE
# import random
# colours = ['red', 'green', 'blue']
# chosen_colour = random.choice(colours)
# print(chosen_colour) #chooses btwn red/green/blue at random

# Exercise 4.7: Write a program to create a random name. You should have a list of random firstnames and a list of lastnames.
# Choose a random item from each and display the result.
# Extension: Using list of verbs and a list of nouns, create randomised sentences

import random
firstnames = ["katie", "molly", "ken"]
chosen_firstname = random.choice(firstnames)
surnames = ["mollart", "bre", "kins"]
chosen_surnames = random.choice(surnames)
print(chosen_firstname, chosen_surnames)