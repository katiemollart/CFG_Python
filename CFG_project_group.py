import requests
from pprint import pprint


def recipe_search(ingredient, health_label = None, meal_type = None):
    app_id = '1894ea27'
    app_key = '4932e642ba6532369e48374398d1bfc3'

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    if meal_type:
        url += '&mealType={}'.format(meal_type)  #if a meal type is given, this appends it to the URL request

    if health_label:
        url += '&health={}'.format(health_label)  #if a dietary req is given, this appends it to the URL request

    result = requests.get(url)
    data = result.json()
    return data['hits']


def run_search():
    ingredient = input('Enter an ingredient: ')
    meal_type = input('Enter any meal type (breakfast/lunch/dinner/snack) or press enter for N/A: ')  # this corresponds to the meal type in the API document
    health_label = input('Enter any dietary requirements (vegetarian/vegan/pescetarian/gluten-free) or press enter for N/A: ')  #this corresponds to the health labels in the API document
    print("\n" + "Here are your recipes: ")
    results = recipe_search(ingredient, health_label, meal_type)  #searches by ingredient & dietary req & meal type

    if not results:
        print("No recipes found.") # message if no recipe found

    with open("recipes.txt", "w+") as text_file:
        for result in results:
            recipe = result['recipe']
        # Write the recipe details to the file
            text_file.write("Recipe Name: " + recipe['label'] + "\n")
            text_file.write("Recipe URL: " + recipe['url'] + "\n")
            text_file.write('\n')

        # Also print the recipe details to the console
            print('Recipe Name:', recipe['label'])
            print('Recipe URL:', recipe['url'])
            print()

    print("Recipes have been saved to recipes.txt")


run_search()