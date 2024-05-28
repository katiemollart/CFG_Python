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
from pprint import pprint
def recipe_search(ingredient, health_label=None):
    app_id = '1894ea27'
    app_key = '4932e642ba6532369e48374398d1bfc3'

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    if health_label:
        url += '&health={}'.format(health_label) #if a dietary req is given, this appends it to the URL request

    result = requests.get(url)
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    health_label = input('Enter any dietary requirements (e.g., vegetarian/vegan/pescetarian/gluten-free) or press enter if N/A: ') #this corresponds to the health labels in the API docu

    results = recipe_search(ingredient, health_label) #searches by ingredient & dietary req
    for result in results:
        recipe = result['recipe']
        print('Recipe Name:', recipe['label'])
        print('Recipe URL:', recipe['url'])
        print()

run()

#Come up with a line that shows which dietary requirement you've selected
#Print?
