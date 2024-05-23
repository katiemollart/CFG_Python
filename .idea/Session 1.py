print("Hello, world")
#single quotes ' ' or double quotes " " for strings
print("My name is Katie!")

#integers - whole numbers
#floats - decimal numbers

print(5-6)
print("5 - 6 equals:", 5-6)
#^ prints the sum as part of the sentence

#print(6/0)
#cannot divide by 0!
print(5%2)
#prints the remainder of a division

print(2**4)
# x ** y -> x to the power of y

print("cat")
print("cat" + "videos")
print("cat" * 3)

#print("cat" + 3)
#gives error "can only concatenate str (not "int") to str"
#to fix - put the number in str()
print("cat" + str(3))
# -> cat3

print("Cat".upper())
#prints 'CAT'
#everything before the . is uppercase
print("Cat".lower())
#prints 'cat'
##everything before the . is lowercase
print("the lord of the rings".title())
#capitalises each word in string

#.upper(), .lower() & .title() are METHODS - like functions, but tied to a specific data type
#eg .upper() can only be used w a string

#setting up variables
food = "spaghetti"
print("A type of pasta is", food)
print(f"This is my favourite food: {food}")
#f string - allows code to know there's a variable there

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
print(str(oranges) + " oranges")
print("costs " + str(total_cost))

#strings have a method .format() which subs placeholders for values
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)