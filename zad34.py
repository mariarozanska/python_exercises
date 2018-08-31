'''This exercise is Part 2 of 4 of the birthday data exercise series.
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
rather than having the dictionary defined in the program.
Bonus: 
Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.'''

import datetime
import json
import zad33

def loadBirthdayDict():
    with open('birthdays.json', 'r') as file_obj:
        return json.load(file_obj)

def addBirthdayData(birthday_dict):
    person_name = input('Give a name: ').title().strip()
    birthday_year = int(input('Give a year: '))
    birthday_month = int(input('Give a month (1-12): '))
    birthday_day = int(input('Give a day (1-31): '))
    person_birthday = datetime.date(birthday_year, birthday_month, birthday_day).strftime("%d/%m/%Y")
    birthday_dict[person_name] = person_birthday
    updateBirthdayDict(birthday_dict)
    
def updateBirthdayDict(birthday_dict):
    with open('birthdays.json', 'w') as file_obj:
        json.dump(birthday_dict, file_obj)

if __name__ == '__main__':
    print('Welcome to the birthday dictionary.')    
    birthdayDict = loadBirthdayDict()

    while True:
        nextAction = input('\nWhat do you want to do (Add/Find/List/Exit)? ').lower()
        print()
        if nextAction == 'add':
            addBirthdayData(birthdayDict)
            birthdayDict = loadBirthdayDict()
        elif nextAction == 'find':
            personName = zad33.askPersonName(birthdayDict)
            zad33.printBirthdayData(personName, birthdayDict)
        elif nextAction == 'list':
            zad33.printBirthdayDict(birthdayDict)
        elif nextAction == 'exit':
            break
        
        
