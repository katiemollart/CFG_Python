## FILES

# with open('people.txt', 'w+') as text_file:
#     people = 'Joanne \nSusan \nAmina' #\n makes it start on a new line
#     text_file.write(people) #WRITING TO A FILE - this adds "Joanne Susan Amina" to text_file
#
# with open('people.txt', 'r') as text_file:
#     contents = text_file.read() #READING TO A FILE - this puts whatever the text_file is holding into the contents variable
# print(contents)

# Exercise 5.1: Create a to-do list program that writes user input to a file
# The program should:
#
# Ask the user to input a new to-do item
# Read the contents of the existing to-do items
# Add the new to do item to the existing to-do items
# Save the updated to-do items
# You will need to manually create a new file called #todo.txt in the same folder as your program before you start

# new_item = input('Enter a to-do item: ')
# with open('todo.txt', 'r') as todo_file:
#     todo = todo_file.read()
# todo = todo + new_item + '\n'
# with open('todo.txt', 'w+') as todo_file:
#     todo_file.write(todo)
# print(todo)

#WORKING WITH CSV FILES

#WRITING A CSV
# import csv
# field_names = ['name', 'age']
# data = [
#     {'name': 'Jill', 'age': 32},
#     {'name': 'Sara', 'age': 28},
# ]
# with open('team.csv', 'w+') as csv_file:
#     spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
#
#     spreadsheet.writeheader()
#     spreadsheet.writerows(data)

# READING A CSV
# import csv
# with open('team.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     for row in spreadsheet:
#         print(dict(row)) #This prints all the data in the CSV we wrote above

# Exercise 5.2: This program is supposed to read data about trees from a file to find the shortest tree.
# Complete the program adding code to open trees.csv. The trees.csv file included with your student guides.
# Save the csv file in the same folder as your Python program.

# import csv
#
# with open("trees.csv", "r") as csv_file:
#     spreadsheet = csv.DictReader(csv_file) # Added code to open the csv file
#
#     heights = []
#     for row in spreadsheet:
#         tree_height = row['height']
#         heights.append(tree_height)
# shortest_height = min(heights)
# print(shortest_height)

## PIP - package manager used to install libraries that others have written
# used via the command line (terminal)

## API - application programming interface
# a way for diff programs to interact e.g. sending data to one another
# web APIs allow you to interact w other programs over the internet

# API request - when your program asks an API for something or to complete a specific action
# API response - the result of your request from the API

# import requests
# from pprint import pprint
# pokemon_number = input("What is the Pokemon's ID? ")
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# response = requests.get(url)
# print(response)
# pokemon = response.json()
# pprint(pokemon)

# response status codes
# 200 - OK - request worked
# 404 - not found - couldn't find URL requested
# 400 - bad request - request you made isn't understood

# Exercise 5.3: Get the height and weight of a specific Pokemon and print the output
import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()
print("Pokemon name: ",(pokemon["name"]))
print("Pokemon height: ",(pokemon["height"]))
print("Pokemon weight: ", (pokemon["weight"]))