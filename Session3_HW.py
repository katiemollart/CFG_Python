# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

# raining = input("Is it raining? Y/N ")
# if raining == "Y":
#     print("Take an umbrella")
# else:
#     print("You don't need an umbrella")

# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

# my_money = int(input('How much money do you have? '))
# boat_cost = int(20 + 5)
# if my_money > boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')


# Question 3
# Your friend works for an antique book shop that sells books between 1800 and 1950
# and wants to quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century, Seventies")

def cat_year(year):
    if 1800 <= year <= 1899:
        century = "19th century"
    elif 1900 <= year <= 1950:
        century = "20th century"
    else:
        return("Year not in range")
    return century
year = int(input("Enter a year between 1800 and 1950: "))
print(cat_year(year))

#I can get this far but I don't understand how to do the decades