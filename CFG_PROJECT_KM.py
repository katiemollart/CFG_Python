### EDAMAM API LINK
# https://api.edamam.com/search?q={INGREDIENT}&app_id=1894ea27&app_key=4932e642ba6532369e48374398d1bfc3

# APP ID:
# 1894ea27
# APP KEY:
# 4932e642ba6532369e48374398d1bfc3

# 1. Ask the user to enter an ingredient that they want to search for
# 2. Create a function that makes a request to the Edamam API with the required ingredient as part of the search query
# (also included your Application ID and Application Key
# 4. Get the returned recipes from the API response
# 3. Display the recipes for each search result

import requests

def recipe_search(ingredient):
    app_id = "1894ea27"
    app_key = "4932e642ba6532369e48374398d1bfc3"

    result = requests.get("https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key))
    data = result.json()

    return data["hits"]

def run():
    ingredient = input("Search for an ingredient: ")  # PART 1
    results = recipe_search(ingredient)

    for result in results:
        recipe = result["recipe"]
        print(recipe["label"])
        print(recipe["url"])

run()