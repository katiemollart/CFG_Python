#I am building some very high quality chairs and need exactly four nails for each chair.
#I've written a program to calculate how many nails I need to buy to build these chairs.


#When I run the program it tells me that I need to buy 15151515 nails.
#This seems like a lot of nails. Is my program calculating the total number of nails correctly?
#What is the problem? How do I fix it?

#chairs value is a string, nails value is an integer - the code's printing the "chairs" value x4
#also can get rid of the 4th line of code, as this makes the print messy
# can just have print("You need to buy {} nails".format(total_nails) & bypass "message" variable

chairs = 15
nails = 4
total_nails = chairs * nails
print("You need to buy {} nails".format(total_nails))


#I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix the program?
my_name = "Penelope"
my_age = 29
#message = 'My name is {} and I am {} years old'.format(my_name, my_age)

#or:
message = f"My name is {my_name} and I am {my_age} years old"
print(message)

#NameError: name 'Penelope' is not defined
#Penelope needs to be a string



#I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
#but I should be able to easily change these values if I want.
#The output should say something like "You can make 9 omelettes with 6 boxes of eggs".

eggs_per_box = 6
boxes = int(input("How many boxes of eggs do you have? "))
print("There are {} eggs in one box".format(eggs_per_box))
eggs_per_omelette = 4
print("You need {} eggs for one omelette".format(eggs_per_omelette))

total_no_eggs = (boxes * eggs_per_box)
no_omelettes = int(total_no_eggs / eggs_per_omelette)
print("You can make {} omelettes with {} boxes of eggs".format(no_omelettes,boxes))