#Create a program that calculates how many cans of cat food you need to feed 10 cats

cat_number = 10
cans_number = 2
print("The number of cans needed to feed 10 cats a day is:", cat_number * cans_number)
cans_daily = cat_number * cans_number
print(cans_daily)
print("The number of cans needed to feed the 10 cats for a week is:", cans_daily * 7)

cat_output = "{} cats eat {} cans a day, which equals {} cans needed daily".format(cat_number, cans_number, cans_daily)
print(cat_output)