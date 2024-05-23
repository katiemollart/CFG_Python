# Question 1
# Explain what this program does
# for number in range(100):
#     output = 'o' * number
# print(output)
# #prints "o" 100x

# Question 2
# Your boss really likes calculating VAT on their purchases. It is their favourite hobby.
# They've written this code to calculate VAT and need your help to fix it.
def calculate_vat(amount):
    amount * 1.2
    return amount * 1.2

total = calculate_vat(100)
print(total)

#or line 3: return print(amount * 1.2)


# When your boss runs the program they get the following output:
# None
# Your boss expects the program to output the value 120. What is wrong? How do you fix it?

#needed to have code to return the function
#i just got it to print 120 but not sure how