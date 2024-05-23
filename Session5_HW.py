# Question 2
# This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w+') as text_file:
#     text_file.write(poem)
#
# with open("poem.txt", "r") as text_file:
#     contents = text_file.read()
# print(contents)

# Question 3
# In this session you used the Pokemon API to retrieve a single Pokemon.
# I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each Pokemon.
# Save their names and moves into a file called 'pokemon.txt'

import requests
import random
from pprint import pprint

pokemon_id_list = [1, 2, 3, 4, 5, 6]

with open("pokemon.txt", "w") as text_file:
    for pokemon_id in pokemon_id_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
            pokemon_name = pokemon["name"]
            pokemon_moves = [move["move"]["name"] for move in pokemon["moves"]]
            text_file.write(f'Name: {pokemon_name}\n')
            text_file.write(f'Moves: {", ".join(pokemon_moves)}\n\n')
        else:
            text_file.write(f'Failed to retrieve data for Pokemon ID: {pokemon_id}\n\n')

with open('pokemon.txt', 'r') as text_file:
    contents = text_file.read()
print(contents)


