#This program will sort people into either Gryffindor, Hufflepuff, Ravenclaw, or Slytherin!

#Dictionary for the houses and point rankings
house_rank = {'Gryffindor':0, 'Slytherin':0, 'Hufflepuff':0, 'Ravenclaw':0}

#Import modules
import os
import time
import random

#Function to clear the screen
def clrscr():
    os.system('cls')
    print("\n\n")
    time.sleep(2)

#Function to skip lines
def skipline(x):
    line = "\n"
    print(line * x)

#Function to print text at different speeds
def printtext(x, y):
    if x != 0:
        for letter in x:
            print(letter, end="", flush=True)
            time.sleep(.05)
    else:
        if y != 0:
            for letter in y:
                print(letter, end="", flush=True)
                time.sleep(.2)

#Function for general text. Compiles the printext, time, and skipline functions
def gentext(printfast, printslow, sleep, line):
    printtext(printfast, printslow)
    time.sleep(sleep)
    skipline(line)

#Function for 2 optoin choices
def choice2(question, option1, option2, output1, output2, sleep, line):
    gentext(question, 0, 1, 0)
    #Prints the different choice options
    if option1 != 0:
        print("1.", option1)
    if option2 != 0:
        print("2.", option2)
    #Defines the available choices
    choice_yes = ['yes', 'yes!', '1']
    choice_no = ['no', 'no.', '2']
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    while True:
        ckey = input("> ").lower()
        time.sleep(2)
        if ckey in choice_yes:
            print('')
            gentext(output1, 0, 1, 0)
            break
        elif ckey in choice_no:
            print('')
            gentext(output2, 0, 1, 0)
            quit()
        #If one of the available choices was not a valid input,
        #cycles back through loop
        else:
            print("Why do you delay?")

#Function for 3-4 option choices
def choice4(question, option1, option2, option3, option4, output1, output2, output3, output4, sleep, line):
    gentext(question, 0, 2, 0)
    #Prints the different choice options
    if option1 != 0:
        print("1. ", end = "")
        gentext(option1, 0, 0, 0)
    if option2 != 0:
        print("2. ", end = "")
        gentext(option2, 0, 0, 0)
    if option3 != 0:
        print("3. ", end = "")
        gentext(option3, 0, 0, 0)
    if option4 != 0:
        print("4. ", end = "")
        gentext(option4, 0, 0, 0)
    #Defines the available choices
    choice_1 = ['1', 'one', 'first', 'spring', 'early', 'early bird', 'bird']
    choice_2 = ['2', 'two', 'second', 'summer', 'night', 'owl', 'night owl']
    choice_3 = ['3', 'three', 'third', 'fall', 'both']
    choice_4 = ['4', 'four', 'fourth', 'last', 'winter']
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    while True:
        ckey = input("> ").lower()
        time.sleep(2)
        print("")
        if ckey in choice_1:
            gentext(output1, 0, sleep, line)
            house_rank['Hufflepuff'] += 1
            break
        elif ckey in choice_2:
            gentext(output2, 0, sleep, line)
            house_rank['Gryffindor'] += 1
            break
        elif ckey in choice_3:
            gentext(output3, 0, sleep, line)
            house_rank['Ravenclaw'] += 1
            break
        elif ckey in choice_4:
            gentext(output4, 0, sleep, line)
            house_rank['Hufflepuff'] += 1
            break
        #If one of the available choices was not a valid input,
        #cycles back through loop
        else:
            print(random.choice(["Why do you delay?", "You must choose!", "...", "Hurry up! Others are waiting!", "Stay focused!"]))

#Function for last series of questions
def lastchoices(question, option1, option2, output1, output2, sleep, line):
    gentext(question, 0, 1, 0)
    #Defines the available choices
    gvalue_hvalue = ['1', 'freedom', 'indulgence', 'humility']
    svalue_rvalue = ['2', 'order', 'abstinence', 'boldness']
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    while True:
        ckey = input("> ").lower()
        time.sleep(1)
        if ckey in gvalue_hvalue:
            print('')
            gentext(output1, 0, 1, 0)
            house_rank['Gryffindor'] += 1
            house_rank['Hufflepuff'] += 1
            break
        elif ckey in svalue_rvalue:
            print('')
            gentext(output2, 0, 1, 0)
            house_rank['Slytherin'] += 1
            house_rank['Ravenclaw'] += 1
            break
        #If one of the available choices was not a valid input,
        #cycles back through loop
        else:
            print("Why do you delay?")

clrscr()

#First question
#Assigning text string to variable for to run through gentext() function
begin = "LET THE SORTING BEGIN!"
gentext(begin, 0, 1, 1)

question_1 = "Will you put on the sorting hat?"
option1 = "Yes!"
option2 = "No."
output1 = "At first nothing happens, but then you hear a deep voice in your head!"
output2 = "You have been expelled."
choice2(question_1, option1, option2, output1, output2, 2, 0)

#Second question
question_2 = "'What is your name?' Says the voice."
gentext(question_2, 0, 1, 0)

user_name = input("> ")
thank_you = "\n""Thank you " + user_name + ", now we can begin."
gentext(thank_you, 0, 2, 0)

hmmm = "Let's see..."
interesting = "...very interesting."
gentext(hmmm, 0, 2, 0)
gentext(interesting, 0, 2, 1)

#Third question
question_3 = "What season were you born in?"
output1 = "...I already knew that."
choice4(question_3, 0, 0, 0, 0, output1, output1, output1, output1, 2, 0)

#Fourth quesion
question_4 = "Are you an early bird or a night owl?\nOr perhaps both?"
output1 = "Hmmm.....yes.....\nLet's continue."
output2 = "You must be wise and have worms."
choice4(question_4, 0, 0, 0, 0, output1, output1, output2, 0, 2, 0)

#Fifth question
question_5 = "Now...what are you more afraid of?"
option1 = "Obscurity"
option2 = "Failure"
option3 = "Powerlessness"
option4 = "Abandonment"
output1 = "...good...very good."
choice4(question_5, option4, option3, option1, option2, output1, output1, output1, output1, 2, 0)

#Sixth question
question_6 = "Which do you value more?"
option1 = "Leadership"
option2 = "Courage"
option3 = "Loyalty"
option4 = "Creativity"
output1 = "...most curious..."
choice4(question_6, option3, option2, option4, option1, output1, output1, output1, output1, 2, 0)

#Seventh question
question_7 = "What pleases you more to hear?"
option1 = "The air is fresh."
option2 = "The earth is solid."
option3 = "The water is cool."
option4 = "The fire is warm."
output1 = "...I suspected as much."+"\n"+"No matter, we are almost done."
choice4(question_7, option2, option4, option1, option3, output1, output1, output1, output1, 2, 0)


#Last series of questions
question_8 = "Freedom or order?"
question_9 = "Indulgence or abstinence?"
question_10 = "Humility or boldness?"
output1 = "Too much freedom is choas."
output2 = "Too much order is tyranny."
output3 = "You'll be pleased to hear the Welcoming Feast is next!"
output4 = "You'll be sorely tested at the Welcoming Feast!"
output5 = "Well, you should be."
output6 = "May fortune favor the foolish."
lastchoices(question_8, 0, 0, output1, output2, 2, 0)
lastchoices(question_9, 0, 0, output3, output4, 2, 0)
lastchoices(question_10, 0, 0, output5, output6, 2, 0)

#Results
new_house_rank = []
for key, value in house_rank.items():
    if value == max(house_rank.values()):
        new_house_rank += [key]

#Reset option variables to 0
option1 = 0
option2 = 0
option3 = 0
option4 = 0

difficult = "Hmm...now where to put you?\nDifficult, very difficult..."
gryffquote = "Plenty of courage I see, as befitting one in Gryffindor."
ravenquote = "...not a bad mind, Ravenclaw would be a good fit."
huffquote = "An abundence of determination, you could be in Hufflepuff."
slythquote = "Or will it be Slytherin? You could be great, and Slytherin will help you on your way to greatness."
which_to_choose = "\nWhich house will you choose?"
last_line = "So be it..."
#If houses are tied for most points, this will run
selected_house = ''
if len(new_house_rank) > 1:
    gentext(difficult, 0, 2, 0)
    #Looks for a specific house in list and assigns it to a variable in lower case
    if 'Gryffindor' in new_house_rank:
        option1 = 'Gryffindor'.lower()
        gentext(gryffquote, 0, 2, 0)
    if 'Hufflepuff' in new_house_rank:
        option2 = 'Hufflepuff'.lower()
        gentext(huffquote, 0, 2, 0)
    if 'Ravenclaw' in new_house_rank:
        option3 = 'Ravenclaw'.lower()
        gentext(ravenquote, 0, 2, 0)
    if 'Slytherin' in new_house_rank:
        option4 = 'Slytherin'.lower()
        gentext(slythquote, 0, 2, 0)
    gentext(which_to_choose, 0, 1, 0)
    #List of avaiable choices
    choice_a = ['1', 'one', 'first', option1]
    choice_b = ['2', 'two', 'second', option2]
    choice_c = ['3', 'three', 'third', option3]
    choice_d = ['4', 'four', 'fourth', 'last', option4]
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    selected_house = ''
    while True:
        ckey = input("> ").lower().strip()
        gentext(0, ".....", 2, 0)
        if ckey == option1:
            selected_house = option1
            gentext(last_line, 0, 1, 0)
            break
        elif ckey == option2:
            selected_house = option2
            gentext(last_line, 0, 1, 0)
            break
        elif ckey == option3:
            selected_house = option3
            gentext(last_line, 0, 1, 0)
            break
        elif ckey == option4:
            selected_house = option4
            gentext(last_line, 0, 1, 0)
            break
        else:
            gentext("That is not an option!", 0, 1, 0)
else:
    selected_house = new_house_rank[0]

#Closing statement
clrscr()
gentext(0, "Your new house is.....", 2, 1)
gentext(selected_house.upper()+"!!!!!", 0, 5, 0)
