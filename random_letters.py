#!/usr/bin/env python
# coding: utf-8

# In[84]:


import random

#Creates a text file "random_words.txt".
#Prints 1000 lines of 4-6 random sets of 8 bits.
# In[161]:


def random_8_bits(file):
    x = 0
    for n in range(9):
        #Generate a 1 or 0 at random.
        rnum = random.randint(0, 1)
        #Add a space after every 8 bits.
        if x == 8:
            file.write(' ')
        #Write a 1/0 to file then add 1 to x.
        else:
            file.write(str(rnum))
            x += 1
    
def random_word():
    with open('random_bits.txt', 'a') as file:
        for n in range(0, random.randint(4, 7)):
            random_8_bits(file)
        file.write('\n')
        
def lines_to_print():
    for n in range(0, 100000):
        random_word()
        
lines_to_print()

#Covert bit sets in "random_words.txt" to unicode characters.
# In[162]:


def is_a_letter(letter):
    #Check is character is in the alphabet.
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        if letter in alphabet:
            return 1
        else:
            return 0
    except:
        print('')

def byte_to_unicode(byte):
    #Convert each byte into its equivalent number.
    number = int(byte, 2)
    #Convert each number into a unicode character.
    character = chr(number)
    return character
    #Check is character is in the alphabet.
            
def generate_words():
    with open('random_bits.txt') as infile:
        with open('random_characters.txt', 'a') as outfile:
            for line in infile:
                word = ''
                byte_list = line.split()
                #Iterate through each byte.
                for byte in byte_list:   
                    #Convert byte to unicode character.
                    letter = byte_to_unicode(byte)
                    #Check is character is in the alphabet.
                    result = is_a_letter(letter)
                    if result == 1:
                        word += letter.lower()
                    else:
                        break
                if len(word) > 3:
                    outfile.write(word+'\n')

generate_words()


# In[ ]:




