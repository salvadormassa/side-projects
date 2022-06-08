#Imports the random module
import random

#Creates an index of the students' names
students = ['Angel', 'Asim', 'Ericka', 'Hibo', 'Jacob', 'John', 'Junwon', 'Markus', 'Pang', 'Priya', 'Rida', 'Sarah', 'Sebastian', 'Tanner', 'Zuneem']

#First loop to run until the index in emtpy
while students > [] :
    print('Please press enter for a student.')
    key = input(str())
    #Second loop in case anything other than the enter key is pressed
    while key != '' :
        print('You must only press enter!')
        print('')
        print('Please press enter for a student.')
        key = input(str())
    #Part of the first loop that adds a random name from students and assigns it to ranstu
    ranstu=random.choice(students)
    print(ranstu+'!')
    print('')
    #The remove() function removes the student from the students list
    students.remove(ranstu)

print('Nice job everyone!')
