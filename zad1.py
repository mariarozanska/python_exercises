'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)'''

import datetime as dt

name = input('Name: ')
age = int(input('Age: '))
copies = int(input('Copies: '))

year100 = dt.datetime.now().year + (100 - age)

for i in range(copies):
    print('%s will be 100 in %i' % (name, year100))