import csv #this allows program to open csv files
import random #this allows program to use 'random' module
from operator import itemgetter #this sorts the list of scores at the end of the game


print("Welcome to the Music Quiz!")
print("\n")
print("┊☆┊┊┊┊☆┊┊┊┊Nyan Cat")
print("┈┈┈┈╭━━━━━━╮┊☆┊┊")
print("┈┈┈┈┃╳╳╳▕╲▂▂╱▏┊┊")
print("┈┈┈┈┃╳╳╳▕▏▍▕▍▏┊☆")
print("┈┈╰━╳╳╳▕▏╰┻╯▏┊┊")
print("┈┈┈┈┃╳╳╳╳╲▂▂╱┊┊┊")
print("┊┊☆┊╰┳┳━━┳┳╯┊┊☆┊")
print("\n")
print(" ☆   MAIN MENU  ☆  ")
print("\n")


login = input("Do you have an account? Y or N: ").upper()

if login == "Y":
    csvfile = open("userfile.csv")
    reader = csv.reader(csvfile)

    login =  False
    while login == False:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for row in reader:
            if row[0] == username:
                if row[1] == password:
                    print("Welcome to the game!")
                    login = True
else:
    print("You are not authorised.")
        
score = 0
incorrect = False
while incorrect != True: #this uses a while loop so that questions will repeat
    #until player gets 2 questions wrong and incorrect is set to true
    with open("songlist.csv") as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader)) #the contents of the file are placed into a list
        #randomly chooses one of the elements in the list
        #assigned to the variable chosen_row
        title = chosen_row[1].split()
        letters = [word[0] for word in title]
        print (chosen_row[0], " ", " ".join (letters))
    answer = input("Enter your answer: ")
    if answer == chosen_row[1]:
        print("Correct! You get 3 points.")
        score = score + 3
    else:
        print("Incorrect.")
        guess2 = input("Try again: ")
        if guess2 == chosen_row[1]:
            print("Correct! You get 1 point.")
            score = score + 1
        else:
            print("Sorry, that is wrong.")
            incorrect = True #this changes value of incorrect to true so while loop ends
            f.close()#this closes the csv file
print ("Your score is ",score)

score_file = open("scores1.csv","a")
score = str(score) #this line converts the score to a string so that it can be appended to a csv file
details = (username + "," + score)
score_file.write(details + "\n") #this line writes the score to the csv file containing the scores
score_file.close()

score_file = open("scores1.csv","r") #this opens the csv file
reader = csv.reader(score_file) #this places it in the reader
my_list = list(reader) #this places the contents of the csv as a list in the reader
for i in my_list:
    i[1] = int(i[1]) #this converts the score into an integer so it can be sorted properly
sorted_list = sorted(my_list, key = itemgetter(1), reverse = True)
print("The top 5 scores are: \n", sorted_list[0:5]) #this manipulates the list so that only the top 5 scores in the list are shown
