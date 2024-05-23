# #User input
# age = input('What is your age? ')
# print('Hello, I am {} yo'.format(age))
# #Exercise 2.1: Write a program that asks two questions using input() then prints the values that were entered. You can choose any questions that you want.
# country = input("What country are you from? ")
# print(f"I am from {country}")
# pets = input("How many pets do you have? ")
# print(f"I have {pets} pets")
# print(f"You are {age} years old, you are from {country} and you have {pets} pets. Cool!")
#
# #input() always returns a string, which can be changed to an integer
# #to turn string values into integer values, use int()
# apples_string = '12'
# total_apples = int(apples_string) + 5
# print(total_apples)
#
# Exercise 2.2: You have friends at your house for dinner and you've accidentally burnt the lasagne.
# Time to order pizza. Write a program calculate how many pizzas you need to feed you and your friends

# friends = int(input("How many friends do you have at home? "))
# pizzas = friends * 0.5 # everyone gets half each
# print(f"You should order {pizzas} pizzas for {friends} friends")


##Python Modules
#modules are code another person has wrote that you can reuse in your programs
#import name of program e.g.
# import datetime
#
# current_time = datetime.datetime.now()
# print(current_time)
#
# my_date = datetime.date(2024, 2, 23)
# print(my_date.strftime("%d-%b-%Y")) #prints 23-Feb-2024
# print(my_date.strftime("%A %d %B %Y")) #prints Friday 23 February 2024

#FOR LOOPS let you repeat a code block multiple times
# for every N, do something
#
# for number in range(5):
#  print(number) #prints every number below 5
# for character in 'Banana':
#  print(character) #prints every letter in banana
#
# # think of this examples as a box with words, we are doing an action for each word #NB: this is called a 'list' but we will learn about it later in the course, this is only an example fo r now.
# for name in ['Mary', 'Ranjit', 'Fatima']:
#  print(name)
#
# total = 0
# print("*** This statement is OUTSIDE THE LOOP")
# print("Before the loop executes, our TOTAL is equal to = ", total, '\n')
# print("--------------------------------------------------------")
# for number in range(3):  # remember --> 0, 1, 2
#     print("This is loop execution for digit: " + str(number) + " inside the loop \n")
#     print("Updating total... (+ 1) \n")
#
#     total = total + 1  # every time the loop executes, we add 1 to the total
# print("--------------------------------------------------------")
# print("***This statementWe is OUTSIDE the loop now")
# print("The final TOTAL value is: " + str(total))
#
# A WHILE LOOP in python is used to iterate over a block of code or statements as long as the test expression is true.
#Be careful of infinite while loops -> can use tons of memory & cause program error

#Due to social distancing, only 10 people are allowed to be inside a shot at the same time.
#This program invites people in the queue to come in while we have some capacity.

# store_capacity = 10 #
# while store_capacity > 0:
#  print('Please come in. Spaces available: ' + str(store_capacity))
#  store_capacity = store_capacity - 1 #if you removed this, it would create an infinite loop
# print("\nPlease wait for someone to exit the store.")
#This prints the number of spaces available, decreasing as 1 person enters each time
# until spaces = 0. then, tells you to wait for someone to exit

#FUNCTIONS are reusable code blocks, containing 1+ python statements & used for performing specific tasks
#good for reusability, readability & avoiding redundancy
#to define a function, use `def keyword():`
#to call a function, use `keyword()`

def hello():
 print("Hello world!")
hello()

#sending info to functions is called "passing arguments"
#arguments are declared after the function name in brackets
#When you call a function with arguments, the values of those arguments are copied to their corresponding parameters inside the function.

#pass single argument to a function:
# def hello(name):
#  print('Hello,', name)
# hello('Maria')
# hello('Kim')
# hello('Lucy')

#Pass multiple arguments:
# def some_function(name, job):
#  print(name, 'is a', job)
# some_function('Fiona', 'developer')

# Positional arguments values are copied to their corresponding parameters in order.
# You must pass arguments in the order in which they are defined e.g. the lines above this.

#you can pass arguments using the names of their corresponding parameters. in this case, the order of the arguments no longer matters.
#you can combine positional and keyword arguments in a single call.
# if you do so, specify the positional arguments before keyword arguments.
# def some_function(name, job):
#  print(name, 'is a', job)
# some_function(job='writer', name='Fiona')
# some_function(name='Fiona', job='author')

#RETURNING VALUES FROM A FUNCTION - simply use a return statement
#Once a return statement is executed, nothing else in the function body is executed.
# def sum(x, y):
#  return x + y
# result = sum(10, 15)
# print("result is: {}".format(result))

#Exercise 2.6: Complete the function to return the area of a circle
#Use the comments to help you
def circle_area(radius):
 area = 3.14 * (radius ** 2)
 return area
area = circle_area(9)
print(area)


def days_in_hours(days):
 hours = days * 24
 return hours
print(days_in_hours(10))


def times_two(num):
 result = num * 2
 return result
for number in range(3):  # 0,1,2
 calc_res = times_two(number)
print(calc_res)