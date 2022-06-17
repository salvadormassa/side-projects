#!/usr/bin/env python3

import random
import time
import os
import sys

# Complete deck of 52 cards
deck = [
    'Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs',
    'Five of Clubs', 'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs',
    'Nine of Clubs', 'Ten of Clubs', 'Jack of Clubs', 'Queen of Clubs',
    'King of Clubs', 'Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds',
    'Four of Diamonds', 'Five of Diamonds', 'Six of Diamonds',
    'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds',
    'Ten of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
    'King of Diamonds', 'Ace of Hearts', 'Two of Hearts', 'Three of Hearts',
    'Four of Hearts', 'Five of Hearts', 'Six of Hearts', 'Seven of Hearts',
    'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts', 'Jack of Hearts',
    'Queen of Hearts', 'King of Hearts', 'Ace of Spades', 'Two of Spades',
    'Three of Spades', 'Four of Spades', 'Five of Spades', 'Six of Spades',
    'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades',
    'Jack of Spades', 'Queen of Spades', 'King of Spades'
    ]

# Clears terminal screen
def clrscr():
    try:
        os.system('cls')
    except Exception:
        pass
    print("\n")
    time.sleep(2)

# General print function
def printtext(x, y):
    if x != 0:
        for letter in x:
            print(letter, end="", flush=True)
            time.sleep(y)

# Prints text in a (string)... format
def iterate_dots(text):
    time.sleep(.5)
    printtext(text, .05)
    time.sleep(.5)
    print('.', end='', flush=True)
    time.sleep(.5)
    print('.', end='', flush=True)
    time.sleep(.5)
    print('.', flush=True)
    time.sleep(.5)

# Removes player column from group, randomly shuffles the remaining 2,
# then re-inserts user column
def shuffle_columns():
    remove_column = columns.pop(user_input-1)
    random.shuffle(columns)
    columns.insert(1, remove_column)
    return columns

# With the 'stack' of 21 cards, lays each card down from left to right
# in 3 columns of 7. Then regroups columns.
def lay_down_columns(columns):
    print('------------------------------------------------------------')
    x = 0
    new_column_1 = []
    new_column_2 = []
    new_column_3 = []
    for column in columns:
        for card in column:
            # print(card)
            print(f"{card: ^20}", end='', flush=True)
            time.sleep(.2)
            x += 1
            if x == 1:
                new_column_1 += [card]
            elif x == 2:
                new_column_2 += [card]
            elif x == 3:
                new_column_3 += [card]
                print('')
                x = 0
    print('------------------------------------------------------------')
    columns = [new_column_1, new_column_2, new_column_3]
    return columns

# Clears initial screen
clrscr()

# Start of program
intro = "\nThis program will guess your card!\n"
printtext(intro, .05)
time.sleep(2)

# Grabs 21 random cards from the deck
random_21 = random.sample(deck, k=21)
print('--------------------')
for card in random_21:
    print("{:^20}".format(card))
    time.sleep(.1)
print('--------------------')
time.sleep(2)

# Stage 1, player picks card, deck is shuffled
pick_card = "Pick a card, memorize it, and shuffle the cards.\n"
type_ok = "Type OK to shuffle cards: "
shuffling = "Shuffling"
printtext(pick_card, .05)
time.sleep(1)
while True:
    printtext(type_ok, .05)
    user_input = input()
    if user_input.upper() != 'OK':
        continue
    break
iterate_dots("Shuffling")
# Shuffle the 21 cards
random.shuffle(random_21)

# Stage 2, split cards into 3 groups for player to identify their card
column_1 = random_21[0:7]
column_2 = random_21[7:14]
column_3 = random_21[14:21]
columns = [column_1, column_2, column_3]
# Print 3 columns of cards, asks player to find their card in columns
deal_columns = "Three columns of cards are layed out in front of you.\n"
which_column = "Is your card in column 1, 2, or 3? "
printtext(deal_columns, .05)
columns = lay_down_columns(columns)
printtext(which_column, .05)
while True:
    try:
        user_input = int(input())
        break
    except ValueError:
        continue

# Stage 3, regroup card with player selected column in the middle. Repeat
merge_columns = "The cards are put back together and again layed out in front of you.\n"
columns = shuffle_columns()
printtext(merge_columns, .05)
columns = lay_down_columns(columns)
printtext(which_column, .05)
while True:
    try:
        user_input = int(input())
        break
    except ValueError:
        continue

# Stage 4, Repeat
last_time = "The cards are put back together and for a third time are dealt.\n"
columns = shuffle_columns()
printtext(last_time, .05)
columns = lay_down_columns(columns)
printtext(which_column, .05)
while True:
    try:
        user_input = int(input())
        break
    except ValueError:
        continue

# Stage 5, columns are put back together and their card is revealed
# Their card will be the 11th fron the 'top', or the 4th in the middle column
columns = shuffle_columns()
iterate_dots("Calculating")
print(f'Is {columns[1][3]} your card? ', end='')
while True:
    user_input = input()
    if user_input[:3].lower() == 'yes':
        printtext("It's magic!!!", .1); time.sleep(2)
        sys.exit()
    elif user_input[:2].lower() == 'no':
        printtext("I hope you learned something here.", .05); time.sleep(2)
        sys.exit()
    else:
        print("Was that your card?")
        continue
